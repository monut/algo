#include <iostream>
#include <vector>
#include <queue>

using namespace std;

using pp = pair<int, pair<int, int> >;
pair<int, int> findminrange(const vector<vector<int> >& arr){
   int k = arr.size();
   auto  comp = [](pp a, pp b){return a.first > b.first;};
   
   priority_queue<pp, vector<pp>, decltype(comp)> pq(comp);
  
   int minval = numeric_limits<int>::max(); 
   int maxval = numeric_limits<int>::min(); 
    
   for(int i = 0; i < k; i++) {
        if(arr[i][0] > maxval) maxval = arr[i][0];
        pq.emplace(arr[i][0], pair<int, int>(i, 0)); 
   }
   minval = pq.top().first;
   
   int curmax = 0,  curmin = 0; 
   while(!pq.empty()){
       auto elem = pq.top(); pq.pop();
       int n_q = elem.second.first;
       int n_i = elem.second.second + 1;
       if(n_i >= arr[n_q].size()){break;}
       if(arr[n_q][n_i] > maxval) maxval = arr[n_q][n_i];
       pq.emplace(arr[n_q][n_i], pair<int, int> (n_q, n_i));
       if(arr[n_q][n_i] > maxval)
            curmax = arr[n_q][n_i] ;
       else 
           curmax = maxval;
       curmin = pq.top().first;
       if(maxval - minval > curmax - curmin ||
            maxval - minval == curmax - curmin && curmin < minval){
           minval = curmin; maxval = curmax; 
       }
   }
   
    
   return {minval, maxval};
}
// To execute C++, please define "int main()"
int main() {
    vector<vector<int> > vec = {
        {4,10,15,24,26}, {0,9,12,20}, {5,18,22,30}};
    
    auto val = findminrange(vec);
    
    cout << val.first << " ";
    cout << val.second;
}
