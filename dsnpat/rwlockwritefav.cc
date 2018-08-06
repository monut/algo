class RWlock {

private:
    mutex mtx;
    conditon_variable rd_cv;
    conditon_variable wr_cv;
    int wrers; // can be 0 or 1
    int rders;
    int wr_waiters;
    Int rd_waiters;

public:

RWlock():wres(0), rders(0), wr_waiters(0), rd_waiters(0) {

}
write_lock() {
{
        unique_lock<mutex> wl(mtx);
        if(wrers || rders) {
            wr_waiters++;
            wr_cv.wait(wl, [this](){ return !(rders||wrers);}); // waiting till reader or writers
            wr_waiters—;
        }     
        wrers = 1;
 }

write_unlock() {
    unique_lock<mutex> wl(mtx);
    wrers = 0;
    If (wr_waiters) 
            wr_cv.notiffy_one()
    else if(rd_waiters)
            rd_cv.notify_one()
}

read_lock(){
        unique_lock<mutex> rl(mtx);
        if(wers || wr_waiters) {
            rd_waiters++;
            rd_cv.wait(rl, [this]() { return !(wrers||wr_waiters);});
            read_waiters—;
        }
        readers++;
}

read_unlock() {
        unique_lock<mutex> rl(mtx);
        readers—;
        if(wr_waiters)
                wr_cv.notify_one(); 
}

}
