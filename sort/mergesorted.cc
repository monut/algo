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

#include <iostream>
#include <vector>
#include <queue>
/*
 * Complete the function below.
 */
// need to handle ascending case

#if 0
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


class Comp {
    private:
        bool reverse_;
    public:
        Comp(bool reverse = false):reverse_(reverse){};
        bool operator()(pair<int, pair <int, int> > a, pair<int, pair <int, int> > b){
            if(reverse_)
                return a.first > b.first;
            else 
                return a.first < b.first;
        }
};

vector <int> 
mergeArrays(vector < vector<int> > arr) {
    auto N = arr[0].size();  // # of elements in a array
    auto K = arr.size(); // # of arrays
    vector<int> res;
    // find 
    bool minh = ((arr[0][0] < arr[0][1])?true:false); // need min heap in ascending order
    Comp mycomp(minh);
    priority_queue<pair<int, pair <int, int> >, 
                vector<pair<int, pair <int, int> > >, Comp> pq(mycomp);
    // inset the first element from each of the queue 
    // {element, {index of queue, next index in that queue}}
    for(auto i = 0; i < K; i++){
        pq.emplace(arr[i][0], pair<int, int>(i,1));
    }
    int total = N *K; 
    int cnt = 0;
    cout << " While loop";
    while(cnt < total){
        auto val = pq.top();
        res.push_back(val.first); // push element into vector
        pq.pop();
        if(val.second.second < N){
            int q_idx = val.second.first;
            int idx_in_q = val.second.second;
            pq.emplace(arr[q_idx][idx_in_q], pair<int, int> (q_idx, idx_in_q + 1));
        }
        cnt++;
    }
    return res;
}

#endif

vector <int> 
mergeArrays(vector <vector<int> > arr) {
    /*
        Find the order if ascending or descending
        create a priority queue 
        insert the first element from each of the K queue
        {val { number_of_q, index_in_that_q} }
        Pop the top item from pq and get the next element from 
        the Q to which that element belongs. Else go to the next q
     */
    int num_q = arr.size();
    
     
    bool ascend_flag = false;
    if(arr[0][0] > arr[0][1])
            ascend_flag = true;
    using pp = pair<int, pair<int, int> >;
    function<bool(pp, pp)> comp;
    
    if(ascend_flag)
        comp = [](pp a, pp b){ return a.first < b.first;};
    else 
        comp = [](pp a, pp b){ return a.first > b.first;};
        
    priority_queue<pp, vector<pp>, decltype(comp)> pq(comp);
    
    // pushing first elements from all the K queues
    for(int i = 0; i < num_q; i++){
        pq.emplace(arr[i][0], pair<int,int>(i, 0));
    }
    
    vector<int> res;
    while(!pq.empty()){
        auto val = pq.top();
        pq.pop();
        cout << val.first << endl;
        res.push_back(val.first);
        int nxt_q = val.second.first;
        int nxt_q_idx = val.second.second + 1;
        if( nxt_q_idx >= arr[nxt_q].size()) {
            // skip becasue index is more than than elements in array
            continue;
        } else {
            pq.emplace(arr[nxt_q][nxt_q_idx], pair<int, int>(nxt_q, nxt_q_idx));
        }
    }
    return res;
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

