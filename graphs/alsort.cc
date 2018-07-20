#include "myutils.h"

void dfs(char from, unordered_map<char, vector<char> >& g, string& s, unordered_set<char>& visited){
    visited.insert(from);
    for(auto it = g[from].begin(); it != g[from].end(); it++){
        if(visited.find(*it) == visited.end()){
            dfs(*it, g, s, visited);
        }
    }
    s = from + s;
    cout << " res build " << s;
}

string 
topological_sort(unordered_map<char, vector<char> >& g){
    string res;
    // to keep track of nodes/letter visited 
    unordered_set<char> visited;
    for(auto it = g.begin(); it == g.end(); it++){
        // if node not visited then visit the node and it's neighbour
        if(visited.find(it->first) != visited.end()){
            dfs(it->first, g, res, visited);
        }
    }
    return res;
}
string find_order(vector <string> words) {
    int n = words.size();
    unordered_map<char, vector<char>> g;
    
    //initialize graph by mapping the unique letters in all the words
    for(int i = 0; i < n; i++){
        for(int j = 0; j < words[i].length(); j++){
            g[words[i][j]] = vector<char>(0);
        }
    }
    // compare adjacent words and add mimacted letter to the adjaceny list 
    // of the graph for the letter {aaa, aab} then a ---> b 
    for(int i = 0; i < n -1 ; i++){
        int min_length = min(words[i].length(), words[i+1].length());
        
        for(int j = 0; j < min_length; j++){
            if(words[i][j] != words[i+1][j]){
                g[words[i][j]].push_back(words[i+1][j]);
                break;
            }
        }
    }
    
    // Graph is done
    // do topological sorting to have 
    return topological_sort(g);

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string res;
    int words_size = 0;
    cin >> words_size;
    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    vector<string> words;
    for(int i = 0; i < words_size; i++) {
        string words_item;
        //getline(cin, words_item);
        cin >> words_item;
        words.push_back(words_item);
    }

    res = find_order(words);
    fout << res << endl;

    fout.close();
    return 0;
}

