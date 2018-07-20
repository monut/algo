#include <iostream>
#include <vector>
#include <queue>

// Merge K sorted arrays size N each
using namespace std;


template<typename T>
ostream&
operator<<(ostream& os, vector<T> v) {
    for( auto val : v){
        os << val << " ";
    }
    return os;
}

/*
 * Complete the function below.
 */
vector <int> mergeArrays(vector < vector<int> > arr) {
   auto K = arr.size();
    auto N = arr[0].size();
    vector<int> rslt;
    priority_queue<pair<int, pair<int, int> > > pq;

    for(auto i = 0; i < K; i++) {
        pq.emplace(arr[i][0], make_pair( i, 0));
    }
    auto total = K * N;
    auto cnt = K;
    auto nxt_q = 0;
    auto nxt_idx = 0;
    while(!pq.empty() &&  cnt < total){
        cnt++;
        auto elem = pq.top();
        pq.pop();
        rslt.push_back(elem.first);
        nxt_q = elem.second.first;
        nxt_idx = elem.second.second + 1;
        if(nxt_idx > K) {
            continue;
        }
        pq.emplace(arr[nxt_q][nxt_idx],
                    make_pair(nxt_q, nxt_idx));
    }
    while(!pq.empty()){
        auto elem = pq.top();
        rslt.push_back(elem.first);
        pq.pop();
    }
    return rslt;
}


/*
look at all the arrays first element
push the max in the result array
look at the next element in the array which has the max element
compare if its the maximim amont the elemnrts in temp array
if it is max insert in result keep it ( may be tupple of value and index)
if it is not the get the max and go to the Q which had the max
insert in the result
*/

int main()
{

    vector <int> res;
    vector< vector<int> > mat = {{1,3,5,7}, {2,4,6,8}, {0,9,10,11}};
    res = mergeArrays(mat);
    cout << res;
    return 0;
}

