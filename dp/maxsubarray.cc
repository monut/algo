/*
  find subarray with max sum  in array of +ive and -ive integers
  maintain a running sum and and keep the maximiim 
  if some decreases we start the sum again and preserve the old range
 */
 
 pair<int, int> findmaxsubarray(vector<int> arr){
  int max_sum = 0, max_i = 0, min_i = 0, sum = 0;
  pair<int, int> max_pair = {0,0};
  for(int i = 0; i < arr.size(), i++){
    sum += arr[i];
    if(max_sum < sum) {
        max_i = i;
        max_sum = sum;
    } else {
        max_pair = {min_i, max_i};
        sum = arr[i];
        max_i = min_i = i;
    }
  }
  return max_pair;
}
