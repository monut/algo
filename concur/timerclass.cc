/*
Implement a timer class.  The goal of the class is to defer work for n milliseconds and execute the 
work on a background thread.  The defer function should return quickly and should not call the callback 
function itself.  You can assume you have a ThreadPool class available to help you schedule work if you want.
Callbacks should be run as soon as possible after the delay is satisfied. 

*/

//  optional helper class  (cannot be modified)
typedef void (callback*)(void*);

Class ThreadPool {
    static void doWork(callback, void *data);
}

// You need to implement
Class Timer {
public:
    Timer();
    defer(callback, void* data, int delayMS);
    double get_time(){
        steady_time::now();
    }
private:
    
    mutex mtx_;
    condition_variable cn_
    multimap<double,pair< function(void*()), void *> > map_;  
};

Tmer::Timer(){

}

Timer::main_thread() {
    double time = 1;
        mtx.wait();
    while(1) {
        
        while (!list || !list.peek().shouldBeScheduled()) {
            time = (!list)? INFINITE: now() - list.peek().time;
            cv.wait(time);
        }
        auto rng = map_.upper_bound(now_time);
        for(auto st = map_.begin(); st != rng; st++){
           ThreadPool::do_work(st->first, st->second);
           
        }
        // remove submitted work
    }
    
        mtx.signal();
}

Timer::defer(callback, void* data, int delayMS){
    double cur_time = get_time();
   lock_guard<mutex> lck(mtx_);
   map_[cur_time + delayMS] = {callback, data};
   cv.signal();
  
}

Timer::schedule_event(){
   double now_time = get_time();
   {
   ` lock)guard<mutex> lck(mtx_);
     auto rng = map_.upper_bound(now_time);
    for(auto st = map_.begin(); st != rng; st++){
       ThreadPool::do_work(st->first, st->second);
    }
   
   }
  
   ThreadPool::doWork(bind(this,schedule_event()));

}
















