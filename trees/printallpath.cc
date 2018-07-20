#include "myutils.h"

/*
27
222 29 76 66 159 81 192 235 249 147 # # 14 # # # # 40 # # # # # 195 # # #
# is a null node
222 29 76 66 159 81 192 235 249 147
222 29 76 66 159 81 192 235 249 14
222 29 76 66 159 81 40
222 29 195

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

void 
helper(Node *nd, vector<int> lst, int len){

    if(nd != nullptr) {
        lst.push_back(nd->val);
        len++;
        // if leaf node print the path from
        // 0 to len-1 index.
        if(nd->left == nullptr && nd->right == nullptr){
            for(auto i = 0; i < len; i++){
                cout << lst[i] << " ";
            }
            cout << endl;
        } 
    }

    if(nd->left != nullptr)
            helper(nd->left, lst, len);

    if(nd->right= nullptr)
            helper(nd->right, lst, len);
}

void 
postorderTraversal(Node* root) {

    vector<int> vec;
    helper(root, vec, 0);

}
*/
void
helper(Node *nd, vector<int> lst, int len){
  
    if(nd != nullptr){
        lst.push_back(nd->val);
        len++;
    
        if(nd->left == nullptr && nd->right == nullptr){
            // leaf node
            for(auto i = 0; i < len; i ++){
                cout << lst[i] << " ";
            }
            cout << endl;
            return;
        }
    }
    
    if(nd->left != nullptr)
        helper(nd->left, lst, len);
    if(nd->right != nullptr)
        helper(nd->right, lst, len);    

}

/*
 * Complete the function below.
 */
void printAllPaths(Node* root) {
    vector<int> vec;
    helper(root, vec, 0);
}


int main() {
    int _size;
    cin >> _size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    string _str;
    getline(cin, _str);
    Node* root = createTree(_str);
    printAllPaths(root);
    
    return 0;
}
