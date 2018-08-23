
/*
 * Megre sort is stable sort for duplicates.
 */
void mymerge(vector<int>& ar, int st, int m,  int en) {
    int i = st;
    int j = m+1;
    vector<int> res;
    while(i <= m && j <= en) {
        if(ar[i] <= ar[j]){ // This ensures that it is stable
            res.push_back(ar[i++]);
        } else {
            res.push_back(ar[j++]);
        }
    }
    while(i <= m){
        res.push_back(ar[i++]);
    }
    
    while(j <= en){
        res.push_back(ar[j++]);
    }
    for(int idx = st; idx <= en; idx++){
        ar[idx] = res[idx-st];
    }
}
void helper(vector<int>& intArr, int st, int en){
    if(st >= en) return;
    int mid = st + (en - st)/2;
    helper(intArr, st, mid);
    helper(intArr, mid+1, en);
    mymerge(intArr, st, mid, en);
}
vector <int> MergeSort(vector <int> intArr) {
    helper(intArr, 0, intArr.size() - 1);
    return intArr;
}
