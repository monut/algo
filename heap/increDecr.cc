#include <iostream>
#include <vector>
using namespace std;

/*
    sort increment decrement array
    divide the array into subarrays and the 
    merge these sorted arrays
    travers left to right and split when 
    increaing becomes decreaisng
 */
vector<vector<int> > fs(vector<int>& a){
    enum TYP {
       INCR,
       DECR,
    };
    TYP typ = INCR; 
    int idx = 0;
    vector<vector<int> > res; 
    for(int i = 1; i <= a.size(); i++){
        if(i == a.size() || (a[i-1] >= a[i] && typ == INCR) ||  
                (a[i-1] <= a[i] && typ == DECR)){
           if(typ == INCR){
             res.emplace_back(a.begin()+idx, a.begin()+i); 
           } else {
             res.emplace_back(a.rbegin() + a.size() - i, a.rbegin() + a.size() - idx); 
           }
            idx = i;
            typ = (typ == INCR ? DECR : INCR);
            
        }
    }
    return res;
}

int main() {
    vector<int> vec = {57, 131, 493, 294, 221, 339, 418, 452, 442, 190};
    vector<vector<int> > res = fs(vec);
    
    for(auto vv : res ){
       for(auto val : vv){
           cout << val << " ";
       } 
       cout << endl;
    }
}

/*
57 131 493
221 294
339 418 452
190 442
*/
