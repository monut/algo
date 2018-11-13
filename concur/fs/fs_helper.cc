#include <iostream>
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
#include <thread>
#include <mutex>
#include <condition_variable>


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
