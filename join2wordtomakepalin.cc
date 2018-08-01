/*
    Build a hash map with revers words. The search each word.
    For each word seach for subsrting  of 1 to str.length(). starting 
    from index 0. If  partial substring is found then check if the remaning 
    string is palindrome or not. 
 */

bool is_palindrome(string st){
    int i = 0;
    int j = st.length() -1;
    while(i < j){
        if(st[i] != st[j])
            return false;
    }
    return true;
    
}

bool helper(const vector<string>& words){
    // reverse map
    unordered_map<string, bool> rmap;
    
    for(auto wrd : words){
        reverse(wrd.begin(), wrd.end());
        rmap[wrd] = true;
    }
    
    // O(N*k^2) -- N words and K substrings K to compare with the map keys which 
    // are strings too.
    for(auto wrd : words){
        for(int i = 1; i <= wrd.length(); i++){
            string s = wrd.substr(0, i);
            if(rmap.find(s) != rmap.end()){
                if(i == wrd.length()) {
                    cout << "Word " << wrd;
                    return true;
                } else {
                    return is_palindrome(s.substr(i-1, wrd.length() - i));
                }
            }
        }
        
    }
    return false;
}
vector<string> join_words_to_make_a_palindrome(vector<string> words) {
    bool bl = helper(words);
    if(bl) {
        cout << " Found ";
    } else{
        cout << "Not Found";
    }
            
    return {"ok"};
}


#if 0
class TrieNode {
public:
    unordered_map<char, TrieNode *> children;
    int index = -1;
    vector<int> lst;
};

bool 
is_palindrome(string word, int l, int r){
    while(l < r){
        if(word[l++] != word[r--])
            return false;
    }
    return true;
}

void
insert(TrieNode *root, string word, int indx){
    TrieNode *node = root;
    // go from end to start of word to inset in revers order
    for(int i = word.length() - 1 ; i >= 0; i--){
        char c = word[i];
        cout << " i = " << i;
        if(node->children[c] == nullptr){
            // node doesn't exist need to add one here
            node->children[c] = new TrieNode();
        }
        if(is_palindrome(word,0,i)){
            node->lst.push_back(indx);
        }
        node = node->children[c];
    }
    cout << "+++++++++++++++"  << endl;
    node->index = indx;
    node->lst.push_back(indx);
}

TrieNode*
build_reversetrie(vector<string> words){
    TrieNode *root = new TrieNode();
    int i = 0;
    for(string word : words){
        insert(root, word, i++);
        cout << " adding word :" << word << endl;
    }
    return root;
}

// res should return list of pairs which have index pair
void
searchtrie(string word, TrieNode *root, int indx, vector<pair<int, int> >& res){
    TrieNode *node = root;
    cout << "Looking for Word" << word << endl;
    auto j = -1;
    for(auto c : word){
        j++;
        cout << " char :" << c;
        // case where word is larger the word in the trie match "aaaa" and trie is "a"
        if(node->index >= 0 && node->index != indx && is_palindrome(word, j, word.length() -1)){
            cout << " inserting index " <<  indx << " node->index " << node->index;
            res.emplace_back(indx, node->index);
        }
        node = node->children[c];
        
        if(node == nullptr){ return;}
    }
    
    for(auto val : node->lst){
        if(val == indx)
            continue;
         // cout << "Inserting from List" << endl;
         // cout << "val " << val << " indx : " << indx << endl;
        res.emplace_back(indx, val);
    }

}
vector<string> join_words_to_make_a_palindrome(vector<string> words) {
    /*
     * Write your code here.
     */
     TrieNode *root = build_reversetrie(words);
     vector< pair<int, int> > res;
     int i = 0;
     for(auto word : words){
        searchtrie(word, root, i++, res);
     }
     
     vector<string> vec;
     
     for(auto indx_pair : res){
        vec.push_back(words[indx_pair.first] + words[indx_pair.second]);
     }
     return vec;
}
#endif
