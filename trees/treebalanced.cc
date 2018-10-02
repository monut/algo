struct Node {
  int leftlen,
  int rightlen,
  int left_wt;
  int right_wt;
  Node *left;
  Node *right;
}
/*
  Only th leaf node will have a weights
 */

bool ifBalanced(Node *nd, int& wt) {
  if(!nd) { wt = 0; return true;}
  int wtl = 0; int wtr = 0;
  bool bl = ifbalanced(nd->left, wtl);
  bool br = ifbalanced(nd->right, wtr);
  
  if(bl && br) {
    if((left_wt + wl) * leftlen == (right_wt + wr) * right_len) {
        wt = left_wt+right_wt + wl + wr; return true;  
    }
    return false;
  }
}
