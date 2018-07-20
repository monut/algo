#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

#include "myutils.h"

using namespace std;
/*
 * Complete the function below.
 */
//find top K 

vector <int> topk(vector <int> arr, int k) {

    vector<int> res;
    auto comp = [](int a, int b){return a > b;};
    priority_queue<int, vector<int>, decltype(comp)> pq(comp);
    int arr_sz = arr.size();
    auto cnt = min(k, arr_sz);
    for(auto i = 0; i < cnt; i++) {
        pq.push(arr[i]); 
    }

    if(arr.size() > k) {
        for(auto i = k; i < (arr.size()) ; i++) {
            auto elem = pq.top();
            if(elem < arr[i]) {
                pq.pop();
                pq.push(arr[i]);
            }
        }
    } 
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
