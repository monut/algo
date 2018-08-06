/* 
Given a 7 digit number find all possible leter combinatns based on digit to letter mapping on numeric pad
*/
#include <iostream>
#include <unordered_map>
#inlcude <vector>
#inlcude <string>

using namespace std;


unordered_map <int, string> keypad = { {1, ""}, {2, "abc"}, {3, "def"}, {4,"ghi"}, {5,"jkl"}, {6,"mno"},
  {7, "pqrs"}, {8, "tuv"}, {9, "wxyz"}};
 
unordered_set<string> dict = {"dad", "bad","cattle"}; 

void 
helper(vector<int>& numb, i , string exp, vector<string>& res) {
  if(i == number.length()) {
    // check in dictionary and if found insert in the result
    if(dict.find(exp) != dict.end()){
      res.push_back(exp);
    }
    return;
  }
  // get the string assocaited with the number
  string st = keypad[number[i]];
  for(auto c : st) {
    helper(numb, i+1, exp + c);
  }
 }
 
 int main(){
  vector<string> res;
  vector<int> num1 = {3,2,3};
  vector<int> num2  = {2,2,8,8,5,3};
  string exp;
  helper(num1, 0, exp,res);
  
  for(auto val : res) {
    cout << val << endl;
  }
 
 }


