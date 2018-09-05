/*
  wa2 matched {water, wafer, washington} wa + 2 or more characters.
 */


#include <iostream>
#include <map>
#include <vector>
#include <string>
using namespace std;

// To execute C++, please define "int main()"
struct TrieNode {
    map<char,TrieNode * > chlds;
    bool isword;
    TrieNode():isword(false){};
};

void insertTrie(TrieNode *nd, string wrd){
    for(auto c : wrd){
        if(nd->chlds.find(c) == nd->chlds.end()){
            nd->chlds[c] = new TrieNode();
        }
        nd = nd->chlds[c];
    }
    nd->isword = true;
}

TrieNode *buildTrie(vector<string>& wrds){
    TrieNode *root = new TrieNode();
    for(auto wrd : wrds){
        insertTrie(root, wrd);
    } 
    return root;
}

void bfs(TrieNode *nd, string exp, int cnt, vector<string>& res){
   if(!nd ){return;}
   if(cnt < 0){return;}
   if(nd->isword && cnt >= 0){
       res.push_back(exp);
   }
    
   for(auto elem : nd->chlds){
      bfs(elem.second, exp + elem.first, cnt-1, res);
   }  
}

void  helper(string wrd, TrieNode *nd, vector<string>& res){
    string exp; 
    for(auto c : wrd){
       if(isdigit(c)){
          int cnt = c;
          bfs(nd, exp, cnt, res);
       }
       auto it = nd->chlds.find(c);
       if(it == nd->chlds.end()){
           break;
       }
       nd = nd->chlds[c];
       exp +=c;
    }
}

int 
main() {
    vector<string> vec = {"water", "wafer", "dog"};    
    TrieNode *root = buildTrie(vec);
    string wrd = "wa3";
    vector<string> res;
    helper(wrd, root, res);
    
    for(auto val : res){
        cout << val << endl;
    }
}




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


