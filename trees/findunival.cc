#include "myutils.h"

/*
5
1 2 # # 3
ans: 2
# is a null node

top down approach
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

/*
 * Complete the function below.
 */

bool helper(Node *nd, int *count) {
    if(nd == nullptr)
            return true;

    bool l = helper(nd->left, count);
    bool r = helper(nd->right, count);

    // all leaf nodes are unival
    if(l&&r) {
        Node *l = nd->left;
        Node *r = nd->right;

        // leaf node
        if(l == nullptr && r == nullptr) {
            *count += 1;
            return true;
        }    

        // left and right child exist and val matches
        if( l != nullptr && r != nullptr && l->val == nd->val && 
            r->val == nd->val) {
            *count += 1;
            return true;
        }    

        // no right child
        if( l != nullptr && r == nullptr && l->val == nd->val) {
            *count += 1;
            return true;
        }    
        // no left child
        if( l == nullptr && r != nullptr && r->val == nd->val) {
            *count += 1;
            return true;
        }    
    }
    retun false;
}

int findSingleValueTrees(Node* node) {
    int count = 0;
    helper(node, &count);
    cout << " Univals: " << count;
    return count;
}


int main() {
    ofstream fout(getenv("OUTPUT_PATH"));
    int _size;
    cin >> _size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    string _str;
    getline(cin, _str);
    Node* root = createTree(_str);

    int res = findSingleValueTrees(root);
    fout << res << endl;
    fout.close();
    return 0;
}
