/*
 * Find the anagrams in a list of srings
 * letters. case sensitive
 * frequency map
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

map<vector<int>, vector<string>> myresult(const vector<string>& v);
vector<int> str_frequency(string ss); 

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

map<vector<int>, vector<string> >
myresult(const vector<string>& v) {
    map<vector<int>, vector<string> > m;
    
    for( auto st : v) {
        // need to make a copy of the original 
        // string
        // find frequency graph
        auto freq = str_frequency(st);
        // vector<string> v1 = {st};
        // pair second value indicates if inserted or not 
        // the string vector arg has to constructed explicity
        auto res = m.emplace(freq, vector<string>{st});
        if(!res.second ){
            res.first->second.push_back(st);
        } 
    }
    return m;
}

namespace {
size_t maxsize = 26;
};

vector<int>
str_frequency(string ss) {
    vector<int> freq(maxsize,0);
    for( auto v : ss) {
        freq[v -'a']++;
    } 
    return freq;
}
