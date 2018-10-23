#include "file_cache.h"



//forward declaration

static void insert_file_nodes(struct file_cache *fc,
                const char **files, int num_files);
static void remove_file_nodes(file_cache_t *fc,
                const char **files, int num_files) ;
static int find_cached_nodes(struct file_cache *fc,
                const char **files, int num_files);

//  globals
#define FILE_SIZE 1024 * 10

// Constructor. 'max_cache_entries' is the maximum number of files that can
// be cached at any time.
// will return NULL if allocation fails or max_cache_entries is zero
struct file_cache *
file_cache_construct(int max_cache_entries) {
  int ret = 0;
  if(!max_cache_entries) {
    return NULL;
  }
  file_cache_t *fc = malloc(sizeof(struct file_cache));
  if(!fc) {
    return NULL;
  }
  fc->max_cache_entries = max_cache_entries;
  fc->free_node_cnt = max_cache_entries;
  fc->file_nodes = NULL;
  if((ret = pthread_mutex_init(&fc->fc_cond_mtx, NULL))) {
    printf("mutex initialization error \n");
    free(fc);
    return NULL;
  }
  if((ret = pthread_cond_init(&fc->fc_cond, NULL))) {
    printf("condition initialization error \n");
    free(fc);
    return NULL;
  }
  return fc;
}

// Destructor. Flushes all dirty buffers.
// will deallocate all buffers, pinned or unpinned 
void
file_cache_destroy(struct file_cache *cache) {
  if(!cache) {
    return;
  }
  pthread_mutex_lock(&cache->fc_cond_mtx);
  file_node_t *fn_list = cache->file_nodes;
  file_node_t *tmpn = NULL;
  while(fn_list) {
    if(fn_list->dirty_flag == 1) {
        if (lseek(fn_list->fdin, 0, SEEK_SET) == -1)
                printf("lseek error\n");
        if (write(fn_list->fdin, fn_list->file_buf, FILE_SIZE) != FILE_SIZE)
                printf("write error \n");
        close(fn_list->fdin);
        free(fn_list->file_buf);
    }
    tmpn = fn_list;
    fn_list = fn_list->next;
    free(tmpn);
  }

  pthread_mutex_unlock(&cache->fc_cond_mtx);
  free(cache);
}

// will block if the total free nodes are less than needed
// caller should ensure the validity of files and number of
// files being pinned
void
file_cache_pin_files(struct file_cache *cache,
                          const char **files,
                          int num_files) {
  int cach_cnt = 0;
  if(!cache) {
    return;
  }
  pthread_mutex_lock(&cache->fc_cond_mtx);
  // need free nodes only for files not already cached
  cach_cnt = find_cached_nodes(cache, files, num_files);
  while(cache->free_node_cnt < (num_files - cach_cnt)) {
    pthread_cond_wait(&cache->fc_cond, &cache->fc_cond_mtx);
    cach_cnt = find_cached_nodes(cache, files, num_files);
  }
  insert_file_nodes(cache, files, num_files);
  pthread_mutex_unlock(&cache->fc_cond_mtx);
}

// finds files which are already there in the file cache
static int
find_cached_nodes(struct file_cache *fc, const char **files, int num_files) {
  int i = 0;
  int found = 0;
  for(;i < num_files; i++) {
    file_node_t *fn_list = fc->file_nodes;
    while(fn_list) {
        if(strcmp(files[i], fn_list->file_name) == 0) {
            found++;
        }
        fn_list = fn_list->next;
    }
  }
  return found;
}
// Inserts files in the file cache
static void
insert_file_nodes(struct file_cache *fc, const char **files, int num_files) {
  int i = 0;
  for(;i < num_files; i++) {
    file_node_t *fnfree_p = NULL;
    file_node_t *fn_list = fc->file_nodes;
    int found = 0;
    while(fn_list) {
        if(strcmp(files[i],fn_list->file_name) != 0) {
            if(fn_list->dirty_flag == 0 && fn_list->pin_cnt == 0) {
                // tag the free node
                fnfree_p = fn_list;
            }
            fn_list = fn_list->next;
            continue;
        } else {// found same file 
            found = 1;
            break;
        }
    } // while loop
    if (found) {
        if(fn_list->pin_cnt == 0) {
            fc->free_node_cnt --;
        }
        fn_list->pin_cnt ++;
        continue;
    } else {
        int fdin =0;
        // decrement the free count
        fc->free_node_cnt --;
        if(!fnfree_p) {
          // create a new node
            fnfree_p = (file_node_t *)malloc(sizeof(file_node_t));
            fnfree_p->next = fc->file_nodes;
            fc->file_nodes = fnfree_p;
            fnfree_p->file_buf = (char *)malloc(FILE_SIZE);
            fnfree_p->dirty_flag = 0;
        } else {
            close(fnfree_p->fdin);
        }
        bzero(fnfree_p->file_buf, FILE_SIZE);
        strcpy(fnfree_p->file_name, files[i]);
        fnfree_p->pin_cnt++;

        /* open/create the output file */
        if ((fdin = open (files[i], O_RDWR, S_IRUSR |
                S_IWUSR | S_IRUSR | S_IRGRP | S_IROTH)) < 0) {
            if(errno == ENOENT) {
                // create a file if doest exist and write zeros
                if ((fdin = open (files[i], O_RDWR | O_CREAT, S_IRUSR |
                    S_IWUSR | S_IRUSR | S_IRGRP | S_IROTH)) < 0) {
                    printf ("unable to  create file %s ",files[i]);
                    assert(0);
                }

                if (write (fdin, fnfree_p->file_buf, FILE_SIZE) != FILE_SIZE) {
                    printf("write error \n");
                    assert(0);
                }
            } else {
                printf ("unable to open file %s ",files[i]);
                assert(0);
            }
        } else {
            read(fdin, fnfree_p->file_buf, FILE_SIZE);
        }
        fnfree_p->fdin = fdin;
    } // ! found
  } // for loop
}

