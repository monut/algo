#include "myutils.h"
/*
    insert in a min hip the K element
    and in a set
    loop through the elements 
    if top element is less than the new element 
    and is not already in the set then pop the top element 
    and insert it else continue.
 */
vector <int> topK(vector <int> arr, int k) {
    
    if(arr.size() <= k)
        return arr;
    unordered_set<int> myk;
    auto comp = [](int& a, int& b){return a > b;};
    priority_queue<int, vector<int>, decltype(comp)> pq(comp);
    
    int i = 0;
    while(i < k){
        if(myk.find(arr[i]) == myk.end()){
            myk.insert(arr[i]);
            pq.push(arr[i]);
        }
        i++;
    }
    
    while(i < arr.size()){
        if(myk.find(arr[i]) == myk.end() ){
            if(pq.size() < k){
                pq.push(arr[i]);
                myk.insert(arr[i]);
            } else {
            
                if(pq.top() < arr[i]){
                    myk.erase(pq.top());
                    pq.pop();
                    pq.push(arr[i]);
                    myk.insert(arr[i]);
                    
                }
            }
        }
        i++;
    }
    
    vector<int> res;
    while(!pq.empty()){
        res.push_back(pq.top());
        pq.pop();
    }
    return res;
}



int main()
{

    // vector <int> inp = {9, 10, 1,2,3,4, 10};
    // vector <int> inp = {9, 10, 1,2,3,4, 11};
    vector <int> inp = {-2, -1, -4, 0, -2, 4};
    int k ;
    cin >> k;    
    vector <int> res = topk(inp,k); 
    cout << res;
    return 0;
}
