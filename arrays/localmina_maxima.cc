/* 
 Do binary search for midddle.  
 if arr[m] < arr[m-1] the go left 
 ifarr[m+1] < arr[m] then go right 
 */ 

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int findlocalmin(vector<int> arr, int st, int en){
   
   int m = st + (en-st)/2; 
    
  if((m == 0 || arr[m-1] > arr[m]) 
        && (m == arr.size()-1 || arr[m] < arr[m+1]))  {
        return m;    
  } else if(m > 0 && arr[m-1] < arr[m]){
    return findlocalmin(arr, st, m-1);    
  }
    
   return (findlocalmin(arr,m+1, en));
    
    
      
}

int findlocalmaxima(vector<int> arr, int st, int en){
   
   int m = st + (en-st)/2; 
    
  if((m == 0 || arr[m-1] < arr[m]) 
        && (m == arr.size()-1 || arr[m] > arr[m+1]))  {
        return m;    
  } else if(m > 0 && arr[m-1] > arr[m]){
    return findlocalmin(arr, st, m-1);    
  }
    
   return (findlocalmin(arr,m+1, en));
 }
 
// To execute C++, please define "int main()"
int main() {
    vector<int> v = {7, 4, 2, 4, 9};
    cout <<   " Local MIn " <<  findlocalmin(v, 0, v.size() -1);
}
