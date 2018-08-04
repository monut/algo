/*

Post order traversl. Preseve the ends of the lists being stiched. (l1end = l1->left  && l2end = l2->left) 
stich list from left traversal to root, Then stich the resuting list with one got my right traversal.
Before stiching set roots  node's left and right pointer point to self. Circular list so
first node left points to last node. drawing trees/dll along with pointers helps. handle root == null 
condition in linking 2 list as well in recursive function.
Post order : action can be taken after both left and right of the tree have been visited

 * smple input 
 * 21 
 * 335 -77 -81 # # 19 # # 547 505 350 # # # 807 692 # # 816 # #
 * Output: -81 -77 19 335 350 505 547 692 807 816 
 */
#include "myutils.h"

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


Node *stitch(Node *n1, Node *n2) {
    if(n1 == nullptr)
        return n2;
    if(n2 == nullptr)
        return n1;
    Node *n1_last = n1->left;
    Node *n2_last = n2->left;
    n1_last->right = n2;
    n2->left = n1_last;
    n2_last->right= n1;
    n1->left = n2_last;
    return n1;
}

Node *helperBSTtoLL(Node* root) {
    if(root == nullptr)
        return nullptr;
    Node *l1 = helperBSTtoLL(root->left);
    Node *l2 = helperBSTtoLL(root->right);
    // single node case
    root->left = root;
    root->right = root;
    l1 = stitch(l1, root);
    l1 = stitch(l1, l2);
    return (l1);
}

void printList(Node *head)  {
    Node *pWalk = head;
    while(pWalk != nullptr){
        cout << pWalk->val << " ";
        // walk before the check for head 
        pWalk = pWalk->right;
        if(pWalk == head)
                break;
    } 
}


void BSTtoLL(Node* root) {
    root =  helperBSTtoLL(root);
    printList(root);
}

int main() {
    int _size;
    cin >> _size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    string _str;
    getline(cin, _str);
    
    Node* root = createTree(_str);
    BSTtoLL(root);
    
    return 0;
}
