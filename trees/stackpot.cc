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
/*
void postorderTraversal(Node* root) {
    stack<Node *> st;
    Node *pwalk = root;
    while(!st.empty() || pwalk != nullptr) {

        if(pwalk != nullptr) {
            st.push(pwalk);
            pwalk = pwalk->left;
        } else {
            Node *tmp = nullptr;
            tmp = st.top()->right;
            if(tmp == nullptr){
                // reached the leaf so print the val
                tmp = st.top();
                st.pop();
                cout << tmp->val << " ";
                while(!st.empty() && st.top()->right == tmp){
                    tmp = st.top();
                    cout << tmp->val << " ";
                    st.pop();
                } 
            } else { // else need to push to stack
                pwalk = tmp; 
            } 
        }
    }
    cout << endl;
}

*/

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
