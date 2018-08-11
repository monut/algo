
/*
 * do BFS while contriucting the dependency graph. Build the shortest 
 path tree prev[child] = parent. 
 "stop" should be added to the list of words prvoided.  add "start" to
 the bfs_q and mark it visited before starting the loop. don't forget 
 to pop item from q once its visited. 
 word length = len, # of words = N
 Runtime : T(26 * len) to contruct words by substituting the letters
 for each word T(len) to find the matching word in the given list 
 => O(len^2 * 26)
 2) approach: For each word compare with words in the list to find the
  one which differ by 1 letter T(N  * len) this has to be done for each 
  of the word so O( N * len * N).
 */
/*
 * do BFS while contriucting the dependency graph. Build the shortest 
 path tree prev[child] = parent. 
 "stop" should be added to the list of words prvoided.  add "start" to
 the bfs_q and mark it visited before starting the loop. don't forget 
 to pop item from q once its visited. 
 */


unordered_map<string, bool> visited;
unordered_map<string, string> path;

void build_graph(vector<string>& words, string start){
    
    
    queue<string> q;
    q.push(start);
    visited[start] = true;
    while(!q.empty()){
        
        // Don't forget to pop and set visited to true for the node
        auto cur_word = q.front(); 
        
        
        q.pop();
        
        string wrd = cur_word;
        
        for(int i = 0; i < wrd.length(); i++) {
            
            for(char c = 'a'; c <= 'z'; c++){
                char tmp = wrd[i];
                wrd[i] = c; //replace
                auto it = find(words.begin(), words.end(), wrd);
                if(it != words.end() && !visited[wrd]){
                    path[wrd] = cur_word; 
                    visited[wrd] = true;
                    q.push(wrd); // Need to push the new word
                }
                
                wrd[i] = tmp; // reset
            }
        }
        
    }
}

vector<string> 
string_transformation(vector<string> words, string start, string stop) {
    if(words.size() == 0) return {"-1"};
    
    if(find(words.begin(), words.end(), stop) == words.end()){
        // insert stop only it is not present 
        words.push_back(stop);
    } else {
        words.push_back(stop);
    }
    
    build_graph(words, start);
    
    vector<string> res;
    while(stop != start && stop != string()){
        res.push_back(stop);
        stop = path[stop];
    }
    if(stop != string()){
        res.push_back(start);
    }
    
    reverse(res.begin(), res.end());
    return res;
}





#if 0
//hashmap for words
unordered_map<string, int> position;
unordered_map<int, int> parent;
vector<bool> visited;
queue<int> bfs_q;

void
build_graph(string cur_str, int idx){
    // change letter in th current string and if match found in
    //  words update the parent position for the index
    for(int i = 0; i < cur_str.length(); i++){
        char tmp = cur_str[i];
        for(char c = 'a'; c <= 'z'; c++){
            cur_str[i] = c;
            auto it = position.find(cur_str);
            
            if( it != position.end() && visited[it->second] != true){
                // found a macth the node has not been visited
                // mark it visted and update the parent index
                visited[it->second] = true;
                parent[it->second] = idx;
                // insert the node index in q to explored later 
                bfs_q.push(it->second);
            }
        } // got through all letter in position i
        // revert the curr string to original position
        cur_str[i] = tmp;
     } // loop through all the chars
    
   
}

void
solution(vector<string>& words, string& start, string& stop){
    
    // include the stop word
    for(int i = 0; i < words.size(); i++){
        position[words[i]] = i;
    }
    
    visited.assign(words.size(), false);
    // -1 for starting string
    // build the graph
    bfs_q.push(-1);
    string cur_str;
    while(!bfs_q.empty()){
        int idx = bfs_q.front();
        bfs_q.pop();
        if(idx == -1) {
            cur_str = start;
        } else {
            cur_str = words[idx];
        }
        build_graph(cur_str, idx);
    }
}

vector<string> string_transformation(vector<string> words, string start, string stop) {
    int str_len = start.length();  
    
    if(words.size() == 0)
        return {"-1"};
    words.push_back(stop);
    solution(words, start, stop);
    // find the parent index of stop word from parent map
    // and up the chain till we find start word index which
    // -1. Stop was inserted as last word
    auto it = parent.find(words.size() - 1);
    vector<string> ans;
    if(it == parent.end()){
        ans.push_back("-1");
        return ans;
    }
    int cur_idx = words.size() - 1;
    
    while(cur_idx != -1){
        ans.push_back(words[cur_idx]);
        cur_idx = parent[cur_idx];
    }
    // and the start string
    ans.push_back(start);
    reverse(ans.begin(), ans.end());
    return ans;
}
/*
4
cat
hat
bad
had

bat
had
{bat, hat had}
*/
#endif

int main()
{
 
 vector<string> inp = {"cat", "hat", "bad", "had"};
 string st = "bat", en = "had";
 
 vector<string> vs = string_transformation(inp,st, en);
 
 for(auto val : vs){
     cout << val << " ";
 }


}
