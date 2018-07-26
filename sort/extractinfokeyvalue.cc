
//#include <regex>
/*
    Space : O(n*(MAX_LENGTH(KEYS)+MAX_LENGTH(VALUES)))
    Time : O(n*(MAX_LENGTH(VALUE))
    N * length of the keys as key is string and the length of values as values of string
    hash map of {key => {count, <highest string>}}
    
 */

vector<string> solve(vector<string> arr) {
    unordered_map<string, pair<int, string> > hmap;
   
    for(int i = 0; i < arr.size(); i++){
        string s = arr[i];
        vector<string> tok;
        regex re(" ");
        copy(sregex_token_iterator(s.begin(), s.end(), re, -1), 
                sregex_token_iterator(), back_inserter(tok));
        // find key 
        auto it = hmap.find(tok[0]);
        if(it == hmap.end()){
            hmap[tok[0]] = {1, tok[1]};
        } else {
            int cnt = it->second.first + 1;
            string val = (it->second.second > tok[1])? it->second.second : tok[1];
            hmap[tok[0]] = {cnt, val};
        }
        
    }
    
    vector<string> res;
    for(auto& hp : hmap){
        string s = hp.first + ":" + to_string(hp.second.first) + "," + hp.second.second;
        res.push_back(s);
    }
    return res;
}
/*
Input {"Mark zuck", "Tim cook", "Mark twain"}
Output {"Mark:2,zuck", "Tim:1,cook"}
*/
