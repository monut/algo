/*
  Build a Trie for dictionary words
  start from each cell and look in trie as we construct the grid travelling in each direction
  stop the search if there is not match in the trie.
  There are 8 possible adjacent position to a cell. 
  r_mov = {1, -1, 0, 0 , 1, -1, -1, 1};
  c_mov = {0, 0, 1, -1, 1 -1,  1,   -1}
 */

int r_mv[] = {1, -1, 0, 0 , 1, -1, -1, 1};
int c_mv[] = {0, 0, 1, -1, 1 -1,  1,   -1};
vector<int> wlist;

struct TrieNode {
    unordered_map<char, TrieNode *> children;
    int isword;
    TrieNode():isword(-1){};
};

void
insertTrie(string st, TrieNode *root, int idx){
    TrieNode *nd = root;
    for(auto c : st){
        if(nd->children.find(c) == nd->children.end()){
            nd->children[c] = new TrieNode();
        }
        nd = nd->children[c];
    }
    nd->isword = idx;
}

TrieNode *buildTrie(vector<string>& svec){
    TrieNode *root = new TrieNode();
    int i = 0;
    for(auto st : svec){
        insertTrie(st, root, i++);
    }
    return root;
}

bool
isvalid(int r, int c, int rows, int cols)
{
    if(r >0 && r < rows && c > 0 && c < cols)
        return true;
    return false;
}

void
helper(vector<vector < string> >& g, vector< vector<bool>>& used, int r, int c, TrieNode *root){
    if(root->children.find(g[r][0][c]) == root->children.end())
        return;
    TrieNode *nd = root->children[g[r][0][c]];
    if(nd->isword != -1)
        wlist.push_back(nd->isword);
    ///try out the eight options
    for(int i = 0; i < 8; i++){
        int nr = r + r_mv[i];
        int nc = c + c_mv[i];
        if(isvalid(nr,c, g.size(), g[0].size()) && used[nr][nc] != true){
            used[nr][nc] = true;
            helper(g, used, nr, nc, nd);
        }
        used[nr][nc] = false;
    }
}

vector <string > findWords(vector <string> dictionaryList, vector<vector < string > > board) {
    
    int rows = board.size();
    int cols = board[0].size();
    // create Trie
    TrieNode *troot = buildTrie(dictionaryList);
    
    
    // Traverse to find if the word exist or not
    
    
    vector<vector<bool> > used(rows, vector<bool>(cols, false));
    
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++){
            helper(board, used, i, j, troot);
        }
    }
    
    vector<string> rslt;
    for(auto idx : wlist){
        rslt.push_back(dictionaryList[idx]);
    }
    return rslt;
    
}

#if 0 

int r_mov[] = {1, -1, 0, 0 , 1, -1, -1, 1};
int c_mov[] = {0, 0, 1, -1, 1 -1,  1,   -1};
vector<int> wilst = {};

struct TrieNode {
    unordered_map<char, TrieNode *> children;
    int isword; // stores the index of the word in the dictionary
    TrieNode():isword(-1){};
};

void insertTrie(TrieNode *root, string& name, int idx){
    TrieNode *nd = root;
    for(auto c : name){
        if(nd->children.find(c) == nd->children.end()){
            nd->children[c] = new TrieNode();
        }
        nd = nd->children[c]; 
    }
    nd->isword = idx;
}
// build trie from dictionary
TrieNode *buildTrie(vector<string>& dict){
    TrieNode *root = new TrieNode();
    int idx = 0;
    for(auto val : dict){
        insertTrie(root, val, idx++);
    }
    return root;
}


bool
is_valid(int r, int c, int rows, int cols)
{
    if(r >0 && r < rows && c > 0 && c < cols)
        return true;
    return false;
}

void helper(int r, int c, vector<vector<string> >& grid, vector<vector<bool> >& used, TrieNode *root){
    auto it = (root->children).find(grid[r][0][c]);
    //auto it = (root->children).find('a');
    if(it == root->children.end())
        return;
    
    TrieNode *nd = it->second;
    // found the letter in trie so mark it used
    used[r][c] = true;
    
    // found a word insert the index into the list
    if(nd->isword >= 0){
        wilst.push_back(nd->isword);
    }
    
    int n_rows = grid.size();
    int n_cols = grid[0].size();
    // keep traversing the grid
    // and try out all the 8 possible movements
    for(int i = 0; i < 8; i++){
        r+=r_mov[i]; c+=c_mov[i];
        // the cell is valid and has been considered yet
        if(is_valid(r, c, n_rows, n_cols) && !used[r][c] ){
            helper(r, c, grid, used, nd);
        }
        r-=r_mov[i]; c-=c_mov[i]; // reset
    }
    
    //reset the cell status  and back track
    used[r][c] = false;
    
}

vector <string > findWords(vector <string> dictionaryList, vector<vector < string > > board) {
    int rows = board.size();
    int cols = board[0].size();
    vector< vector<bool> >  used(rows, vector<bool>(cols, false));
    
    TrieNode *root = buildTrie(dictionaryList);
    
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            helper(i, j, board, used, root);
        }
    }
    vector<string> rslt;
    for(auto idx : wilst){
        rslt.push_back(dictionaryList[idx]);
    }
    return rslt;
}
#endif
