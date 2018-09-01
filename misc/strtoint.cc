#include <iostream>
#include <sstream>
#include <ctype.h>
using namespace std;

int main() {
    string s = "1234";
    cout <<  stoi(s) << endl; 

    string s1 = "122";
    // id s1 has non digit number then this will 
    // return 0
    stringstream ss(s1); 
    int x;
    ss >> x;
    cout << x << endl;
}
/*
    given a string find first contiguous integers 
 */
#include <iostream>
#include <string>
using namespace std;

// To execute C++, please define "int main()"


int findint(string str){
    int idx = -1;
    
    int i = 0;
    for(; i < str.length(); i++){
        if(str[i] == '-' || str[i] == '+' || isdigit(str[i])) {
           if(idx ==  -1){ 
               idx = i; 
           }
           continue;
        }
        if(idx != -1){
           if (i - idx == 1){
                if(str[idx] == '-' || str[idx] == '+'){
                    idx = -1; // reset 
                    continue;
                }
           }    
           break;
        }   
    }
    if(idx == -1) return 0;
   
    int sign = 1;
    if(str.substr(idx,1) == "-"){
            sign = -1;
            idx++;
    }
    
    if(str.substr(idx,1) == "+"){
            idx++;
            sign = 1;
    }
    return sign * stoi(str.substr(idx, i - idx));
}
int main() {
    // string st("abc23");
    string st("-abc+23");
    cout << findint(st);
        
}
