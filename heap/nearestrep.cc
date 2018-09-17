#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

/*
    sort increment decrement array
    divide the array into subarrays and the 
    merge these sorted arrays
    travers left to right and split when 
    increaing becomes decreaisng
 */
int nearestrep(vector<string>& a){
    unordered_map<string, int> mp;
    int dist = numeric_limits<int>::max();
    
    for(int i = 0; i < a.size(); i++){
        auto it = mp.find(a[i]);
        if(it != mp.end()){
            dist = min(dist, i - it->second);
        }
        mp[a[i]] = i;
    } 
    
    return dist;
}

int main() {
    vector<string> v1 = {"All", "work", "and", "no", "pay", "no", "fun","make", "jack", "no"};
    cout << nearestrep(v1);
}
