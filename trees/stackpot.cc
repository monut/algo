#include "myutils.h"

/*
pwalk from root and push left nodes into stack till reach the left most node.  If there is right node of the
top of stack element then 
, set pwalk to right and continue pushing the node. If we reach a leaf node (no left or right child) 
pop the stack print the value. Compare with top stack and if the right node of top of stack is same
then pop the top of stack. Keep on doing til this holds.
27
222 29 76 66 159 81 192 235 249 147 # # 14 # # # # 40 # # # # # 195 # # #
# is a null  node
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


void postorderTraversal(Node* root) {
    Node *pwalk = root;
    stack<Node *> st;
    while(!st.empty() || pwalk != nullptr){
        if(pwalk != nullptr){
            st.push(pwalk);
            pwalk = pwalk->left;
        } else {
            Node *tmp = st.top()->right;
            if(tmp == nullptr){
                tmp = st.top();
                cout << tmp->val << " ";
                st.pop();
                while(!st.empty() && st.top()->right == tmp){
                    tmp = st.top();
                    cout << tmp->val << " ";
                    st.pop();
                }
            }  else {
                pwalk = tmp;
            }
        }
    }
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
