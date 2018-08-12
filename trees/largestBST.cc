/*
 * do post order traversal. leaf nodes and null nodes are BST. If node
 is null set cnt = 0. Count as  a parametr return is bool.
 count of BST is 1 + count of left BST  + count of right BST. if 
 both left and right are BST and this node satisfies BST else 
 return max(left BST, right BST)
 */

bool helper(Node *nd, int& cnt) {
    if(!nd) {cnt = 0; return true;}
    int clt = 0 ; int crt = 0;
    bool bl = helper(nd->left, clt);
    bool br = helper(nd->right, crt);
    
    if(bl && br){
        if((!nd->left || nd->left->val < nd->val) 
            && (!nd->right || nd->right->val > nd->val) ){
            cnt = clt + crt + 1;
            return true;
        }
            
    }
    cnt = max(clt, crt);
    return false;
}

int findLargestBST(Node* node) {
    int cnt = 0;
    helper(node, cnt);
    return cnt;
}

#if 0

bool
helper(Node *nd, int& cnt){
    if(!nd){cnt = 0; return true;}
    int cl = 0, cr = 0;
    bool bl = helper(nd->left, cl);
    bool br = helper(nd->right, cr);
    if(bl && br){
        // left and right subtree are BST so now test if the node
        // inclusing this tree is a binary tree.
        
        if(nd->left && nd->val > nd->left->val) bl = true;
        if(nd->right && nd->val < nd->right->val) br = true;
      
        if(bl && br){
            cnt = cl + cr + 1; return true; // add this int th e mix
        } else {
            cnt = max(cl, cr);
        } 
    }
     
     return false;
}

int findLargestBST(Node* node) {
    if(!node)
        return 0;
    int cnt = 0;
    helper(node, cnt);
    return cnt;
    

}
#endif
