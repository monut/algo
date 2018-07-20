#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int
main(){
    string fname = "my_file.txt";
    ifstream rf(fname.c_str());
    string line;
    while(getline(rf,line)){
        // cout << line << endl;
        istringstream iss(line);
        string str;
        while(iss >> str){
            cout << str << endl;
        }
    }
   
    vector<string> vec = {"pig", "wig", "jig", "twig"}; 
    ofstream wf("my_write.txt");
    int cnt = 1;
    for(auto val : vec) {
        wf << val << " "; 
        if(cnt %2 == 0) {
            wf << endl;
            cnt = 0;
        }
        cnt++;
    } 
    
}
