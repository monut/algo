// recursively find if the given string can be broken in to words in the dictionary
bool helper(string strWord, vector <string >& strDict, vector<string>& res){
if(strWord.size() == 0)
return true;
for(auto i = 1; i <= strWord.length(); i++){
auto it = find(strDict.begin(), strDict.end(), strWord.substr(0,i));
// the first half should be in dictionary and recursvely find if second half
// is in the disctionaty
if(it != strDict.end() && helper(strWord.substr(i, strWord.length() - i), strDict, res)) {
res.push_back(strWord.substr(0,i));
return true;
}
}
return false;
}
vector< vector<string> >
helperdp(string strWord, vector < string > strDict){
size_t sz = strWord.size();
//if(sz == 0) return true;
vector< vector<string> > wb(sz+1, vector<string>());
for(int i = 1; i <= sz; i++){
//if(wb[i].empty() &&
if(find(strDict.begin(), strDict.end(), strWord.substr(0, i)) != strDict.end()){
wb[i].push_back(strWord.substr(0,i));
}
//}
if(!wb[i].empty()){
// go thtough i+1 to size of the reamining string
for(auto j = i+1; j <= sz; j++){
//if(wb[j].empty() &&
if(find(strDict.begin(), strDict.end(), strWord.substr(i, j-i)) != strDict.end()){
wb[j].push_back(strWord.substr(i, j-i));
}
}
}
}
return wb;
}

void
dfs(vector< vector<string> > dp, vector<string>& res, string path, int pos) {
if(pos == 0){
res.push_back(path) ;
}
for(auto st : dp[pos]){
// create a new string by appending what was passed and
// one at that index.
string comb = st +" " + path;
dfs(dp, res, comb, pos-st.length());

}
}
vector < string > wordBreak(string strWord, vector < string > strDict) {
vector< vector<string> > dp;
vector<string> res;
dp = helperdp(strWord,strDict);
dfs(dp, res, "", strWord.length());
return res;
}
