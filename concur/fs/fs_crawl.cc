include <iostream>
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
static const size_t queue_capacity = 10;
auto dir_q = new boundedQ(10);
vector<thread> _thread_pool;

static void process_file(string file_name) {
  struct stat buf;
  if(lstat(file_name.c_str(), &buf) < 0){
    cout << " Error in lstat of " << file_name;
  }
  cout << "File: " << file_name  << endl;
  cout << "File Inode :" << buf.st_ino << endl;
}

static void get_filedir_list(string file_name){
  struct dirent *dptr;
  DIR *dir = opendir(file_name.c_str());
  if(dir == nullptr){
    cout << "unable to opendir " << file_name << endl;
    return;
  }
  process_file(file_name);
  while((dptr = readdir(dir)) != nullptr){
    if(dptr->d_type == DT_DIR &&
          (strcmp(dptr->d_name,".") && strcmp(dptr->d_name,".."))) {
      string tmp_name = file_name + "/" + string(dptr->d_name);
      cout << " Directory Entries " << dptr->d_name << endl;
      dir_q->put(file_name);
      cout << tmp_name << endl;
    } else {
      string tmp_name = file_name + "/" +  string(dptr->d_name);
      process_file(tmp_name);
      cout << " File Entries " << dptr->d_name << endl;
      // cout << " Other File Types " << dptr->d_name << endl;
    }
  }
  closedir(dir);
}
static void execute() {
  cout << "Executing thtead :: " << this_thread::get_id() << endl;
  while(1) {
    string file_name = dir_q->get();
    get_filedir_list(file_name);
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
    cout << "Number of fles to process :" << file_count << endl;
    for(int i = 1; i <= file_count; i++){
        if(lstat(argv[i], &buf) < 0){
            cout << " Error in lstat of " << argv[i];
        }
        cout << "File: " << argv[i] << endl;
        cout << "File Inode :" << buf.st_ino << endl;
    }
    dir_q->put(argv[1]);

    // create worker threads
    for(int i = 0; i < number_of_threads ; i++){
        _thread_pool.push_back(thread(execute));
    }

    for(auto& thr : _thread_pool){
      thr.join();
    }
    cout << " Exiting now" << endl;
}


