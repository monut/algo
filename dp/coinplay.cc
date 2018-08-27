int maxWin(vector < int > intCoins) {
int sz = intCoins.size();
vector<vector<int> > DP(sz, vector<int>(sz, 0));
for(auto dif = 0; dif < sz; ++dif){
for(int i = 0, j = dif; j < sz ;++i, ++j){
int x = (i+2 <= j)? DP[i+2][j] : 0;
int y = (i+1 <= j-1)? DP[i+1][j -1] : 0;
int z = (i <= j-2)? DP[i][j -2] : 0;
DP[i][j] = max(intCoins[i] + min(x,y), intCoins[j] + min(y,z));
}
}
return DP[0][sz -1];
}
int maxWin1(vector < int > v) {
vector<vector<int>> opt(v.size(), vector<int>(v.size(), 0));
for(int i = 0; i < v.size();i++) opt[i][i] = v[i];
for(int s = 1; s < v.size(); s++) {
for(int i = 0; i < v.size()-s; i++) {
int j = i+s;
int p1 = (i < v.size()-2)?opt[i+2][j]:0;
int p2 = (i < v.size()-1 && j > 0)?opt[i+1][j-1]:0;
int p3 = (j > 1)?opt[i][j-2]:0;
opt[i][j] = max(v[i]+min(p1,p2) , v[j]+min(p2,p3));
}
}
return opt[0][v.size()-1;

}
