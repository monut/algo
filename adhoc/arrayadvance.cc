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
