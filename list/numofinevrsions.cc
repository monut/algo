// Given an array count the number of inversions in the array
For any index i<j if A[i] > A[j]  => inv
Arr: 2  3 1 
Ind :[0 1 2]
SortinArr:  [2 0 1]
Pos Indx : 0 1 2
A[0] > A[1]  A[1] > A[2] 
BF: O(N^2)


5 4 3 2 1

Idx : 0 1 2 3 4
Sort [<0, 4> <1 3> < 2 2> < 3 1> <4 0>]
Sort[0] = 4 

O(NlogN) 

3 4 5 0 1 2

int
merge(vector<int>& arr,int st, int m, int en) {
        int sz1 = m
        int sz2 = en;
        int cnt = 0;
        int i = st, j = m+1;
        vector<int> res;
        while(i < sz1 && j < sz2){
            if(arr[i] < arr[j]) {
               i++;
                res.push_back(ar[i]);
            } else {
                cnt++; j++;
                res.push_back(arr[j]);
            }  
             
        }
        
        while(i < sz1) {
            res.push_back(arr[i++]);
        }
        while(j < sz2) {
            res.push_back(arr[j++]);
           
        }
        
        for(int k = st; i <= en; k++) {
            
            arr[k] = res[k-st];
        }
        return cnt;
}

void 
mergesort(vector<int> arr, int st, int en, int& cnt){
      if(st >= en) return;
     int m = st + (en-st)/2;
     //mergesort(arr, st, m);
     // mergesort(arr, m+1, en);
     cnt += merge(arr, st, m, en);
}

int main(vector<int> arr){
    int cnt = 0;
     mergsort(arr, 0 , arr.size() -1, cnt);
     cout << cnt;

}
