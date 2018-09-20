#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// To execute C++, please define "int main()"


int main() {
    string str("bat cat");
    reverse(str.begin(), str.end());
    cout << str << endl;
     
    auto idx = str.find(" ");
    size_t st = 0;
    while(idx != string::npos){
       reverse(str.begin()+ st, str.begin()+idx); 
       st = idx +1;
       idx = str.find(" ", st);
       
    }
    if( idx < str.length() -1){
        reverse(str.begin() + st, str.end());
    }
    cout << str;
}
