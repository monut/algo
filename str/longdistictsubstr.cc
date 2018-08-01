/*
longest substring with atleast 2 ditinct characters.
 eg: eecbebbb ===> "bebbb"
 * start window and window size. manitain a hashmap. add charcters and increment count 
 if already present. If map size becomes greater than 2 them start moving the window to the left
 removing characters and erase if the count becomes zero. Loop untill map size becomes 1.
 Update the {window_start, window_size} before shirning the window.
  
 * Each character is touched at max twice or O(N);
 */

int getLongestSubstringLengthExactly2DistinctChars(string strText) {
    // char => cnt
    unordered_map<char, int> mp;
    cout << strText;
    mp[strText[0]] = 1;
    int w_st = 0, w_sz = 1;
    // window start and window size
    pair<int, int>  res;
    res.first = 0; res.second = 1;
    bool do_shrink = false;
    for(int i = 1; i < strText.length(); i++){
        // if map has only 2 distinct keys I can still 
        // expand if the charachter is found else I 
        // need to shrink from the left
        
        mp[strText[i]]++;
        cout << "w_sz " << w_sz << endl;
        w_sz++;
        
        if(mp.size() > 2){
            // need to shrink the window
            // but first update
            if(res.second < w_sz-1){
                res.first = w_st;
                res.second = w_sz-1;
            }
        }
            
        // shrinkig will set the new window start
        // keep on removing the element from the set while
        // moving the window start to the right
        while(mp.size() > 2){
            mp[strText[w_st]]--;
            if(mp[strText[w_st]] == 0);
                mp.erase(strText[w_st]);
            w_st++; w_sz--;
        }
    }
            
    if(res.second < w_sz){
        res.first = w_st;
        res.second = w_sz;
    }   
        
    cout  << strText.substr(res.first, res.second);
    return res.second;
}
