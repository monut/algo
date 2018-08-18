/*

Given an array of n elements, where each element is at most k away from its position in a sorted array, devise an algorithm that fully sorts the array.

       0 1 2
intput 8 5 3 k = 2
       3 5 8

    2 +- k

pivot = 2 

BF: O(nlogn)
Scan: O(n*k)
    5 3 8


8 4 3 3

    8 5 3
i = 0 look at i + k inex if arr[i+k-1] < arr[i]  3 5 8

i = 0 get the minimum in the next K element
3 5 8
     5 8 7 9 K = 2
     7 8 5 9 <=
     5 7 8 9
     
 PQ: 5 8 Res : 5
 PQ: 7 8 Res : 5 7
 PQ: 7 
 
 
    
PQ: 8 
 5 8 
 4 5 8 
4
 PQ: 5 7 8
 5
 P
 */
 
 vector<int> sortbyK(vector<int> arr, int k){ // [7 8 5 9], 2 
     
     priority_queue<int,vector<int>, decltype(comop)> pq(comp);
     int j = k + 1; // j = 3
     while(j){
         pq.push(arr[--j]); 
     }
     // 5 7 8 
     vector<int> res;
     for(int i = k + 1; i < arr.size(); i++){  // i = . 4
         res.push_back(pq.top()); // Res: 5 
         pq.pop();
         pq.push(arr[i]);// PQ: 7 8 9
     }
     while(!pq.empty()){
         res.push_back(pq.top()); REs :5 7 8 9e
         pq.pop();
     }
         
     return res;
 }
 
