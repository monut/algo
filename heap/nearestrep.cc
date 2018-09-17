#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

/*
   store the index and compute the min dist if the same word is found agai. 
   also update the index for the word with new index
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
