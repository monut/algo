/*
 if st == ent return the arr[st]. If arr[m-1] > arr[m+1] and arr[m] < arr[m-1] then arr[m] is smallest.
 if middle element is less than end element then smallest will lie on the left else on the right. 
 Return arr[0] if the array is sorted
 */

int findMinimum(vector < int > arr) {
    int st = 0;
    int en = arr.size() - 1;
   
    while(st <= en){
        if(st == en)
            return arr[st];
        int m = st+ (en - st)/2;
        if(arr[m-1] > arr[m+1] && arr[m] < arr[m-1])
             return arr[m];
        if(arr[m] < arr[en]) {
            // search in left half for smaller number
            en = m - 1;
        } else {
            // serach in right half
            st = m+1;
        }
    }
    // sorted array so return the first element
    return arr[0];
}
