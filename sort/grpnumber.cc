#include <iostream>
#include <vector>
#include <algorithm>

#include "myutils.h"

using namespace std;
/*
 * Complete the function below.
 */
// group event to the left and odd to the right
vector <int> solve(vector <int> arr) {
    auto j = 0;
    // auto temp = arr[j];
    for(auto i = 0; i < arr.size(); i++) {
        if(arr[i] %2== 0) { // even
            swap(arr[i],arr[j]);
            j++;
        }
    }
    return arr;    
}

int main()
{

    vector <int> inp = {1,2,3,4};
    
    vector <int> res = solve(inp); 
    cout << res;
    return 0;
}
