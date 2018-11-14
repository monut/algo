 /*
 *   put and get directories  
 */
#include "crawl_helper.h"
#include <chrono>

static const int wait_time_ = 2; // seconds
class boundedQ {
 private :
    mutex mtx_;
    condition_variable cv_full;
    condition_variable cv_empty;
    queue<string> bq_;
    int cap_;
 public :
    boundedQ(int cap):cap_(cap){};
    bool isempty() {
        lock_guard<mutex> _(mtx_);
        return bq_.empty();
    }
    
    bool put(string val){
      unique_lock<mutex> lck(mtx_);
      if(bq_.size() >= cap_){
        cv_full.wait_for(lck,chrono::seconds(2),
                  [this](){return bq_.size() < cap_;});
      }
      bq_.push(val);
      cv_empty.notify_all();
    };
    
    string get(){
        unique_lock<mutex> lck(mtx_);
        if(bq_.empty()){
          cv_empty.wait_for(lck, chrono::seconds(wait_time_), 
                                [this](){return !bq_.empty();});
        }
        if(bq_.empty()) {return "EOQ";};
        string val = bq_.front();
        bq_.pop();
        cv_full.notify_all();
        return val;
    };
};
                                            
