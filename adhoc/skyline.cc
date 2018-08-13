/*
 divide and conqour like merge sort. For singele entry return pairs {{x1, h1}, {x2,0}.
 While merging keep track of height h1 and h2 for two skylines. Add to result the entry 
 from one with less X co-oridnate and the height max(h1,h2). Don't add if prev entry
 has same height.
 */
using vecpr = vector<pair<int, int> >;

vecpr
mergeskyline(vecpr v1, vecpr v2){
    int h1 = 0;
    int h2 = 0;
    vecpr res;
    
    int i = 0;
    int j =0;
    
    while( i < v1.size() && j < v2.size()){
        if(v1[i].first < v2[j].first){
            h1 = v1[i].second;
            int nmax = max(h1,h2);
            res.emplace_back(v1[i].first, nmax);
            i++;
        } else {
            h2 = v2[j].second;
            int nmax = max(h1, h2);
            res.emplace_back(v2[j].first, nmax);
            j++;
        }
    }
    
    while(i < v1.size()){
        res.push_back(v1[i++]);
    }
    while( j < v2.size()){
        res.push_back(v2[j++]);
    }
    return res;
}

vecpr
helper(vector<vector<int> > bld, int st, int en){
    if(st == en){
        return {{bld[st][0], bld[st][1]}, {bld[st][2], 0}};
    }
    
    int mid = st + (en - st)/2;
    vecpr v1 = helper(bld, st, mid);
    vecpr v2 = helper(bld, mid + 1, en);
    vecpr v3 = mergeskyline(v1, v2);
    return v3;
}


vector<vector<int>> find_skyline(vector<vector<int>> buildings) {

    int num_blds = buildings.size();
    // pair { x , height}
    vector<pair<int, int> > res = helper(buildings, 0, num_blds - 1);
     
    for(auto val : res) {
        cout << "{" << val.first << ", " << val.second << "}";
    }
    cout << endl;
    return {{0}};
}

#if 0

vector< pair<int, int> > mergeskyline(vector<pair<int, int> >& sk1, vector<pair<int, int> >& sk2){
    int h1 = 0, h2 = 0;
    vector<pair<int, int> > res;
    
    int i = 0, j = 0;
    // Compare the x co-oridiate and which is less add it to result 
    // alonh with the max of the h1 and h2 height. Setting h1 height 
    // to cuurent value being inserted in the result.
    while(i < sk1.size() && j < sk2.size()){
        if(sk1[i].first < sk2[j].first){
            //cout << " sk1 " << sk1[i].first;
            h1 = sk1[i].second;
            int maxh = max(h1, h2);
            if(!res.empty()){
                auto val = res.back();
                // optimization : don't add the entry if the previous entry
                // is same as previous height.
                if(val.second != maxh)
                    res.emplace_back(sk1[i].first, maxh);
            } else {
                res.emplace_back(sk1[i].first, maxh);
            }
            
            i++;
        } else {
            h2 = sk2[j].second;
            int maxh = max(h1, h2);
            // cout << " sk2 " << sk2[j].first;
            if(!res.empty()){
                auto val = res.back();
                if(val.second != maxh)
                    res.emplace_back(sk2[j].first, maxh);
            } else {
                res.emplace_back(sk2[j].first, maxh);             
            }
            
            j++;
        }
    }
    
    // add remaining elementsin sk1
    while(i < sk1.size()){
        // don't add the entry if the previous entry has the same height
        
       res.emplace_back(sk1[i++]); 
    }
    //add remaining elements in sk2
    while(j < sk2.size()){
        res.emplace_back(sk2[j++]);
    }
    
    return res;
 }

vector<pair<int, int> >  findSkyline(vector< vector<int> >& blds, int lft , int rt) {
    if(lft == rt){
        // for a single building {x1, ht1} and {x2, 0} 
        return {{blds[lft][0], blds[lft][1]}, {blds[lft][2], 0}};
    }
    
    int mid = lft + (rt-lft)/2;
    
    auto sk1 = findSkyline(blds, lft, mid);
    auto sk2 = findSkyline(blds, mid+1, rt);
    // merge the results
    auto res = mergeskyline(sk1, sk2);
    return res;
}


vector<vector<int>> find_skyline(vector<vector<int>> buildings) {
    /*
     * Write your code here.
     */
    int num_blds = buildings.size();
    // pair { x , height}
    vector<pair<int, int> > res = findSkyline(buildings, 0, num_blds - 1);
     
    for(auto val : res) {
        cout << "{" << val.first << ", " << val.second << "}";
    }
    cout << endl;
    return {{0}};
}

#endif

/*
8
3
1 11 5
2 6 7
3 13 9
12 7 16
14 3 25
19 18 22
23 13 29
24 4 28
*/

