#include <iostream>
#include <sstream>
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
