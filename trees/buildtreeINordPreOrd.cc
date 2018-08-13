/*
 * Complete the function below.
 */
struct Node {
    int val;
    Node *left, *right;
    Node(int v):val(v){};
};

#define all(vec) vec.begin(),vec.end()

Node *helper(vector<int>& inO, int inst, int inend, vector<int>& preO, int prest, int preend){
    // st > end the return
    if(inst > inend) return nullptr;
    
    Node *nd = new Node(preO[prest]);
    int INidx = find(all(inO), preO[prest]) - inO.begin();
   
   // int root_idx = 0;
    // handle the left tree
    nd->left = helper(inO, inst, INidx - 1, preO, prest + 1, prest + INidx - inst);
    // handle the right tree
    //nd->right = helper(inO,  INidx + 1, inend, preO, prest + 1 + INidx - inst, prest + INidx - inst);
    nd->right = helper(inO,  INidx + 1, inend, preO, prest + 1 + INidx - inst, preend);
    
    return nd;
}

void
printtreeIN(Node *root){
    if(!root) return;
    printtreeIN(root->left);
    cout << root->val << " ";
    printtreeIN(root->right);
}

void
printtreePre(Node *root){
    if(!root) return;
    cout << root->val << " ";
    printtreePre(root->left);
    printtreePre(root->right);
}

void BFT(Node *root){
    queue<Node *> q;
    q.push(root);
    
    while(!q.empty()){
        int ncnt = q.size();
        
        while(ncnt--){
            auto elem = q.front();
            if(elem->left) q.push(elem->left);
            if(elem->right) q.push(elem->right);
            cout << elem->val << " ";
            q.pop();
        }
        cout << endl;
        
    }
    cout << endl;
}

void 
constrctTree(vector < int > iInOrderArray, vector < int > iPreOrderArray) {
    
    Node *root = 
        helper(iInOrderArray, 0, iInOrderArray.size() - 1, iPreOrderArray, 0, iPreOrderArray.size() -1);
        
        //printtreeIN(root);
        // cout << endl;
        // printtreePre(root);
        // cout << endl;
        BFT(root);
}

