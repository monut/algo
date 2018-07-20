#include "myutils.h"

/*
27
222 29 76 66 159 81 192 235 249 147 # # 14 # # # # 40 # # # # # 195 # # #
# is a node
 */
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
void printInorder(Node* n) {
    if(!n) return;
    printInorder(n->left);
    cout << n->val << " ";
    printInorder(n->right);
}
/*
 * Complete the function below.
 */
void postorderTraversal(Node* root) {


}


int main() {
    int _size;
    cin >> _size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    string _str;
    getline(cin, _str);
    Node* root = createTree(_str);
    postorderTraversal(root);
    
    return 0;
}
