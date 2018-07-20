#include "myutils.h"
/*
 * Complete the function below.
 */

class TrieNode {
public:
    unordered_map<char, TrieNode * > children;
    bool isend;
};

void 
inserttrie( TrieNode *root, string str){
    TrieNode *node = root;
    for(auto c : str){
        if(node->children[c] == nullptr){
            node->children[c] = new TrieNode();
        }
        node = node->children[c];
    }
    node->isend = true;
}

TrieNode*
build_trie(string str){
    TrieNode *root = new TrieNode();
    int len = str.length();
    // suffixs for "abcd" => { abcd, bcd, cd, d}
    // should inserted in that order
    auto i = 0;
    while(i < len){
        inserttrie(root, str.substr(i));
        i++;
    }
    return root;
}

void trie_traverse(TrieNode *root, string exp, vector<string>& res){
    if(root == nullptr){
        return;
    }
    if(root->children.size() > 1 || (root->isend == true && root->children.size() != 0)){
        res.push_back(exp);
    }

    for( auto c : root->children) {
        trie_traverse(c.second, exp + c.first,  res);
    }
}

string LRS(string iString) {
    TrieNode *root = build_trie(iString);
    vector<string> res;
    string exp;
    trie_traverse(root, exp, res);
    return *max_element(res.begin(), res.end(),
                []( const string& a, const string& b)
                { return a.size() < b.size();});
}


int main(){
    ofstream fout(getenv("OUTPUT_PATH"));
    string res;
    string _iString;
    getline(cin, _iString);
    
    res = LRS(_iString);
    fout << res << endl;
    
    fout.close();
    return 0;
}
