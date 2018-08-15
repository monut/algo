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

int fliptree(Node* node) {
    stack<Node *> st;
    st.push(node);
    while(!st.empty()){
        Node *tmp = st.top();
        if(tmp->left == nullptr)
                break;
        st.push(tmp->right); 
        st.push(tmp->left); 
    }

    Node *root = st.top();
    while(!st.empty()){
        Node *tmp = st.top();
        st.pop(); 
        if(st.empty())
                break;
        Node *l = st.top(); 
        tmp->left = l;
        l->left = nullptr;
        l->right = nullptr;
        st.pop();
        if(st.empty())
                break;
        Node *r = st.top(); 
        tmp->right = r;
        r->left = nullptr;
        r->right = nullptr;
    }

    printInorder(root);
}
// recursive solution
/*
 * Post order trevaresal and start flipping on the way up;
 */

Node* flipTreeRecur(Node* node) {
    if(!node) return nullptr;
    Node *ndl = flipTreeRecur(node->left);   
    Node *ndr = flipTreeRecur(node->right);
    node->left = ndr;
    node->right = ndl;
    return node;
}

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));
    int _size;
    cin >> _size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    string _str;
    getline(cin, _str);
    Node* root = createTree(_str);

    int res = fliptree(root);
    fout << res << endl;
    fout.close();
    return 0;
}
