vector<string> findsword(TrieNode *nd, string wrd){
  if(!nd) return;
  for(auto c : wrd){
    auto it = nd->chlds.find(c);
    if(it == nd->chlds.end()) break;
    nd = it->second;
  }
  vector<string> res;
  string exp;
  if(it != nd->chlds.end()){
    dobfs(nd, exp + wrd, res)
  }
}

void dobfs(TrieNode *nd,string exp ,vector<string>& res){
    if(!nd) return;
    if(nd->isword) res.push_back(exp);
    
    for(auto elem : nd->chlds){
      dobfs(elem.second, exp + nd.first, res);
    }
  
}
