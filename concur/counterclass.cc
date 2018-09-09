/*
  void inc(int va);
  int get_val();
 */
 
 class CounterClass{
  private :
    vector<double> cnt_;
    double start_time_;
    
  public :
    void inc(int val);
    int get_val(int last_mins);  
  
 }
