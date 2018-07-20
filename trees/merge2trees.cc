#include "myutils.h"
/*
 * Merge two trees in O(N1 + ON2) time
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

void printInorder(Node* root) {
    if(!root) return;
    printInorder(root->left);
    cout << root->val << " ";
    printInorder(root->right);
}

Node* 
mergeTrees(Node* n1, Node* n2) {


}

int main() {
    //ofstream fout(getenv("OUTPUT_PATH"));
    int _size1;
    cin >> _size1;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    string _str1;
    getline(cin, _str1);
    Node* root1 = createTree(_str1);

    int _size2;
    cin >> _size2;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    string _str2;
    getline(cin, _str2);
    Node* root2 = createTree(_str2);

    Node* res = mergeTrees(root1, root2);
    printInorder(res);

    //fout << res << endl;
    
    //fout.close();
    return 0;
}
