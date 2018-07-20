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


bool
isBST(Node *root) {
    if(root == nullptr){
        return true;
    }
    
    // left or right could be null check for it
    if(root->left != nullptr && root->left->val >= root->val) {
        return flase;
    }
    if(root->right != nullptr && root->right->val <= root->val) {
        return flase;
    }
    return isBST(root->left) && isBST(root->right);
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
