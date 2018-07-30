
/*
 * do BFS while contriucting the dependency graph. Build the shortest 
 path tree prev[child] = parent. 
 "stop" should be added to the list of words prvoided.  add "start" to
 the bfs_q and mark it visited before starting the loop. don't forget 
 to pop item from q once its visited. 
 O(len*len*26);
???  O(num of words * len) ???
 */

unordered_map<string, vector<string> > g;
unordered_map<string, bool> visited;
queue<string> bfs_q;
unordered_map<string, string> mypar; // for shortest path tree

void build_graph(vector<string>& words, string start, string stop) {
    
    bfs_q.push(start);
    
    visited[start] = true;
    
    while(!bfs_q.empty()){
        auto wrd = bfs_q.front();
        bfs_q.pop();
        auto current_wrd = wrd;
        for(int i = 0; i < wrd.length(); i++){
        // change each letter with each of the 26 characters
            
            for(char c = 'a'; c <= 'z'; c++){
                char tmp = wrd[i];
                
                wrd[i] = c;
                auto it = find(words.begin(), words.end(), wrd);
                
                if(it != words.end() && !visited[*it]){
                    
                    g[wrd].push_back(*it);
                    bfs_q.push(*it);
                    visited[*it] = true;
                    mypar[*it] = current_wrd; // shortest path tree
                    cout << " parent " << current_wrd << endl;
                }
                wrd[i] = tmp; // reset
            }
        }
    }
     cout << " Done building graph" << endl;
}

vector<string> 
string_transformation(vector<string> words, string start, string stop) {

    // stop word
    words.push_back(stop);  
    for(auto st : words){
        mypar[st] = "";
    }
    
    build_graph(words, start, stop);
    vector<string> res;
    string u = mypar[stop];
    res.push_back(stop);
     cout << " Done building graph" << endl;
     
     
    while(u != start ){
        cout << " " << u << " ";
        if(u == "")
            break;
        res.push_back(u);
        u = mypar[u];
    }
    res.push_back(start);
    
    if(u == ""){
        return {"-1"};
    }    
   reverse(res.begin(), res.end());
   return res;
}
int main()
{
 
 vector<string> inp = {"cat", "hat", "bad", "had"};
 string st = "bat", en = "had";
 
 vector<string> vs = string_transformation(inp,st, en);
 
 for(auto val : vs){
     cout << val << " ";
 }


}
