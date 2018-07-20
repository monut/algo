#include <iostream>
#include <set>
#include <map>

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>


#define all(c) c.begin(),c.end()
using namespace std;

template<typename T>
ostream & 
operator<<(ostream &os, const vector<T>& v) {
    for(auto val : v) {
        os << val <<  " ";
    }
    return os;
}

template<typename T>
ostream & 
operator<<(ostream &os, set<T>& v) {
    for(auto val : v) {
        os << val <<  " ";
    }
    return os;
}

template<typename T1, typename T2>
ostream & 
operator<<(ostream &os, map<T1, T2>& m) {
    for(auto pr : m) {
        os  << "Key:" << pr.first << " "
            << "Value :" << m[pr.first] << endl; 
    }
    return os;
}
