/*
mohrs algo 
1st scan : start scanning the array and keep a count of duplicates
set count to zero if different. If count becomes zero set the new element as maj element
and set cnt to 1;
2nd scan go through to veify if its the majority element
*/
int majelem(vector<int>& arr){
    int cnt = 0;
    int maj = arr[0];
    for(auto val : arr) {
      if(maj == val){
        cnt ++;
      } else {
        cnt--;
      }
      if(cnt == 0){
        // 
        maj = val;
        cnt = 1;
      }
    }
    
    for(auto val : arr) {
        if(val == maj)
          cnt++;
    }
    if(cnt > arr.size()/2)
      retrun maj;
    return -1;
}

