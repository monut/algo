#include <iostream>
#include <string>
using namespace std;
// O(logN)  do binary search
int main()
{
    int x = 9;
    if(x == 0 || x == 1)
        return 1;
    int ans = 1;
    int start = 1;
    int end = x;
    while(start < end ) {
        int mid = (end+start)/2;
        if(mid * mid == x)
            return mid;
        if(mid * mid < x)
        { ans = mid; start = mid + 1;
        } else {
            end = mid -1;
        }
    }
    cout << ans;
    
}
