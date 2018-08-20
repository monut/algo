/*  Given an array with element indicating the max number of steps one
    can take from the position given by index. Find if we can reach the end.
    Indx :      0 1 2 3 4
    Arry:    <  3 3 0 2 0 >
   Max <      0 4 5 5 6 6
   Travers left to right keep the running max and if for any index the max = i 
   then we cannot reach the end
 */
bool arrayadvance(vector<int>& arr){
    int sz = arr.size();
    int max = 0;
    
    for(int i = 0; i < sz; i++) {
        if(i+a[i] > max){
            max = i+a[i];
        } 
        if(max == i) return false;
    }
    return true;
}
