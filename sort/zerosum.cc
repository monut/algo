#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include "myutils.h"

using namespace std;

vector<string> 
findZeroSum(vector<int> arr) {
    // Write your code here.
    vector<string> res;
    for(int i = 0 ; i < arr.size()-1; i++){
        unordered_map<int, int> sset;
        for(int j = i+1; j < arr.size() ; j++){
            auto sum = -(arr[i] + arr [j]);
            if(sset.find(sum) != sset.end()){
                auto ans = to_string(sum) + ","  + to_string(arr[i]) 
                        + "," +to_string(arr[j]);
                res.push_back(ans);
                arr.erase(find(arr.begin(), arr.end(), sum));
                arr.erase(find(arr.begin(), arr.end(), arr[i]));
                arr.erase(find(arr.begin(), arr.end(), arr[j]));
            } else {
                sset.emplace(arr[j], 1);
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
