int maxStolenValue(vector < int > arrHouseValues) {
int sz = arrHouseValues.size();
vector<int> dp(sz+2, 0);
for(int i = sz-1; i >= 0; i--){
dp[i] = max(dp[i+1], dp[i+2] + arrHouseValues[i]);
}
return dp[0];
}
