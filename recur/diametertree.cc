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



/*
 * Complete the diameter_of_a_tree function below.
 */

int 
heightoftree(Node *root){
    if(!root) return 0;
    
    return 1 + max(heightoftree(root->left), heightoftree(root->right));
}

int
diameter_of_bt(Node *root){
    if(!root)
        return 0;
    int dlt = diameter_of_bt(root->left);
    int drt = diameter_of_bt(root->right);
    int hlt = heightoftree(root->left);
    int hrt = heightoftree(root->right);
    return max((1 + hlt + hrt), max(dlt, drt));
}


void diameter_of_a_tree(string tree, int ans) {
    /*
     * Write your code here.
     */
    
    int _size;
    cin >> _size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    //string _str = "1 2 4 # # 5 # # 3 # #"; // height 4 passs through root
    string _str = "1 2 4 6 10 # # # # 5 # 7 # 8 # 9 # # 3 # #"; // in left subtree 8
    getline(cin, _str);
    
    Node* root = createTree(_str);
    
    int dm = diameter_of_bt(root);
    cout << " diameter " << dm << endl;
    return;
}



