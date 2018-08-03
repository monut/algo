#include <iostream>
#include <vector>
#include <limits> // max_limits
#include <sstream> // istringstream 
using namespace std;

struct Node {
    int val;
    Node* left;
    Node* right;
    Node(int v):val(v),left(nullptr), right(nullptr) {}
};


Node* deserialize(istringstream& in) {
        if(in.eof()) return nullptr;

        string val;
        in >> val;

        if(val.empty()) return nullptr;

        if (val == "#")
            return nullptr;

        Node* root = new Node(stoi(val));
        root->left = deserialize(in);
        root->right = deserialize(in);
        return root;
}

Node* createTree(string data) {
    if(data.empty()) return nullptr;
    istringstream in(data);
    return deserialize(in);
}


/*
 *  An empty tree is BST. Do in-order traversal and keep a previous
 pointer. Compare on the way up the stack if the prevoius value is < 
  current node val. Return false if not.
 */

bool helper(Node *root, Node* &prev){
    if(root == nullptr)
        return true;
    if(!helper(root->left, prev)) return false;
    
    if(prev != nullptr && prev->val >= root->val) return false;
    prev = root; //prev will be set at left most node
    
    return (helper(root->right, prev));
        
}

bool isBST(Node *root){
    Node *prev = nullptr;
    return helper(root, prev);   
}

int main() {
    
    int _str_size = 0;
    cin >> _str_size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n'); 
    vector<string> _str;
    string _str_item;
    getline(cin, _str_item);
    
    Node* root = createTree(_str_item);
    cout << isBST(root) << endl;
    
    return 0;
}
