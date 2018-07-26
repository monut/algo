#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include "myutils.h"

using namespace std;

/*
    nCr = n^3 can be done n^2 by keeping sum of elements seen 
    in a sset
    loop(i:0 to sz-1)
    loop(j:i+1 to sz)
    if negative sum for two elements is found then good else
    add the element in the set
 */


// if hashing is allowed
vector<string> 
findZeroSum1(vector<int> arr) {
    int sz = arr.size();
    unordered_set<int> ss;
    
    for(int i = 0; i < sz; i++){
        ss.insert(arr[i]);
    }
    
    vector<string> res;
    
    for(int i = 0; i < sz - 1; i++){
        for(int j = i+1; j < sz; j++){
            int sum = -1 *(arr[i] + arr[j]);
            if(ss.find(sum) != ss.end()){
                string rs = to_string(arr[i]) + "," + to_string(arr[j]) + "," + to_string(sum);   
                res.push_back(rs);
            } 
            
        }
    }
    return res;
}

// hash table is not allowed
/*
    sort the array
    loop (all elements)
    check elements from st and end and if arr[i] + el[start] + arr[end] is zero
    if not increment start  is sum is > 0 else decrement end;
    O(NlogN) for sort and O(N^2) for going thriugh
    can be used for match any other sum, just replace 0 with that sum
*/
vector<string> 
findZeroSum(vector<int> arr) {
    
    vector<string> res;
    sort(arr.begin(), arr.end());
    int n = arr.size();
    for(int i = 0; i < n - 2; i++){
        int a = arr[i];
        int st = i+1;
        int en = n - 1;
        while(st < en){
            int b = arr[st];
            int c = arr[en];
            int sum = a + b + c;
            if(sum == 0){
                string s = to_string(a) + "," + to_string(b) + "," + to_string(c);
                // add only if triplet not found
                if(find(res.begin(), res.end(), s) == res.end()){
                    res.push_back(s); // can use set to ensure no duplicates
                }
                // continue search
                // if b is same we have one more triplet
                if(b == arr[st+1]){
                    st++;
                } else {
                    en--;
                }
            } else if( sum > 0){
                en--;
            } else {
                st++;
            }
        }
    }
    return res;
}


int 
main() {

    // vector<int> v{10, -6, -4, };
    // vector<int> v{-2, 2, 0, -2, 2};
    vector<int> v{10, -6, 3, -4, 1};
    vector<string> s = findZeroSum(v);
    cout << s;
}
