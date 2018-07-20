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

bool  
find_path(Node *root, vector<Node *>& vec, int val){
    if(root == nullptr)
            return false;
    vec.push_back(root);
     
    if(root->val == val)
            return true;
    if(find_path(root->left, vec, val) 
            || find_path(root->right, vec, val))
            return true;
    // found not in either side so pop out this node
    vec.pop_back();
    return false;
}

void 
printPath(vector<Node *>& vec) {
    for( auto nd : vec) {
        cout << nd->val << " ";
    }
    cout << endl;
}

Node* 
findLCA(Node* root, int n1, int n2) {
    vector<Node *> vecn1;
    vector<Node *> vecn2;
    find_path(root, vecn1, n1);
    find_path(root, vecn2, n2);
    printPath(vecn1);
    printPath(vecn2);
    vector<Node *> rslt;
    set_intersection(all(vecn1), all(vecn2), back_inserter(rslt));
    return rslt.back(); 
}

int main() {
    
    int _size;
    cin >> _size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    string _str;
    getline(cin, _str);
    
    int _n1;
    cin >> _n1;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    int _n2;
    cin >> _n2;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    Node* root = createTree(_str);

    Node* n = findLCA(root, _n1, _n2);
    cout << n->val << endl;
    return 0;
}
