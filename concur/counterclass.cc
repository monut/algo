/*
  void inc(int va);
  int get_val();
  
 chrono::time_point<chrono::system_clock> t = chrono::system_clock::now();
 this_thread::sleep_for(chrono::seconds(3));  
 auto diff = chrono::system_clock::now() - t;    
 cout << chrono::duration_cast<chrono::seconds>(diff).count();
}
 */
 
#include <iostream>
#include <vector>
#include <mutex>
#include <chrono>
using namespace std;

class CounterClass{
  private :
    unsigned int cnt_;
    vector<int> sum_; 
    chrono::time_point<chrono::system_clock> start_time_;
    mutex mtx_; // atomic<unsigned int> cnt_  no need for lock
    double get_time(){
         auto diff = (chrono:system_clock::now() - start_time_);
         return duration_cast<chrono::minutes>(diff).count();
    }
    
  public :
    CounterClass(){
        start_time_ = chrono::system_clock::now(); cnt_ = 0};
    
    void inc(unsigned int val){
         guard_lock<mutex> lck(mtx_);
         cnt_ += val;
         double tmnt  = get_time(); 
         // atomic_exchange(sum_[tmnt], cnt_);
         sum_[tmnt] = cnt_; 
    };
    
    unsigned int get_val(unsigned int st_range, 
                         unsigned int en_range ) {
        return  (sum_[en_range] - sum_[st_range]);
    }  
  
 }


#include <iostream>
#include <map>
#include <mutex>
#include <cstdint>

enum class Type {
    LAST_MNT,
    LAST_HR,
    LAST_DAY,
};

class CounterClass {
    private:
        // map<double, vector<int> >
        // how to prune. May be queue per minute and
        // also maintain a hmap
        map<int64_t, int> cnt_;
        mutex mtx_;
        time_point<chrono::system_clock> start_time_;
        int64_t get_time(){
            auto t = chrono::system_clock::now();
            /*
                this_thread::sleep_for(2s)// sleeps for 2 seconds
             */
            return duration_cast<chrono::seconds>(t-start_time_).count();

        }
        void prune_old_entries() {
            // get the enteries older than a now - 1400
            // and drop them from hash table
            auto itu = cnt_.lower_bound(t - 1400);
            // erase [begin() , itu) not including upper bound
            cnt_.erase(cnt_.begin(), itu--);
        }
    public:
        CounterClass():start_time_(chrono::system_clock::now()){};
       void  addEvents(uint64_t val);
       int64_t  getNumEvents();
}

void
CounterClass::addEvents(uint64_t val) {
    /*
    can use atomic counter and use tes_and_set()
    local_val = cnt_.get(); new_val = local_val + val;
    while(!test_and_test(local_val, new_wal){local_val = cnt_.get(); new_val = local_val + val;}
    */
  
    // based on thread id take a bucket lock
    // aggregate the stats when ?
    int64_t t = get_time();
    unique_lock<mutex> lck(mtx_);
    if(cnt_.find(t) == cnt_.end()){
        // find lower bound for the t-1
        /*
          if(cnt_.size() != 0) then only can do it--;
          auto it = cnt_.end(); it--;
          cnt[t] = it->second + val;
        */
        if(cnt_.find(t-1) == cnt_.end()) {
            auto it =  cnt_.upper_bound(t-1);
            if(it == cnt_.end()) it--;
            cnt_[t] = it->second + val;
        } else {
            cnt_[t] = cnt[t-1] + val;
        }
    } else {
        cnt_[t] += val;
    }
}

uint64_t
CounterClass::getNumEvents(Type et){
    int64_t t = get_time();
    unique_lock<mutex> lcl(mtx_);
    if(et == Type::LAST_MNT) {
        if(cnt_.find(t-1) {
            return cnt_[t-1];
        }
    } else if(et == Type::LAST_HR || et == Type::LAST_DAT) {
        int64_t dif = 60;
        if(et == Type::LAST_DAY) {
            dif == 24*60;
        }
        auto itl = cnt_.lower_bound(t-dif);
        auto itu = cnt_.upper_bound(t);
        if(itu == cnt_.end()){
            itu--;
        }
        if(itu == itl) return itl->second);
        return (itu->second - itl->second);
    }
    return 0;
}


