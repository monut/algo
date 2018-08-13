#include <iostream>
using namespace std;

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

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


// start with the guess at the root if the tree
// pre order traversal while compare 
int curr_nxt = numeric_limits<int>::max();
int 
next(Node *root, int k){
    if(!root) return numeric_limits<int>::max();
    
    if( k < root->val && root->val < curr_nxt){
        curr_nxt = root->val;
    }
    if( k < root->val){
        curr_nxt = min(next(root->left, k), curr_nxt);
    } else {
        curr_nxt = min(next(root->right, k) , curr_nxt);
    }
    
    return curr_nxt;
}

// using stack
class BSTIterator {
private:
stack<Node *> st;

void push(Node *root){
    while(root){
        st.push(root);
        root = root->left;
    }
}

public:
    BSTIterator(Node *root){ push(root);}
    
    Node *next(){
        
        auto nd = st.top();
        st.pop();
        // add right branch nodes
        push(nd->right);
       
        return nd;
    }
    
    bool hasNext(){
        return !st.empty();
    }
};

int main() {
    int _size;
    cin >> _size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    string _str;
    getline(cin, _str);
    Node* root = createTree(_str);
    int k = 4;
    
    
    int nxt = next(root, k);
    cout << " next element of "  << k << " is " << nxt << endl;
    
    auto it = BSTIterator(root);
    
    while(it.hasNext()){
        auto nd = it.next();
        cout << nd->val  << " ";
    }
    cout << endl;
    
    printInorder(root);
    return 0;
}
/*
11
4 2 1  # # 3 # # 5 # #
answer: 4 for 3
*/
