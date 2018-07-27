/*
  prod[j] = product of all numbers in array but for jth element
  Create left product array 
  loop from 1 keeping the product 
  loop from right keeping the product of elements in the right
  then scan through each to get the product
  Kind of memoization 
 */
vector<int> 
getProductArray(vector<int> nums) {
    int sz = nums.size();
    vector<int> lprod(sz,1);
    vector<int> rprod(sz,1);
    
    for(int i = 1; i < sz; i++){
        lprod[i] = lprod[i-1] * nums[i-1];
    }
    
    for(int i = sz - 2; i >= 0; i--){
        rprod[i] = rprod[i+1] * nums[i+1];
    }
    
    for(int i = 0; i < sz; i++){
        nums[i] = lprod[i]*rprod[i];
    }
    return nums;
}
