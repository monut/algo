/* 

 */
 void addnode(BT *nd, int val) {
  
 queue<BT *> q;
 BT *cand = nullptr;
 q.push(nd);
 while(!q.empty()){
  auo val = q.front();
  if(val->left == nullptr && val->right != nullptr) { val->left = new BT(val); return; }
  if(val->left != nullptr && val->right == nullptr)  { val->right = new BT(val); return; }
  if(val->left == nullptr && val->right == nullptr)  { cand = val; break; }
  q.push(val->left); q.push(val->right);
  q.pop();
 }
 cand->left = new BT(val);
 
 }
 
