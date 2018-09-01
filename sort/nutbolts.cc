#include <iostream>
#include <vector>
#include <algorithm>

/*
quicksort. Chose value as pivot from nuts and partition bolt on that pivot. 
The parition will retunr the pi for bolt. Now choose the bolt[pi] as pivot 
and partition the nuts on that pivot.
*/
#include "myutils.h"
// max case and min case
using namespace std;

int partition(vector<int>& v, int pvt, int lft , int rt);
void
matchit(vector<int>& nuts, vector<int>& bolts, int lft, int rt); 

int
main() {
vector<int> nuts = {9, 2, 8, 5,3,4};
vector<int> bolts = {5, 8, 3, 4, 2, 9};

cout << "Before Nuts " << nuts ;
cout << endl;
cout << "Before Bolts " << bolts ;
cout << endl;

matchit(nuts, bolts,0, nuts.size() - 1);

cout << "After Nuts " << nuts ;
cout << endl;
cout << "After Bolts " << bolts ;
cout << endl;
}

void
matchit(vector<int>& nuts, vector<int>& bolts, int lft, int rt) {
    if(lft < rt) {
        int pvt = partition(nuts, bolts[rt], lft, rt);
        partition(bolts,nuts[pvt], lft, rt); 
        matchit(nuts, bolts, lft, pvt -1);
        matchit(nuts, bolts, pvt+1, rt);
    }
}


int
partition(vector<int>& v, int pvt, int lft , int rt)
{
    int j = lft;
    for(int i = lft; i < rt; i++) {
        if(v[i] < pvt){
            swap(v[i],v[j]);
            j++;
        } else if(v[i] == pvt) {
            swap(v[i], v[rt]);
            i--;
        }   
    } 
    swap(v[rt], v[j]);
    return j; 
}
