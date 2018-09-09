#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>
#include <memory>
#include <unordered_map>

using namespace std;

class Mediator;

class Publisher
{
  public:
    Publisher(Mediator *mediator, string name);
    ~Publisher() {};

    virtual void publish(Publisher * pb, int ev);

  protected:
    string  name_;
  private:
    Mediator *mediator_;
};

class Subscriber
{
  public:
    Subscriber(Mediator *mediator, string name);

   ~Subscriber() {};
    virtual void update(int ev)= 0;

  protected:
    string  name_;
  private:
    Mediator *mediator_;
};
class Pub1: public Publisher
{
  public:
    Pub1(Mediator *md, string name): Publisher(md, name){}

    void notify(int ev)
    {
        cout << "   " << name_ << " Publishing " << endl;
        publish(this, ev);
    }
};

class Sub1: public Subscriber
{
  public:
    Sub1(Mediator *md, string name):Subscriber(md, name){}

    virtual void update(int ev)
    {
        cout << "   " << name_ << " received event " << ev << endl;
    }
};

class Mediator
{
  public:

    Mediator() { };
    virtual ~Mediator();
    virtual void attach(Publisher *pb, Subscriber *sub);

    virtual void notify(Publisher *pub, int ev);

  private:
    unordered_map<Publisher *, vector< Subscriber*> > subscriber_map_;
};

// publisher

void
Publisher::publish(Publisher * pb, int ev) {
        mediator_->notify(pb, ev);
};

// Subscriber
Subscriber::Subscriber(Mediator *mediator, string name)
                :mediator_(mediator), name_(name){};
// Mediator
Mediator::~Mediator(){ cout << " Mediator destroyed " << endl;}

void
Mediator::notify(Publisher *pub, int ev)
{
    cout << " Mediator notifying subscriber " << endl;
    auto it = subscriber_map_.find(pub);
    if (it != subscriber_map_.end()) {
        for(auto subs : it->second ){
              subs->update(ev);
        }
    }
}

void
Mediator::attach(Publisher *pb, Subscriber *sub) {
    auto it = subscriber_map_.find(pb);
    cout << " setting up subscriber " << endl;
    if(it != subscriber_map_.end()){
        it->second.push_back(sub);
    } else {
        subscriber_map_[pb] = {sub};
    }
}
int main()
{
    Mediator *md = new Mediator();
    Pub1 *pub1  = new Pub1(md, "Pub1");
    Sub1 *sub1 = new Sub1(md, "Sub1");
    md->attach(pub1, sub1);
    int ev = 1;
    pub1->notify(ev);
}
          
