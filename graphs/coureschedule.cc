/*
Topological sort and reverse post order to create a path 
but first need to verify if there is DAG or not
*/

#include <iostream>
#include <unordered_map>
using namespace std;


#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;


class Solution {
    vector<bool> visited;
    vector<bool> recur;
    vector<int> path;
public:
    void explore(int nd, unordered_map<int, vector<int> >& adjl ){
        visited[nd] = true;
        
        auto vec = adjl[nd];
        for(auto w : vec){
            if(!visited[w]){
                explore(w, adjl);
            }
        }
        cout << " Pushing in " << nd;
        path.push_back(nd);
    }
    
   
    void DFS(unordered_map<int, vector<int> >& adjl){
        for(auto nd : adjl){
            cout << " DFS " << nd.first << endl;
            if(!visited[nd.first]){
                explore(nd.first, adjl);
            }
        }
    }
    
    bool util(int u, unordered_map<int, vector<int> >& adjl){
        if(!visited[u]){
            visited[u] = true;
            recur[u] = true;
            for(auto w : adjl[u]){
               if(!visited[w] && !util(w, adjl)) {
                   return false;
               } else if(recur[w]){
                   return false;
               }
            }
        }    
        recur[u] = false;
        return true;
    }
        
    bool isdag(unordered_map<int, vector<int> >& adjl){
       for(auto elem : adjl){
           if(!util(elem.first, adjl))
                    return false;
       } 
       return true;
    }
    
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        visited.assign(numCourses, false);
        recur.assign(numCourses, false);
        cout << " In here ";
        unordered_map<int, vector<int> > adjl;
        for(auto elem : prerequisites){
            cout << elem.first << endl;
            adjl[elem.first].push_back(elem.second);
        }
        
        if(!isdag(adjl)){
            cout << " is Not a DAG" << endl;
            return false;
        }
        
        visited.assign(numCourses, false);
        DFS(adjl);
        
        int i = 0;
        for(auto val : path){
            if(i != val) return false;
            i++;
            cout << "Path " << val << " ";
                
        }
        return true;
    }
};

// To execute C++, please define "int main()"
int main() {
    // vector<int> v = {7, 4, 2, 4, 9};
    int nco = 2;
    vector<pair<int, int> > vec = {{1,0}, {2,1}};
    // vector<pair<int, int> > vec = {{1,0}, {0,1}};
    Solution sl;
    sl.canFinish(nco, vec);
}
