
using namespace std;

class ThreadPool {
  private :
    int wrk_threads; 
    int tot_tasks;
    bool shutdown; // atomic ??
    queue<function<void(void)> > taskq; 
    vector<thread> threads;
    mutex taskq_mtx;
    mutex wait_mtx;
    condition_variable task_ready;
    condition_variable task_wait;
    
    void execute() {
        // continue executing till shutdown is called
        while(!shutdown){
          // function executed outside the lock to reduce the lock
          // hold time
          get_task()(); // get and execute the next function
          tot_tasks--;
          // need to notify ??
          task_wait.notify_one();
        }
    }
    
    function<void(void)>
    get_task() {
      function<void(void)> func;
      unique_lock<mutex> lck(taskq_mtx);
      // wait till tasks are enqued or shutdown initiated 
      task_ready.wait(lck,[this](){return (taskq.size() != 0 )|| shutdown;});
      if(!shutdown) {
        res = taskq.front(); taskq.pop();
      } else {
        // add the task so that get_task() logic goes through
        //  as is at shutdown.
        res = [](){};
        tot_tasks++;
      }
      return res.
    }
    
   public:
      ThreadPool(int num_threads):wrk_thds(num_threads),
                             tot_tasks(0), shutdown(false), finished(false);
                             
      {
      // create the worker threads and they will wait till
      // notified at jobs enqueue 
      for(int i = 0; i < wrk_threads; i++) {
          threads.push_back(thread([this](){this->execute();}));
      };
      
      ~ThreadPool() {
        // should tear down all threads and finish the job if possible
        // or decide to reqliquish the jobs
        jointhreads();
      }
      
      void
      addTask(function<void(void)> func) {
        // need to hold the lock before adding the queue
        lock_guard<mutex> lck(taskq_mtx);
        // can be augmented to provide the priority  with pair {func, priority}
        // which can be used in execute to decide  on the function to call.
        taskq.push(func);
        tot_tasks++;
        task_ready.notify_one();
      }
      
      void jointhreads(){
      
        if(!finished) {
          waitfortasks();
          // shutdown 
          shutdown = true;
          task_ready.notify_all();
          for(auto& thrd : threads) {
              if(thrd.joinable())
                  thrd.join();
             finshed = true;
        }
        
      }

      void waitfortasks(){
        
        if(tot_tasks > 0) {
          unique_lock<mutex> lck(wait_mtx);
          task_wait.wait(lck,[this](){return tot_tasks == 0;}
        }
      
      }
}
