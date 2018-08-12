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

// construct the tree
struct Node {
    string val_;
    Node *left = nullptr, *right = nullptr, *nxtRight = nullptr;
    Node(string val = ""):val_(val){};
};

Node *deserialize(istringstream& in){
    if(in.eof())
        return nullptr;
    string val;
    in >> val;
    if(val == "#")
        return nullptr;
    Node *nd = new Node(val);
    nd->left = deserialize(in);
    nd->right = deserialize(in);
    return nd;
}

Node *createTree(string data){
    if(data.empty()) return nullptr;
    istringstream in(data);
    return deserialize(in);
}

void printtree(Node *root){
    if(!root)return;
    cout << root->val_ << " ";
    printtree(root->left);
    printtree(root->right);
}


void setsibling(Node *nd, Node *prev){
    if(!nd) return;
    
    if(prev == nullptr)
        nd->nxtRight = prev;
    if(prev){
        if(prev->right == nd){
            if(prev->nxtRight) {
                nd->nxtRight = (prev->nxtRight->left!=nullptr)?prev->nxtRight->left 
                                :prev->nxtRight->right;
            } else {
                nd->nxtRight = nullptr;
            }
            
        } else {
            nd->nxtRight = prev->right;
        }
    }
    prev = nd;
    setsibling(nd->left, prev);
    setsibling(nd->right, prev);
}

void
printSiblings(Node *root){
    while(root){
        cout << root->val_ << " ";
        Node *tmp = root;
        while(tmp->nxtRight){
            tmp = tmp->nxtRight;
            cout << tmp->val_ << " ";
        }
        root = root->left;
    }
}

int main() {
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int _size;
    cin >> _size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    string _str;
    getline(cin, _str);
    Node* root = createTree(_str);
    printtree(root);
    cout << endl;
    setsibling(root, nullptr);
    
    
    
    
    printSiblings(root);
    cout << endl;
    return 0;
return 0;
}

/*
13
 a b d # #  e # # c # f # #
*/
