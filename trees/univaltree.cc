/*
 top down take a node and search down and keep counter. 
 Not efficient as look at each node for every node O(N^2). 
 Bottom  up approach start from the leaf nodes. All leaf nodes are unival 
 trees.If right tree and left tree exist then current node val should be same as
 left and right node val. O(N)
 
 */



bool helper(Node *nd, int& cnt){
    if(!nd)
        return true;
    bool lt = helper(nd->left, cnt);    
    bool rt = helper(nd->right, cnt);
    if(lt & rt) {
        // all tree below are univals so now we need to
        // so lets check if the one including the root is unival
        Node *ltt = nd->left;
        Node *rtt = nd->right;
        
        // leaf node
        if(!ltt && !rtt){
            cnt++;
            return true;
            // left and right child exist and val matches
        } else if(ltt && rtt && ltt->val == nd->val && rtt->val == nd->val){
            cnt++; return true;
            // no right child
        } else if (ltt && !rtt && ltt->val == nd->val){
            cnt++; return true;
            // no left child
        } else if(!ltt && rtt && rtt->val ==  nd->val){
            cnt++; return true;
        }
    }
    
    return false;
}

int findSingleValueTrees(Node* node) {
    int count = 0;
    helper(node, count);
    cout << " Univals: " << count;
    return count;
}
