/** A thread-safe FIFO queue with a size limit. */
#include <pthread.h>
#include <queue>

template <typename T>
class BlockingQueue {
public:
    /** Retrieve and remove the head of the queue, waiting if no elements are present. */
    virtual T* take() = 0;

    /** Add the given element to the end of the queue, waiting if necessary for space to become available. */
    virtual void put (T* obj) = 0;

    virtual ~BlockingQueue() {}
};

template <typename T>
class myBlockingQueue : public BlockingQueue {
public :
    myBlockingQueue();
    ~myBlockingQueue();
protected:
    queue<T *obj> _myqueue;
    pthread_muex_t _lck;
    pthread_cond_t _putcnd
    pthread_cond_t _takeqcnd
    static const int qSize = 16;
}

template <typename T>
myBlockingQueue<T>::myBlockingQueue() {
    pthread_mutex_init(&_lck, NULL);
    pthread_cond_init(&_putcnd, NULL);
    pthread_cond_init(&_takecnd, NULL);
}

template <typename T>
myBlockingQueue<T>::myBlockingQueue() {
    pthread_mutex_destroy(&_lck);
    pthread_cond_destroy(&_putcnd);
    pthread_cond_destroy(&_takecnd);
}

template <typename T>
void
myBlockinQueue<T>::put(T *obj) {
    pthread_mutex_lock(&_lck)
    while(myqueue.size() >= BlockinQueue::qSize){
        pthread_cond_wait(&_putcnd,&_lck);
    }
    myqueue.push(obj);
    pthread_cond_signal(&_takecnd);
    pthread_mutex_unlock(&_lck)
}

template <typename T>
T *myBlockinQueue<T>::take() {
    T *obj = NULL;
    pthread_mutex_lock(&_lck)
    while(myqueue.empty()){
        pthread_cond_wait(&_takecnd, &_lck);
    }

    obj = myqueue.front();
    myqueue.pop();
    pthread_signal(qcnd);
    pthread_mutex_unlock(qlck)
    return obj;
}
