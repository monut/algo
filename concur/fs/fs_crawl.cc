#include <iostream>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <string.h>
#include "bounded_queue.h"
using namespace std;
// change to configurable value
static const size_t number_of_threads = 4;
// handle case if queue capacity is reached
// keep capacity high
static const size_t queue_capacity = 40;
auto dir_q = new boundedQ(queue_capacity);
vector<thread> _thread_pool;
// {thread_id, {path, inode }}
// to be dumped to disk for the time being represeting
// in mem
unordered_map<thread::id, vector<pair<string, int> > >
                                        _per_thread_fileinfo;

static void process_file(string file_name) {
  struct stat buf;
  if(lstat(file_name.c_str(), &buf) < 0){
    cout << " Error in lstat of " << file_name;
  }
  // cout << "File: " << file_name  << endl;
  // cout << "File Inode :" << buf.st_ino << endl;
  _per_thread_fileinfo[this_thread::get_id()].emplace_back(file_name,
                                                        buf.st_ino);
}
static bool is_directory(const string& file_name) {
  struct stat sb;
  if(lstat(file_name.c_str(), &sb) == -1) {
    cout << " Unable to stat the file" << endl;
    return false;
  }
  if(S_ISDIR(sb.st_mode)) return true;
  return false;
}

static void get_filedir_list(string file_name){
  struct dirent *dptr;
  DIR *dir = opendir(file_name.c_str());
  if(dir == nullptr){
    cout << "ERROR : unable to opendir " << file_name << endl;
    return;
  }

  process_file(file_name);
  while((dptr = readdir(dir)) != nullptr){
    if (strcmp(dptr->d_name,".") && strcmp(dptr->d_name,"..")) {
      string tmp_name = file_name + "/" + string(dptr->d_name);
      if(is_directory(tmp_name)) {
        dir_q->put(tmp_name);
        cout << tmp_name <<  " Is Directory " << endl;
      } else {
        process_file(tmp_name);
      }
    }
  }
  closedir(dir);
}

/* support where d_type is supported by FS */
static void get_filedir_list_ext4(string file_name){
  struct dirent *dptr;
  DIR *dir = opendir(file_name.c_str());
  if(dir == nullptr){
    cout << "ERROR : unable to opendir " << file_name << endl;
    return;
  }
  process_file(file_name);
  while((dptr = readdir(dir)) != nullptr){
    if(dptr->d_type == DT_DIR &&
          (strcmp(dptr->d_name,".") && strcmp(dptr->d_name,".."))) {
      string tmp_name = file_name + "/" + string(dptr->d_name);
      // cout << " Directory Entries " << dptr->d_name << endl;
      dir_q->put(tmp_name);
    } else {
      string tmp_name = file_name + "/" +  string(dptr->d_name);
      process_file(tmp_name);
      // cout << " Other File Types " << dptr->d_name << endl;
    }
  }
  closedir(dir);
}

static void execute() {
  // cout << "Executing thtead :: " << this_thread::get_id() << endl;
  _per_thread_fileinfo[this_thread::get_id()];
  while(1) {
    string file_name = dir_q->get();
    if(file_name == "EOQ") break;
    get_filedir_list(file_name);
  }
}

// iterate through map
void print_collected_info(){
  for(auto& elem : _per_thread_fileinfo) {
    cout << " +++++++++++++++++++++++++++++++++++++++++++++" << endl;
    cout << " Info collected by Thread: " << elem.first << endl;
    cout << " +++++++++++++++++++++++++++++++++++++++++++++" << endl;
    auto info_vec = elem.second;
    for(auto &pr : info_vec){
       cout << "File Name : " << pr.first;
       cout << " File Inode  : " << pr.second << endl;
    }
    cout << endl;
    cout << endl;
  }
}

int
main(int argc, char *argv[]){
    if(argc < 2) {
      cout << " No Seed Directory given " << endl;
      return 0;
    }

    int file_count = argc-1;
    struct stat buf;
    cout << "Seed File :" <<  argv[1] << endl;
    dir_q->put(argv[1]);
    // create worker threads
    for(int i = 0; i < number_of_threads ; i++){
        _thread_pool.push_back(thread(execute));
    }
    
    
    for(auto& thr : _thread_pool){
      thr.join();
    }
    print_collected_info();
    cout << " Exiting now" << endl;
}


