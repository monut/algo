/* 

 */
 void addnode(BT nd, int val) {
  
 queue<BT> q;
 BT *cand = nullptr;
 q.push(nd);
 while(!q.empty()){
  auo val = q.front();
  if(val->left == nullptr && val->right != nullptr) val->left = new BT(val);
  if(val->left != nullptr && val->right == nullptr) val->right = new BT(val);
  if(val->left == nullptr && val->right == nullptr) cand = val;
  q.pop();
 }
 cand->left = new BT(val);
 
 }
 
