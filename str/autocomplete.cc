/*
  wa2 matched {water, wafer, washington} wa + 2 or more characters.
 */

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct TNode {
    unordered_map<char, TNode *> chlds;
    bool isword;
    TNode():isword(false){};
};

void
insertTrie(TNode *nd, string str){
    
    for(auto c : str){
        if(nd->chlds.find(c) == nd->chlds.end()){
            nd->chlds[c] = new TNode();
        }
        nd = nd->chlds[c];
    }
    nd->isword = true;
}

TNode *bldtrie(vector<string>& vec){
    
    TNode *root = new TNode();
    
    for(auto str : vec){
        insertTrie(root, str);
    }
    
    return root;
}
void
bfs(TNode *root, string exp,vector<string>& res, int cnt){
    if(!root) return;
   
    if(root->isword && cnt < 0){
        res.push_back(exp);
    }
    
    for(auto elem : root->chlds){
        bfs(elem.second, exp + elem.first,res, cnt--);
    }
}

void helper(TNode *root, string str,int pos, string exp,vector<string>& res){
    if(!root || pos >= (int)str.size()) return;
    
    char c = str[pos];
    int cnt = 0;
    if(isdigit(c)){
        cnt = c;
        // follow alt path 
        bfs(root, exp, res,cnt);
        return;
    }
    
    auto it = root->chlds.find(c);
    if(it == root->chlds.end()){
        return;
    }
   
    TNode *nd = it->second;
    helper(nd, str, pos+1, exp + c, res);
 
    
}
// To execute C++, please define "int main()"
int main() {
    vector<string> dict = {"water", "wafer", "gelatin"};
    // crete Trie from dicionary
    TNode *root = bldtrie(dict);
    string exp;
    string str("wa2");
    vector<string> res;
    helper(root, str, 0, exp, res);
}

