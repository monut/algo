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

long numPhoneNumbers(int startdigit, int phonenumberlength) {
if(startdigit < 0 || startdigit > 9){
return 0;
}
// didgits from 0 to 9 so 10 digits
// 0 numbers with 0 lenght and 1 number for each digit with 1
// phone number length
vector< vector<int> > dp(phonenumberlength + 1, vector<int>(10));
vector< vector<int> > kpad= {{1, 2, 3},
{4, 5, 6},
{7, 8, 9},
{-1, 0,-1}};
for(int i = 0; i < 10; i++){
dp[0][i] = 0;
dp[1][i] = 1;
}
for(int len = 2; len <= phonenumberlength; len++){
for(int digit = 0; digit < 10 ; digit++){
// find all digits which can be reached from "digit" in the kpad
auto pd = positioninkpad(digit, kpad); // assuming the digit is valid
auto i = pd.first;
auto j = pd.second;
bool p1 = valid_position(i+1,j+2);
bool p2 = valid_position(i+1,j-2);
bool p3 = valid_position(i-1,j+2);
bool p4 = valid_position(i-1,j-2);
bool p5 = valid_position(i-2,j+1);
bool p6 = valid_position(i-2, j-1);
bool p7 = valid_position(i+2,j+1);
bool p8 = valid_position(i+2,j-1);
dp[len][digit] = (p1?dp[len-1][kpad[i+1][j+2]]:0)
+(p2?dp[len-1][kpad[i+1][j-2]]:0)
+ (p3?dp[len-1][kpad[i-1][j+2]]:0)
+ (p4?dp[len-1][kpad[i-1][j-2]]:0)
+ (p5?dp[len-1][kpad[i-2][j+1]]:0)
+ (p6?dp[len-1][kpad[i-2][j-1]]:0)
+ (p7?dp[len-1][kpad[i+2][j+1]]:0)
+ (p8?dp[len-1][kpad[i+2][j-1]]:0);
}
}
return dp[phonenumberlength][startdigit];
}
