/*
Topological sort and reverse post order to create a path 
but first need to verify if there is DAG or nor.
*/

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;


class Solution {
    vector<bool> visited;
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
    
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        visited.assign(numCourses, false);
        cout << " In here ";
        unordered_map<int, vector<int> > adjl;
        for(auto elem : prerequisites){
            cout << elem.first << endl;
            adjl[elem.first].push_back(elem.second);
        }
        
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
    vector<pair<int, int> > vec = {{1,0}};
    Solution sl;
    sl.canFinish(nco, vec);
}
