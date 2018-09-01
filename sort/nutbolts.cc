#include <iostream>
#include <vector>
#include <algorithm>

/*
quicksort. Chose value as pivot from nuts and partition bolt on that pivot. 
The parition will retunr the pi for bolt. Now choose the bolt[pi] as pivot 
and partition the nuts on that pivot.
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

template<typename T>
ostream&
operator<<(ostream& os, vector<T> v) {
    for( auto val : v){
        os << val << " ";
    }
    return os;
}

// return the index of the pvt
int 
partition(vector<int>& v, int pvt, int lft, int rt){
    while(lft < rt){
        while(v[lft] < pvt){
            lft++;
        }
        
        while(v[rt] > pvt){
            rt--;
        }
        
        if(lft < rt)
            swap(v[lft], v[rt]);
    }
    return rt; // index of pvt element
}

void matchit(vector<int>& nuts, vector<int>& bolts, int lft, int rt) {
    if(lft > rt)
        return;
    int pvt = nuts[lft];
    int idx = partition(bolts, pvt, lft, rt);
    pvt = bolts[idx];
    partition(nuts, pvt, lft,rt);
    matchit(nuts, bolts, lft, idx-1);
    matchit(nuts, bolts, idx+1, rt);
}

int main() {
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<int> nuts = {9, 2, 8, 5,3,4,10};
    vector<int> bolts = {5, 8, 3, 4, 2, 9, 10}; // No duplicates allowed as per question

    cout << "Before Nuts " << nuts ;
    cout << endl;
    cout << "Before Bolts " << bolts ;
    cout << endl;

    matchit(nuts, bolts,0, nuts.size() - 1);

    cout << "After Nuts " << nuts ;
    cout << endl;
    cout << "After Bolts " << bolts ;
    cout << endl;

    return 0;
}

