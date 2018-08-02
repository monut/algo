/*
 * Longest common substring
 * Suffix tree finds the commonality from the middle where as 
 * Preffix tree from the beginning. But in both cases the data structure is a Trie
 */

struct TrieNode {
    unordered_map<char, TrieNode *> children;
    bool isend;
    TrieNode():isend(false){};
};

void insertTrie(TrieNode *root, string str){
    TrieNode *nd = root;
    
    for(auto c : str){
        if(nd->children.find(c) == nd->children.end())
            nd->children[c] = new TrieNode();
        nd = nd->children[c];
    }
    nd->isend = true;
   
}

TrieNode *buildTrie(string str){
    TrieNode *root = new TrieNode();
    
    // suffixs for "abcd" => { abcd, bcd, cd, d}
    // should inserted in that order
    for(int i = 0;  i < str.length(); i++){
        string s = str.substr(i,str.length()-i);
        insertTrie(root,s);
    }
    return root;
}

void
TrieBFS(TrieNode *nd, string exp, vector<string>& res)
{
    if(nd == nullptr)
        return;
    // need to push if this node has more than - 1 children
    // as that indicates branching
    // or reached the end of one word eg "AAAA" where there
    // is not branching
    
    if(nd->children.size() > 1  || (nd->isend && nd->children.size() != 0) )
        res.push_back(exp); 
    for(auto c : nd->children){
        TrieBFS(c.second, exp + c.first, res);
    }
}
string LRS(string str){
    
    TrieNode *root = buildTrie(str);
    vector<string> res;
    string exp = "";
    TrieBFS(root, exp, res);
    auto it = 
        max_element(res.begin(), res.end(),[](string a, string b){ return a.length() < b.length();});
    
    if(it != res.end())return *it;
    
    return "";
}
