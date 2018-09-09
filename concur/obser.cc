#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Observer {
 public:
    virtual ~Observer(){};
    virtual void update(int val) = 0;
};

class Subject {
    int status_;
    vector<Observer *> lst_;
public:
    ~Subject(){};

    virtual void attach(Observer *ob) = 0;

    virtual void set_value(int status) = 0;

    virtual void notify() = 0;
};

class Sub1: public Subject {

public:
    Sub1(){};

    void attach(Observer *ob) override {
        lst_.push_back(ob);
    }

    void set_value(int status) override {
        status_ = status;
        notify();
    }

    void notify() override {
        for(auto ob : lst_){
            ob->update(status_);
        }
     }
}

class Ob1 : public Observer
{
    int my_status_;
  public:
    Ob1(Subject *sub, int status)
    {
        my_status_ = div;
        sub->attach(this);
    }
    void update(int status)
    {
        cout << " My Old status " << status << endl;
        cout << " My New status " << status_ << endl;
        status_ = status;
    }
};

int main()
{
  Sub1 *sub1;
  Ob1 ob1(sub1, 4);
  sub1->set_value(2);

}


