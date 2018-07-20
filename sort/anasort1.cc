/*
 * Find the anagrams in a list of srings
 * letters. case sensitive
 */
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

ostream& 
operator<<(ostream& os, vector<string>& v) {
    for(auto val : v) {
        os << val << " ";
    }
    return os;
}

map<string, vector<string>> myresult(vector<string>& v);
int 
main(){
    vector<string> vec = {"stop", "post", "got", "top", "shot", "hots", "tosh"};
    auto rslt = myresult(vec);    
    // ?? write a generic map container printer
    if(!rslt.empty()){
        for(auto pr : rslt) {
            cout << rslt[pr.first];
            cout << endl;
        }
    } else {
        cout << "empty resut set" << endl;
    }
}

map<string, vector<string>>
myresult(vector<string>& v) {
    map<string, vector<string>> m;
    
    for( auto st : v) {
        // need to make a copy of the original 
        // string
        auto sst = st;
        sort(sst.begin(), sst.end());
        auto it = m.find(sst);
        if(it != m.end()){
            it->second.push_back(st);
        } else {
            m[sst] = {st};  
        } 
    }
    return m;
}
