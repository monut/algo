
/*
 Store back pointer(iterator) from unordered_map <int, iterator> to list<pair<init, int>>.  
 {key, vaue}. insert in front of the list and lst.begin() gives an iterator to the inserted 
 elemnet and that can be used to map[key] = lst.begin().  Evict from the back.
 */

class Lru {
    private:
        int cap_;
        // {key, value}
        list<pair<int, int > > lru_;
        // {key, iterator}
        unordered_map<int, list<pair<int, int> >::iterator> kptr_;
        
        void evict(){
            auto val = lru_.back();
            lru_.pop_back();
            kptr_.erase(val.first);
        };
        
        void add_to_lru(int key, int val){
            lru_.emplace_front(key,val);
            kptr_[key] = lru_.begin();
        }
    
    public:
    Lru(int cap = 10):cap_(cap){};
    
    
    void set(int key, int val){
        auto it = kptr_.find(key);
        if(it == kptr_.end()){// new key
            if(lru_.size() == cap_) {
                evict();
            }
            
        } else {
           lru_.erase(it->second);      
        }
        add_to_lru(key, val);
        
    };
    
    int get(int key) {
        auto it = kptr_.find(key);
        if(it == kptr_.end())
            return -1;
        int val = it->second->second;
        lru_.erase(it->second);
        add_to_lru(key, val);
        return val;
    }
};

#if 0

class Lru {
    private:
        int cap_; 
        list<pair<int, int> > lru_;
        unordered_map<int, list<pair<int, int> >::iterator > map_;
    
        void evict_lru(){
            auto pr = lru_.back();
            map_.erase(pr.first);
            lru_.pop_back();
        }
    
        void add_to_lru(int key, int val){
            lru_.emplace_front(key, val);
            map_[key] = lru_.begin();
        }
    
    public:
        Lru(int val):cap_(val){};
        int 
        get(int key){
            auto it = map_.find(key);
            if(it == map_.end())
                        return -1;
            auto val = it->second->second;
            lru_.erase(it->second);
            add_to_lru(key, val);
            return val;
        }
    
        // if the key is present then update the key
        // and put entry in the back of LRU
        // if new value the put in the back of LRU
        // if capacity reached remove from the front and then add
        void 
        set(int key, int val){
            auto it = map_.find(key);
            if(it == map_.end()){
                if(lru_.size() == cap_){
                    evict_lru();
                } 
                add_to_lru(key, val);
                
            } else {
                auto it  = map_[key];
                lru_.erase(it);
                add_to_lru(key, val);
            }
        }
    
};

#endif

vector <int> 
implement_LRU_cache(int capacity, vector <int> query_type, vector <int> key, vector <int> value) {
	int n = query_type.size();
	// Setup cache. 
	Lru* cache = new Lru(capacity);
    
	vector<int> ans;
	for (int i = 0; i < n; i++)
	{
		if (query_type[i] == 0)
		{
			ans.push_back(cache->get(key[i]));
		}
		else
		{
			cache->set(key[i], value[i]);
		}
	}
	return ans;
}
