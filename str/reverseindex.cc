/*
 * Complete the find_positions_of_words_in_text function below.
 */

// read from a file and pass also the index of the word and add position to the list of trie node
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isword;
    vector<int> idxs;
    TrieNode():isword(false){};
};

void insertTrie(TrieNode *root, string& name, int idx){
    TrieNode *nd = root;
    for(auto c : name){
        if(nd->children.find(c) == nd->children.end()){
            nd->children[c] = new TrieNode();
        }
        nd = nd->children[c];
    }
    if(!nd->isword){
        nd->isword = true;
    }
    nd->idxs.push_back(idx);
} 
// or vector<pair<string, idx_in_file> > and in that
// case we need to just supply idx value instead of
// computing it.

TrieNode *buildTrie(vector<string>& words){
    int idx = 0;
  
    TrieNode *root = new TrieNode();
    for(auto name : words){
          cout << "inserting " << name << endl;
        insertTrie(root, name, idx);
        idx += name.length();
    }
    return root;
}



void findword(string& word, TrieNode *root, int pos, vector<int>& res){
    cout << "pos " << pos << endl;
    if(pos == word.length() || !root)
        return;
    auto it = root->children.find(word[pos]);
    if(it == root->children.end())
        return;
    TrieNode *nd = it->second;
    if(nd->isword && word.length() -1 == pos){
        cout << " found the word" << endl;
        res = nd->idxs; return;
    } 
    
    findword(word, nd, ++pos, res);
 }

vector<vector<int>> find_positions_of_words_in_text(string text, vector<string> words) {
    /*
     * Write your code here.
     */
    // break text into vector of string and insert in trie
    vector<string> dict = {"world", "cat", "rat", "rot", "wore", "world"};
    // vector<string> wrds = {"world"}
    string wrd("cat");
    // create trie
    TrieNode *root = buildTrie(dict);
    vector<int> res;
    findword(wrd, root, 0, res);
    
    for(auto val : res){
        cout << val <<  " ";
    }
    cout << endl;
    return {{0}};
}

