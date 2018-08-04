#include "myutils.h"
/*
 * Find the paths to both node1 and node2. Then iterate from back both path1 and path2
 till we hit then node which is not same valu. Retunr the node just before that.
 T(N) + T(N) + T(N1 + N2) for  intersection. so O(N) complexity. 
 Second method - start from root. If root matches any node then that node is the  LCA. If not recurse left and right. 
 */
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


void
printPath(vector<Node *>& vec) {
    for( auto nd : vec) {
        cout << nd->val << " ";
    }
    cout << endl;
}


bool findpath(Node *root, vector<Node *>& res, int val){
    if(!root)
        return false;
    
    if(root->val == val) {
        res.push_back(root);
        return true;
    }
    
    bool lf = findpath(root->left, res, val);
    bool rt = findpath(root->right, res, val);
    if(lf || rt){
        // if either path returned true then this node is in the path
        res.push_back(root);
        return true;
    }
    return false;
}

Node * findcommonNode(vector<Node *>& v1, vector<Node *> v2){
    int i = v1.size() -1;
    int j = v2.size()-1;
    
    while(i >= 0 && j >= 0){
        if(v1[i] != v2[j])
            break;
        i--, j--;
    }
    // assumtion is there a common node
    return v1[i+1];
}

#define all(vec) vec.begin(), vec.end()

Node*
findLCA(Node* root, int n1, int n2) {

    vector<Node *> path1;
    vector<Node *> path2;
    
    findpath(root, path1, n1);
    findpath(root, path2, n2);
    // printPath(path1);
    // printPath(path2);
    return findcommonNode(path1, path2);
}

#if 0

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



#define all(w) w.begin(),w.end()
Node*
findLCA(Node* root, int n1, int n2) {
    vector<Node *> vecn1;
    vector<Node *> vecn2;
    find_path(root, vecn1, n1);
    find_path(root, vecn2, n2);
    vector<Node *> rslt;
    set_intersection(all(vecn1), all(vecn2), back_inserter(rslt));
    return rslt.back();
}


Node*
findLCA(Node* root, int n1, int n2) {
    if(!root)
        return nullptr;
    // n1 or n2 are in the same branch
    if(root->val == n1 || root->val == n2){
        return root;
    }
    Node *left_lca = findLCA(root->left, n1, n2);
    Node *right_lca = findLCA(root->right, n1, n2);
    // if n1 and n2 are found in left and right of the node then this node is the LCA
    if(left_lca && right_lca)
        return root;
    return (left_lca!= nullptr?left_lca:right_lca);
    
}
#endif
// Since two nodes exist we can solve single traversal method


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
