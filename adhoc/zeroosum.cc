/*
    keeping a running sum. saving index and sum in a map.
    if see the sum again indicates that the sum of the integers from
    index  after the one found in map to the current sum to zero
*/

vector <int> 
sumZero(vector <int> intArr) {
    unordered_map<int, int> mp;
    int sum = 0; 
    int i = 0;
    
    pair<int, int> max = {0, 0};
    vector< vector<int> > res;
    for(auto val : intArr){
        sum +=val;
        
        if(sum == 0){
            vector<int> v;
            copy(intArr.begin(), intArr.begin() + i +1, back_inserter(v));
            res.push_back(v);
            if((max.second - max.first) < i ){
                max = {0, i};
            }
        }
        
        auto it = mp.find(sum);
        if(it != mp.end()){
            // found the sum
            int idx = it->second + 1;
            vector<int> v;
            // begin + idx as idx started from zero. So works out 
            copy(intArr.begin()+idx,intArr.begin()+i+1, back_inserter(v));
            res.push_back(v);
            if((max.second - max.first) < i - idx){
                max = {idx, i};
            }
            
        } else {
            mp[sum] = i;
        }
    
        i++;
    }
    
    for(const auto& vv : res){
        for( auto val : vv){
            cout << val << " ";
        }
        cout << endl;
    }
    cout << "max_indexes from " << max.first << " to " << max.second;
    return {};
}
