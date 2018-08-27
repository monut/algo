int countWaysToClimb(vector<int> steps, int n) {
/*
* Write your code here.
*/
int sz = steps.size();
vector<int> dp(n+1, 0);
dp[0] = 1;
for(int i = 1; i <=n; i++){
for(auto s : steps){
if(s <= i){
dp[i] += dp[i-s];
}
}
}
return dp[n];
}
