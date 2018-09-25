#include <iostream>
#include <map>
#include <string>
#include <thread>
#include <cstring>

using namespace std;


class Message {
  void* _data;
  size_t _length;

 public:
  Message(void* data, size_t length);

  void Ack();

  void Nack();

  void* data();

  size_t length();
};

class Queue {

  static map<string,Queue*> queues;
  Message* msg;

  Queue();

 public:
  static Queue* getQueue(string name);
  Message* getMessage();
  void putMessage(Message* message);
};

class Server {
 public:
  Server() {
  }

  void serve() {
    // Receive message
    cout << "Receive message" << endl;
    cout << "Add numbers" << endl;
    cout << "Returning response" << endl;
  }
};

int adder(int x, int y) {
  cout << "Send message" << endl;
  cout << "Returning response" << endl;

  return 0;
}

int main() {
  Server s;
  std::thread server(&Server::serve, &s);
  server.join();

  cout << adder(1, 2) << endl;
}


Message::Message(void* data, size_t length) {
  this->_data = malloc(length);
  memcpy(this->_data, data, length);
  this->_length = length;
}

void Message::Ack() {
}

void Message::Nack() {
}

void* Message::data() {
  return this->_data;
}

size_t Message::length() {
  return this->_length;
}

map<string,Queue*> Queue::queues;
Queue::Queue() {
  msg = nullptr;
}

Queue* Queue::getQueue(string name) {
  if (queues.find(name) != queues.end()) {
    return queues[name];
  }

  Queue* q = new Queue();
  queues[name] = q;
  return q;
}

Message* Queue::getMessage() {
  return this->msg;
}

void Queue::putMessage(Message* message) {
}
