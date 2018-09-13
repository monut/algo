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

