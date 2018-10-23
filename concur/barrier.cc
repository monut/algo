#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

pthread_mutex_t mtx_lck;
pthread_cond_t cond;
int TCount = 16;
void
do_the_work(void *ptr){
    // do some work
    int i = (int)ptr;
    printf(" I am thread ## %d\n",i);
    sleep(2);
    pthread_mutex_lock(&mtx_lck);
    TCount--;
    if(TCount == 0) {
        printf(" I am going to WAKEUP and I am  thread ##  %d\n",i);
        pthread_cond_broadcast(&cond);
    }
    while(TCount) {
        printf(" I am going to WAIT thread ##  %d\n",i);
        pthread_cond_wait(&cond, &mtx_lck);
    }
    pthread_mutex_unlock(&mtx_lck);

    printf(" I am thread ##  And DONE %d\n",i);
}

int main()
{
    pthread_mutex_init(&mtx_lck, NULL);
    pthread_cond_init(&cond, NULL);
    pthread_t t[16];
    int i = 0;
    // create threads
    for(i = 0; i < 16; i++) {
        pthread_create(&t[i], NULL,(void *(*)(void *))do_the_work, (void *)i);
    }

    for(i = 0; i < 16; i++) {
        pthread_join(t[i], NULL);
    }
}
