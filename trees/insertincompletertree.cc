/*
  BFS the tree and insert a new node at a left or right empty slot
  identify a candidate node if the level is full.

 */
 
 Node *btree(Node *root, int val){
  if(!root) return new Node(val);
  queue<Node *> q;
  q.push(root);
  
  while(!q.empty()){
    auto elem = q.front(); q.pop();
    if(!elem->left && elem->right != nullptr) return elem->left = new Node(val);
    if(elem->left != nullptr && !elem->right) return elem->right = new Node(val);
    if(!elem->left && !elem->right) return elem->left = new Node(val);
    q.push(elem->left);
    q.push(elem->right);
  }
   
 
 
 }
