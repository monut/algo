#include "myutils.h" 
#include <cmath> 

static const unsigned int x = 2;
static const unsigned int p = 31;
unsigned int
polyhash(string s) {
    unsigned int hash = 0;
    
    for(int i = s.length() -1; i >= 0; i--){
            hash = (hash * x + s[i] ) % p;
            // hash = (int)(hash + (c - 'a') * pow(x,i++)) % p;
    }
    return hash;
}

// p_sz = pattern size
vector<unsigned int>
precomphash(string s, int p_sz){
    // initialize to # of substrings in a txt
    vector<unsigned int> H(s.length() - p_sz + 1, 0);
    H[s.length() - p_sz] = polyhash(s.substr(s.length() - p_sz));
    
    unsigned int y = 1;
    for(int i = 0; i < p_sz ; i++){
        y = (y * x) % p;
    }

    for(int i = s.length()- p_sz - 1; i >= 0; i--){
        H[i] = (x * H[i+1] + s[i]
                   - (s[i + p_sz]*y)%p) % p;
        if(H[i] < 0)
            H[i] = H[i] + p;
    }
    return H;
}

vector<int>
rabinkarp(string s, string p){

    vector<int> rslt;
    unsigned int phash = polyhash(p);
    vector<unsigned int> h = precomphash(s, p.length());
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



}
