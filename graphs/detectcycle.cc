#include <iostream>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

class Graph {
    int v_ ;// # of vertices
    map<int, vector<int> > adjlist;
    
    void explore(int v, vector<bool>& visited);
    bool util(int v, vector<bool>& visited, vector<bool>& recurse);
public:
    Graph(int v):v_(v){};
    void addEdge(int v, int w);
    void dfs();
    bool isCyclic();
};

void
Graph::addEdge(int v, int w) {
        adjlist[v].push_back(w);
}


void
Graph::explore(int v, vector<bool>& visited){
    visited[v] = true;
    vector<int> lst = adjlist[v];
    cout <<  " => " ;
    for(auto w : lst){
    
        if(!visited[w]){
            cout << w ;
            explore(w, visited);
        } 
    }
    
}

void 
Graph::dfs(){
    // DFS the graph
    // set visited to false
    vector<bool> visited(v_, false);
    for(auto val : adjlist){
        cout << " Visiting " << val.first;
        if(!visited[val.first]){
            explore(val.first, visited);
        }
        cout << endl;
    }
}

bool
Graph::util(int v, vector<bool>& visited, vector<bool>& recurse){
    if(!visited[v]){
        visited[v] = true;
        recurse[v] = true;
        vector<int> lst = adjlist[v];
        
        for(auto w : lst){
            // if not visited then vist and if already visited check 
            // in this recursion stack if it was visited in this traversal
            // if yes then return true
            if(!visited[w] && util(w, visited, recurse)){
                return true;
            } else if(recurse[w]){
                return true;
            }
                
        } 
    }
    recurse[v] = false; // reset recursion visit stack 
    return false;
}

bool 
Graph::isCyclic(){
    // DFS the graph
    // set visited to false
    vector<bool> visited(v_, false);
    vector<bool> recurse(v_, false);
    
    for(auto val : adjlist){
        cout << " Visiting " << val.first;
        
        if(util(val.first, visited, recurse))
                                    return true;
       
        cout << endl;
    }
    return false;
}



int main() {
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
    Graph *g = new Graph(3);
    g->addEdge(0, 1);
    g->addEdge(1, 2);
    //g->addEdge(2,0);
    
    bool reslt = g->isCyclic();
    if(reslt){
        cout << " Is cyclic" << endl;
    } else {
        cout << " Not cyclic" << endl;
    }
    
    g->dfs();
return 0;
}
