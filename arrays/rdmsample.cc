vector<int> randomsample(vector<int> arr, int k){
   default_random_engine seed((random_device())());
    
   for(int i = 0; i < k; i++){
       int idx = uniform_int_distribution<int>{i, arr.size() -1}(seed);
       swap(arr[i], arr[idx]);
   }
    
   vector<int> rslt;
   copy(arr.begin(), arr.begin()+k, back_inserter(rslt));
    
    return rslt;
    
}
int main() {
  vector<int> v = { 2,10,3,4,5,6,7,8,9};
  vector<int> rs = randomsample(v, 4);
    
   for(int i = 0; i < rs.size(); i++)
       cout << rs[i] << " ";
    
    cout << endl;
}
