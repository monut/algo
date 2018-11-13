#include "crawl_helper.h"

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

    void put(string val){
      unique_lock<mutex> lck(mtx_);
      if(bq_.size() >= cap_){
        cv_full.wait(lck,[this](){return bq_.size() < cap_;});
      }
      bq_.push(val);
      cv_empty.notify_one();
    };

    string get(){
        unique_lock<mutex> lck(mtx_);
        if(bq_.empty()){
          cv_empty.wait(lck,[this](){return !bq_.empty();});
        }
        string val = bq_.front();
        bq_.pop();
        cv_full.notify_one();
        return val;
    };
};
~                                               
