// maximum subsequnece of K elements

int maxsumk(vector<int> arr, int k) {
  int sz = arr.size();
  int sum = 0;
  int maxs = 0; int d = k;
  for(int i = 0; i < k; i++) sum +=arr[i];
  cout << " sum " << sum;
  for(int i = k; i < sz; i++) {
    sum += arr[i];
    if(sum > maxs) {maxs = sum; d++;};
  cout << " sum " << sum;
    int y = sum;
    int idx = -1;
    while(d > k){
        cout << " i = " << i << " d " << d;
        cout << " arr " << arr[i-d+1];
       y  = y - arr[i-d+1];
       cout << " y" << y << " maxs " << maxs << endl;
      if(y > maxs){
          maxs = y; d--; idx = d;}
      else {
        d--;
      }
    }
      cout << "idx " << idx << endl;
      cout << " maxs " << maxs << endl;
    if(idx != -1) d = idx;
    
  }
    return maxs;
}
int main() {
    vector<int> v = {-1,2,3,4,-7};
    cout << maxsumk(v, 3) << endl;
}
