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

/*
convert the BST into sorted linked list by in-order traversal. keep ref to ptr for head
and prev ptr. set head to node if prev ptr is null. Then merge the two sorted list.
Create a balanced BST with linked list. return n1 or n2 if either of them is empty. 
BSTmergeTrees(Node *sortedlist, in cnt). find mid of number of nodes, move the pointer
to the midde node. This is the new root. Now rmid_node->left = bstmt(lst, m-1) , 
mid_node->right(md_node->right, cnt - m);
O(Nlog(N)) = travel N but every level reduced by 1/2 at each level

Building top up can be done O(N). As building as we do. Build in inorder 
For O(N) solution keep going to the left reducing the cnt by half and returning
when count reaches zero. 
Construct the node and set up the left and right pointer and adjust the list pointer
to next . Return parent address.
*/

// prev is set at the left most node. This 
// can be used to set the head of the list
void BST2ll(Node *nd, Node* &hd, Node* &prev){
    if(!nd) return;
    BST2ll(nd->left, hd, prev);
    if(!prev) {
        hd = nd;
    } else {
        prev->right = nd;
        prev->left = nullptr;
    }
    
    prev = nd;
    BST2ll(nd->right, hd, prev);
}

Node* mergesortedlistrecur(Node *l1, Node *l2){
    if(l1 == nullptr)
        return l2;
    if(l2 == nullptr)
        return l1;
    if(l1->val < l2->val){
        l1->right = mergesortedlistrecur(l1->right, l2);
        return l1;
    } else {
        l2->right = mergesortedlistrecur(l1, l2->right);
        return l2;
    }
}


Node* mergesortedlistit(Node *l1, Node *l2){
    if(!l1) return l2;
    if(!l2) return l1;
    Node *head = nullptr;
    if(l1->val < l2->val)
        head = l1;
    else 
        head = l2;
    
    while(l1 != nullptr  && l2 == nullptr){
        if(l1->val < l2->val){
            l1 = l1->right;
        } else {
            Node *tmp = l1->right;
            l1->right = l2;
             l2 = l2->right;
            l1->right->right = tmp;
            l1 = tmp;
        }
    }
    return head;
}

int numnodes(Node *nd){
    Node *l = nd;
    int cnt = 0;
    while(l){
        cnt++;
        l = l->right;
    }
    return cnt;
}

// start building from the midle O(N(logN)). 

Node * BSTfromSortedList(Node *lst, int cnt){
    if(lst == nullptr ||  cnt <= 0)return nullptr;
    
    int mid = cnt/2 + 1;
    int m = mid; // preserve the value of mid
    Node *pw = lst;
    while(--mid > 0){
        pw = pw->right;
    }
    // pw cannot be null as it will point to middle node 
    // or the last node. 
    // cout << " pw->val " << pw->val << endl;
    // Node *parent = new Node(pw->val);
    
    pw->left = BSTfromSortedList(lst, m-1);
           
   pw->right = BSTfromSortedList(pw->right, cnt - m);
    return pw;
}

Node * BSTfromSortedListOptimal(Node* &lst, int cnt){
    if(cnt <= 0) return nullptr;
    
    int mid = cnt/2 + 1;
    Node *lchild =  BSTfromSortedListOptimal(lst,mid-1);
    Node *parent = lst;
    lst = lst->right; // move list to next item;
    parent->left = lchild;
    parent->right = BSTfromSortedListOptimal(lst,cnt - mid);
    return parent;
}


void
printlist(Node *nd){
    while(nd){
        cout << nd->val << " ";
        nd = nd->right;
    }
    cout << endl;
}

Node* 
mergeTrees(Node* n1, Node* n2) {
    if(!n1) return n2;
    if(!n2) return n1;
    // create lists
    Node *lst1 = nullptr;
    Node *prev = nullptr;
    BST2ll(n1, lst1, prev);
    // cout << " printing 1st" << endl;
    //printlist(lst1);
    
    Node *lst2 = nullptr;
    prev = nullptr;
    BST2ll(n2, lst2, prev);
   
    //cout << " printing 2st" << endl;
    // printlist(lst2);
    
   // merge the lists
    lst1 = mergesortedlistrecur(lst1, lst2);
    
    // cout << " printing merged list" << endl;
     // printlist(lst1);
    
    int cnt = numnodes(lst1);
    // cout << "count " << cnt << endl;
    //Node *ntree = BSTfromSortedList(lst1, cnt);
    Node *ntree = BSTfromSortedListOptimal(lst1, cnt);
    return ntree;
}


/*
pre order input and # represent null node
12
7 3 2 # # 4 # # 10 # 11 # # #
12
17  13 12 # # 14 # # 110 # 111 # # #
*/

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
