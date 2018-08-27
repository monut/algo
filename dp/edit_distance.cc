/*
* Complete the function below.
*/
int min(int x , int y, int z){
return min(min(x, y), z);
}
int helper1(string st1, string st2, int n, int m){
// if the first string exhausts we need to do
// operation for the remaining letter in second
// vice versa
if(n < 0 && m < 0) return 0;
if(n < 0) return m + 1; // account for start from zero
if(m < 0) return n + 1; // account for start from zero
if(st1[n] == st2[m]){
return helper1(st1, st2, n-1 , m-1);
}
return 1 + min(helper1(st1, st2, n-1,m), helper1(st1, st2, n, m-1), helper1(st1, st2, n-1, m
-1));
}
int helper2(string st1, string st2, int n, int m) {
int dp[n+1][m+1];
for(auto i = 0; i <= n; i++){
for(auto j = 0; j <= m; j++){
// first string is empty them option to insert all
if(i == 0) {
dp[i][j] = j;
} else if(j == 0) {
// second string is empty then insert all
dp[i][j] = i;
} else if (st1[i-1] == st2[j-1]) {
dp[i][j] = dp[i-1][j-1];
} else {
dp[i][j] = 1 + + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]);
}
}
}
return dp[n][m];
}
int levenshteinDistance(string strWord1, string strWord2) {
return helper2(strWord1, strWord2, strWord1.length(), strWord2.length());
}
