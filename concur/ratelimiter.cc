/*
  Allow N request in a max interval
  Insert time in q till the limit of Q is reached
  Then if element in front of queue id within time 
  interval process the elem and push the cur time
  drop the current request if the element in front 
  is not outside the interval.
 */
queue<double> q;
int N = MAX_ALLOWED;
double max_interval = 5; // ms
RateLimiter(Req& r) {
  double cur_time = get_time();
  if(q.size() < N) {
      do_work(r);
      q.push(cur_time);
  } else {
    auto tm_front = q.front();
   
    if(cur_time - tm_front > max_interval){
      do_work(r);
      q.push(cur_time);
      q.pop();
    } else {
      do_drop(r);
    }
  }

}
