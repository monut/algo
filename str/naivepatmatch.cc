// Example program
#include <iostream>
#include <string>
#include<vector>

using namespace std;

bool match(string s1, string s2) {
    
    if(s1.length() != s2.length())
        return false;

    for(size_t i = 0; i < s1.length(); i++){
        if(s1[i] != s2[i]) {
                return false;
        }
    }
    return true;
}

template<typename T>
ostream& operator<<(ostream& os, const vector<T>& v){
    for(auto val : v) 
        os << val << " ";
    return os;
}

int main()
{
    string txt = "This is a fox with a box on an ox";
    string pat = "ox";
    vector<size_t> res;
    auto psize = pat.size();
    //auto txtsz = txt.size();
    
    for(size_t i = 0; i <= (txt.size() - pat.size()); i++){
        string p1 = txt.substr(i,psize);
        
        if(match(p1, pat)){
                 
                res.push_back(i);            
        }
    }
    //11 22 31
    cout << res;
}
