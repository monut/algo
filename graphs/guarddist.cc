#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int r_mv = {1, -1, 0, 0};
int c_mv = {0, 0, 1, -1};
vector<vector<int> > shortestDistanceFromAGuard(vector<string> g){
    int rows = g.size();
    int cols = g[0].length();
    
    vector<vector<int> > op(rows, vector<int>(cols, -1));
    // find guard position and insert in q to do BFS
    // set the G position to 0 in op
    
    
    queue<pair<int, int> > q;
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            if(g[i][j] == 'G'){
                q.emplace(i, j);
                dp[i][j] = 0;
            } 
        
        }
    }
    
    while(!q.empty()){
        auto cell = q.front(); q.pop();
        int r = cell.first;
        int c = cell.second;
        
        for(int i = 0; i < 4; i++){
            int n_r = r + r_mv[i];
            int n_c = c + c_mv[i];
            if(isvalid(n_r, n_c, rows, cols) && g[n_r][n_c] == 'O' && op[n_r][n_c] == -1){
                op[n_r][n_c] = op[r][c] + 1;
                q.emplace(n_r, n_c);
            }
        }
    }
    return op;
    
}