// unpins  files  and flush any dirty files if pin count goes 
// to zero
void
file_cache_unpin_files(struct file_cache *cache,
                            const char **files,
                            int num_files){
  if(!cache) {
    return;
  }
  pthread_mutex_lock(&cache->fc_cond_mtx);
  remove_file_nodes(cache, files, num_files);
  pthread_cond_signal(&cache->fc_cond);
  pthread_mutex_unlock(&cache->fc_cond_mtx);
}

// decrements the pin count and flsuhes the dirty buffers if pin count 
// goes to zero. Ignore the the file names not in the cache
static void
remove_file_nodes(file_cache_t *fc,
        const char **files,
        int num_files) {
  int i = 0;
  for(;i < num_files; i++) {
    file_node_t *fn_list = fc->file_nodes;
    int found = 0;
    while(fn_list) {
        if(strcmp(files[i], fn_list->file_name) != 0) {
                fn_list = fn_list->next;
                continue;
            } else {// found  file 
                found = 1;
                break;
            }
    }
    if (found) {
        fn_list->pin_cnt--;
        if (fn_list->pin_cnt == 0) {
            if (fn_list->dirty_flag == 1) {
                if (lseek (fn_list->fdin, 0, SEEK_SET) == -1) {
                    printf("lseek error\n");
                    assert(0);
                }
                if (write (fn_list->fdin, fn_list->file_buf, FILE_SIZE) != FILE_SIZE) {
                    printf("write error \n");
                    assert(0);
                }
                fn_list->dirty_flag = 0;
            }
            // got one free node only when we find one to reclaim 
                fc->free_node_cnt++;
        }
    } // found
  } // for loop
}

// read access to pinned file
// returns NULL if node not found
// Files should not be unpinned while accessing the buffer 
const char *
file_cache_file_data(struct file_cache *cache,
                const char *file){

  if(!cache) {
    return NULL;
  }
  pthread_mutex_lock(&cache->fc_cond_mtx);
  file_node_t *fn_list = cache->file_nodes;
  int found = 0;
  while(fn_list) {
    if(strcmp(file, (const char *)fn_list->file_name) == 0) {
        found = 1;
        break;
    }
    fn_list = fn_list->next;
  }
  pthread_mutex_unlock(&cache->fc_cond_mtx);
  if(found && fn_list->pin_cnt > 0) {
    return fn_list->file_buf;
  } else  {
    return NULL;
  }
}

// write access to pinned file 
// returns NULL if node not found
// Files should not be unpinned while accessing the  buffer
char *
file_cache_mutable_file_data(struct file_cache *cache,
                    const char *file) {
  if(!cache) {
    return NULL;
  }
  pthread_mutex_lock(&cache->fc_cond_mtx);
  file_node_t *fn_list = cache->file_nodes;
  int found = 0;
  while(fn_list) {
    if(strcmp(file, (const char *)fn_list->file_name) == 0) {
        if(fn_list->pin_cnt > 0) {
                fn_list->dirty_flag = 1;
            found = 1;
        }
        break; // no duplicates so break here either way
    }
    fn_list = fn_list->next;
  }
  pthread_mutex_unlock(&cache->fc_cond_mtx);

  if(found) {
    return fn_list->file_buf;
  } else {
    return NULL;
  }
}
