#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <fstream>

#define all(c) c.begin(),c.end()
using namespace std;

template<typename T>
ostream & 
operator<<(ostream &os, const vector<T>& v) {
    for(auto val : v) {
        cout << val <<  " ";
    }
}

template<typename T>
ostream & 
operator<<(ostream &os, set<T>& v) {
    for(auto val : v) {
        cout << val <<  " ";
    }
}

template<typename T1, typename T2>
ostream & 
operator<<(ostream &os, map<T1, T2>& m) {
    for(auto pr : m) {
        cout << "Key:" << pr.first << " "
            << "Value :" << m[pr.first] << endl; 
    }
}

template <typename T>
ostream& 
operator<<(ostream& os, const pair<T, T> pr){
    os << "first: " << pr.first << endl;
    os << "second: " << pr.second << endl;
    return os;
} 
