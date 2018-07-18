#include <iostream>
#include <queue>
#include <mutex>
#include <functional>

using namespace std;

class Taskobj {
    int val_;

    public:
        Taskobj(int val = 0):val_(val){};

        void operator()(int a){
            cout << "the value set " << val_ << endl;
            cout << "the value send " << a << endl;
        }
};

class Dispatcher {
    private:
        queue<function<void(int)> > taskq_;
        mutex mtx_;

    public:
        Dispatcher(){};

        void addtask(function<void(int)> func);
        void dispatchtask();
};

void
Dispatcher::addtask(function<void(int)> func){

        lock_guard<mutex> lck(mtx_);
        taskq_.push(func);
}

// dispatch function based on event
// also multiple and varying arguement to function or different object
// type. Template dispatch class
void
Dispatcher::dispatchtask(){

    queue<function<void(int)> > localq;

    {
        lock_guard<mutex> lck(mtx_);
        localq.swap(taskq_);
    }

    // for range loop use deque as it supports begin()
    // end()
    // for(auto& f : localq){
    while(!localq.empty()){
        auto f = localq.front();
        f(2);
        localq.pop();
    }
}

void taskg(int a) {
    cout << "global task " << a << endl;
}

class Callback {
    int val_;
    public:
        Callback(int val = 0):val_(val){};
        void my_func(int a) {
            cout << "Callback done  set " << val_ << endl;
            cout << " value sent " << a;
        }
};

int
main(){

    // add tasks
    Taskobj tobj(5);

    Dispatcher dsp;

    dsp.addtask(tobj);

    auto tobj2 = [](int a){ cout << "value sent lmda " << a << endl;};
    dsp.addtask(tobj2);

    dsp.addtask(taskg);

    Callback cb(45);

    dsp.addtask(bind(&Callback::my_func, &cb, placeholders::_1));

    dsp.dispatchtask();
}

