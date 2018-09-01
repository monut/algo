/*
  loop i ->  0 to n-1
  loop j -> i+1 to n-1
    look in hashmap if k-sum is there in the map
    if it is threre then check that is formed by different index 
    if formed by same indexes then skip that. Insert the sum and indexexs.
 */
 
 #include <iostream>
using namespace std;

#include <vector>
#include <unordered_map>

bool find4sum(vector<int>& arr, int k){
    unordered_map<int, vector<pair<size_t, size_t> > > map_;
    
    for(size_t i = 0; i < arr.size() -1; i++) {
       for(size_t j = i+1; j < arr.size()-1; j++){
           int sum = arr[i] + arr[j];
           if(map_.find(k-sum)!= map_.end()){
               auto elem = map_.find(k-sum);
               auto vec = elem->second;
               
               for(auto val : vec){
                   if(val.first != i && val.first != j
                        && val.second != i && val.second != j)
                       return true;
               }
           }  
           map_[sum].emplace_back(i,j);
       } 
    }
    return false;
}

// To execute C++, please define "int main()"
int main() {
       vector<int> arr = {1, 5, 1, 0, 6, 0}; 
       bool bl = find4sum(arr,7);
       if(bl){
           cout << " Found " ;
       }
}
