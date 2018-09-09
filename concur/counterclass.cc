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


