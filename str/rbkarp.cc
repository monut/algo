#include "myutils.h"
#include <cmath>

static const int x = 2;
static const int p = 31;
int
polyhash(string s) {
    int hash = 0;
    int i = 0;
    for( auto c : s) {
        hash = (int)(hash + (c - 'a') * pow(x,i++)) % p;
    }
    return hash;
}

// p_sz = pattern size
vector<int>
precomphash(string s, int p_sz){
    // initialize to # of substrings in a txt
    vector<int> H(s.length() - p_sz + 1, 0); 
    H[s.length() - p_sz] = polyhash(s.substr(s.length() - p_sz));

    for(int i = s.length()- p_sz - 1; i >= 0; i--){
        H[i] = (int)(x * H[i+1] + (s[i] - 'a')
                   - (s[i + p_sz] - 'a')*((int)pow(x, p_sz)% p)) % p;
        if(H[i] < 0)
            H[i] = H[i] + p;
    }
    return H;
}

vector<int> 
rabinkarp(string s, string p){

    vector<int> rslt;
    int phash = polyhash(p);
    vector<int> h = precomphash(s, p.length());
    for(int i = 0; i < s.length() - p.length() + 1; i++){
        if(phash != h[i])
            continue;
        if(s.substr(i, p.length()) == p){
            rslt.push_back(i);
        }
    }

    return rslt;
}

int 
main() {
    string s;
    string p;
    cout << "string:";
    cin >> s;
    cout << endl;
    cout << "patern:";
    cin >> p;
    cout << endl;
    vector<int> res = rabinkarp(s, p);
    cout << res;
    cout << polyhash(s) << endl; 
}
