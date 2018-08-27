void makeChange(int C, vector < int > intDenominations) {
int max = C+1;
vector<int> DP(C + 1, max);
vector<int> res;
DP[0] = 0;
for(int amt = 1; amt <= C; amt++){
for(auto di : intDenominations){
if(amt >= di) {
DP[amt] = min(DP[amt], DP[amt - di] + 1);
}
}
}
cout << "Minimum Number of coins to make " << C << "is " << DP[C] <<
endl;
int t = C;
while(t > 0){
for(auto c : intDenominations){
if(DP[t-c] == DP[t] -1){
// add the coin to result
res.push_back(c);
t = t-c;
break;
}
}
}
for(auto val : res){
cout << val << ",";
}
}
