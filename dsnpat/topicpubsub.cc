#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>
#include <memory>
#include <unordered_map>

#include "statehasher.h"

using namespace std;

/*
 * Publisher  Events
 */

class Mediator;

class Publisher
{
  public:
    Publisher(Mediator *mediator, string name);
    ~Publisher() {};

    // Called by derived publisher to inform the attached mediator
    virtual void publish(Publisher * pb, EventType ev);

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

  /*
   * To be implemented by Subscriver and will be called
   * mediator to notify of the published event
   */
  virtual void update(EventType ev)= 0;

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

  /*
   * To be implemented by Subscriver and will be called
   * mediator to notify of the published event
   */
  virtual void update(EventType ev)= 0;

  protected:
    string  name_;
  private:
    Mediator *mediator_;
};


class Store: public Publisher
{
  public:
    Blockstore(Mediator *md, string name): Publisher(md, name){}

    void notify(EventType ev)
    {
        cout << name_ << " is  Publishing " <<  st[ev] << endl;
        // can make mediator protected to access it directly
        // iso via Publisher::publish. keeping private prevents
        // the Derived class from mucking around with mediator
        // reference.
        publish(this, ev);
    }
};

class Management: public Subscriber
{
  public:
    Management(Mediator *md, string name):Subscriber(md, name){};

    virtual void update(EventType ev)
    {
        cout <<  name_ << " received event "  << st[ev] << endl;
    }
};


class RemoteNode: public Subscriber
{
  public:
    RemoteNode(Mediator *md, string name):Subscriber(md, name){};

    virtual void update(EventType ev)
    {
        cout << name_ << " received event "  << st[ev] << endl;
    }
};

class Mediator
{
  public:

    Mediator(){};
    ~Mediator();
    /*
     * Bind the publisher and subscriber
     */
    virtual long attach(Publisher *pb, Subscriber *sub, vector<EventType> events);

    /*
     * Initiate notification to subscribers of the event
     */
    virtual void notify(Publisher *pub, EventType ev);

  private:
    // Used to publish to subscribers interested in event
    unordered_map<Publisher *,
        unordered_map<EventType, vector<Subscriber*>, StateHash<EventType> > > subscriber_map_;
    // used by subscriber to keep track of its subscription
    unordered_map<Subscriber *, int> sub_to_token_;

    // token used to uniquely identify subscriber objet
    // other oprations can be initiated usin the tokens
    long token_;
};



//+++++++ Publisher ++++++++++++++
Publisher::Publisher(Mediator *mediator, string name)
                :mediator_(mediator), name_(name){};

void
Publisher::publish(Publisher * pb, EventType ev) {
        mediator_->notify(pb, ev);
};

//+++++++++ Subscriber +++++++++++++
Subscriber::Subscriber(Mediator *mediator, string name)
                :mediator_(mediator), name_(name){};

// Mediator
Mediator::~Mediator(){ cout << " Mediator destroyed " << endl;}

void
Mediator::notify(Publisher *pub, EventType ev)
{
    cout << " Mediator notifying subscriber " << endl;
    // protect ##
    auto it = subscriber_map_.find(pub);
    if (it == subscriber_map_.end()) {
        cout << " Subscriber not found " << endl;
        return;
    }

    // notify all the subscriber interested in the event
    // need to do inside a lock or add a ref on the subscriber
    // do outside the lock. Protect ##
    auto sublist = it->second[ev];
    for(auto sub : sublist) {
        sub->update(ev);
    }
}

/*
 * events is the list of events published by "pb" in which the
 * "sub" is interested in
 * Return a token which uniquely identifies the subscriber
 */
long
Mediator::attach(Publisher *pb, Subscriber *sub, vector<EventType> events) {
    // find sub in subscriber to token map and if new genrate a  new token
    // Subscribe the sub to pub to all the events its interested in.
    cout << "Setting up subscriber " << endl;
    if(sub_to_token_.find(sub)== sub_to_token_.end()){
        //make it atomic. Not expensive as will be used only at setup
        // protect##
        token_++;
        sub_to_token_[sub]= token_; // need to protect
    }

    long sub_token = sub_to_token_[sub];

    // attach the subscriber to the publisher for all the event
    // should we give a unique name to pub
    // protect##
    auto pubit = subscriber_map_.find(pb);

    if(pubit == subscriber_map_.end()){
        // new publisher found
        subscriber_map_[pb];
    }

    // subscribe the events. will create id if not present or
    // add to existing map
    auto& subeventmap = subscriber_map_[pb];
    for(auto ev : events){
        auto it =  subeventmap.find(ev);
        if(it == subeventmap.end()){
            subeventmap[ev];
                    }
        subeventmap[ev].push_back(sub);
    }
    return sub_token;
}

int main()
{
    Mediator *md = new Mediator();
    Store *st  = new Store(md, "Store");
    Management *mgmt = new Management(md, "Management");
    RemoteNode *rn = new RemoteNode(md, "RemoteNode");

    //list of events that management is interested in
    vector<EventType> events = {
            EventType::LOCAL_READ_ERROR,
            EventType::LOCAL_WRITE_ERROR,
            EventType::REMOTE_IO_ERROR,
            EventType::NETWORk_ERROR,
           
    };

    long mgmt_token = md->attach(st, mgmt, events);
    long rnode_token = md->attach(st, rn, events);
    // should this be done in attach for the subscriber
    // may be but this will impose that subscriber provides
    // mgmt->set_token(mgmt_token)
    EventType ev = EventType::LOCAL_READ_ERROR;
    st->notify(ev);
}
