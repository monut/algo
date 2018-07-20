#include <regex>

#include "myutils.h"

vector<string> 
solve(vector<string> arr) {
    vector<string> res;
    map<string, vector<string> > mp;
    for( auto src : arr) {
        vector<string> tok;
        regex re(" ");
        copy(sregex_token_iterator(src.begin(), src.end(), re, -1),
            sregex_token_iterator(), back_inserter(tok));  
        vector<string> tmp; 
        tmp.push_back(tok[1]);
        auto it = mp.emplace(tok[0], tmp);
        if(!it.second) { // item already exists
            it.first->second.push_back(tok[1]);
            
        } 
        //cout << tok;
    }

    for( auto p : mp) {
        auto vec = p.second;
        auto cnt = p.second.size();
        sort(vec.rbegin(), vec.rend());
        auto ans = p.first + ":" + to_string(cnt) + ","+vec[0];
        res.push_back(ans);
    }
    
    return res ;
}

int 
main() {

    vector<string> vec{"key1 abcd", "key2 zzz", "key1 hello"};
    vector<string> res;
    res = solve(vec);
    cout << res;
    cout << endl;
}
