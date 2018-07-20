#include "myutils.h"
/*
 * Complete the join_words_to_make_a_palindrome function below.
 */

class TrieNode {
public:
    unordered_map<char, TrieNode *> children;
    int index = -1;
    vector<int> lst;
};

bool 
is_palindrome(string word, int l, int r){
    while(l < r){
        if(word[l++] != word[r--])
            return false;
    }
    return true;
}

void
insert(TrieNode *root, string word, int indx){
    TrieNode *node = root;
    // go from end to start of word to inset in revers order
    for(int i = word.length() - 1 ; i >= 0; i--){
        char c = word[i];
        cout << " i = " << i;
        if(node->children[c] == nullptr){
            // node doesn't exist need to add one here
            node->children[c] = new TrieNode();
            cout << "insetring for word :" << word << " char : " << c << endl;
        }
        if(is_palindrome(word,0,i)){
            node->lst.push_back(indx);
        }
        node = node->children[c];
    }
    cout << "+++++++++++++++"  << endl;
    node->index = indx;
    node->lst.push_back(indx);
}

TrieNode*
build_reversetrie(vector<string> words){
    TrieNode *root = new TrieNode();
    int i = -1;
    for(string word : words){
        insert(root, word, i++);
        cout << " adding word :" << word << endl;
    }
    return root;
}

// res should return list of pairs which have index pair
void
searchtrie(string word, TrieNode *root, int indx, vector<pair<int, int> >& res){
    TrieNode *node = root;
    cout << "Looking for Word" << word << endl;
    auto j = -1;
    for(auto c : word){
        j++;
        cout << " char :" << c;
        if(node->index >= 0 && node->index != indx && is_palindrome(word, j, word.length() -1)){
            cout << " inserting index " <<  indx << " node->index " << node->index;
            res.emplace_back(indx, node->index);
        }
        node = node->children[c];
        
        if(node == nullptr){ cout << "hit null returning " ; return;}
    }
    
    for(auto val : node->lst){
        if(val == indx)
            continue;
         cout << "Inserting from List" << endl;
         cout << "val " << val << " indx : " << indx << endl;
        res.emplace_back(indx, val);
    }

}
vector<string> join_words_to_make_a_palindrome(vector<string> words) {
    /*
     * Write your code here.
     */
     TrieNode *root = build_reversetrie(words);
     vector< pair<int, int> > res;
     int i = -1;
     for(auto word : words){
        searchtrie(word, root, i++, res);
     }
     
     vector<string> vec;
     
     for(auto indx_pair : res){
        cout << "first:" << indx_pair.first << endl;
        cout << "second:" << indx_pair.second << endl;
        vec.push_back(words[indx_pair.first] + words[indx_pair.second]);
     }
     return vec;
}


int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int words_count;
    cin >> words_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<string> words(words_count);

    for (int words_itr = 0; words_itr < words_count; words_itr++) {
        string words_item;
        getline(cin, words_item);

        words[words_itr] = words_item;
    }

    vector<string> res = join_words_to_make_a_palindrome(words);

    for (int res_itr = 0; res_itr < res.size(); res_itr++) {
        fout << res[res_itr];

        if (res_itr != res.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

