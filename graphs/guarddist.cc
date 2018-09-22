/*
 * Complete the find_shortest_distance_from_a_guard function below.
 Do  BFS
 create a output array with all position set to -1
 queue position of the guard and set the guard distance in OP as ZERO!!
 Process vertex from the front of queue and visit a cell only if it is "Open space"
 and has not been visited op[r][c] == -1
 and update the dist of the all the vertex which can be reached from threr
 queue these vertices
 */

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


struct vertex {
    int i;
    int j;
    int dist;
    vertex(int x = 0, int y = 0, int d = 0):i(x), j(y),dist(d){};
};

bool isgood(int r, int c, int num_rows, int num_cols) {
    if(r < 0 || r >= num_rows || c < 0 ||  c >= num_cols)
        return false;
    return true;
}
vector<vector<int> > shortestDistanceFromAGuard(vector<string> g){
    int rows = g.size();
    int cols = g[0].length();
    
    vector<vector<int> > op(rows, vector<int>(cols, -1));
    queue<vertex> myq;
    // find the guard position and q it
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            if(g[i][j] == 'G'){
                cout << "Gaurd position " << i << " " << j << endl;
                myq.emplace(i, j, 0);
                op[i][j] = 0; // guard should set to 0
            }
        }
    }
    // moves from a cell
    int r_mv[] = {1, -1, 0, 0};
    int c_mv[] = {0, 0, -1, 1};
    
    while(!myq.empty()){
        cout << " In Loop " << endl;
        auto val = myq.front();
        cout << " My val " << val.i << "  " << val.j << endl;
        // from here we can 4 different ways
        for(int i = 0; i < 4; i++){
            int r = val.i + r_mv[i];
            int c = val.j + c_mv[i];
            if(isgood(r,c, rows, cols)){
                if(g[r][c] == 'O' && op[r][c] == -1){
                    op[r][c] = val.dist + 1;
                    myq.emplace(r,c, op[r][c]);
                }
                    
            }
        }
        myq.pop();
    }
    return op;
}


