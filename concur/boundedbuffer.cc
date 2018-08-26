/*
  queue of certain capacity. consumers block if empty or block if full
 */
 
 class boundedQ {
 private :
    mutex mtx_;
    condition_variable cv_full;
    condition_variable cv_empty;
    queue<int> bq_;
    int cap_;
 public :
    boundedQ(int cap):cap_(cap){};
    void put(int val){
      unique_lock<mutex> lck(mtx_);
      if(bq_.size() >= cap_){
        cv_full(lck,[this](){return bq_.size() < cap_;})
      }
      bq_.push(val);
      cv_empty.notify_one();
    };
    
    int get(){
        unique_lock<mutex> lck(mtx_);
        if(bq_.empty()){
          cv_empty(lck,[this](){return !bq_.empty();})
        }
        int val = bq_.front();
        bq_.pop();
        cv_full.notify_one();
        ret val;
    };
 
 }
