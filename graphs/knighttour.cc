#include "myutils.h"

/*
    Do BFS to find shortest path from start to end. Make a grid. queue the 
    start row and start col. Set it to zero. everything else is set to -1.
    Do BFS. Try out each of the eight possible moves and update cell with the 
    distance. Before procssing next entry examine if its is end cell. If yes break.
    Don't forget to pop the item which is being examined. Also valis check return
    false if row >= num_rows || col >= num_cols as there are zero indexed rows and cols.
 */

bool isvalid(int nr, int nc, int rows, int cols){
    if(nr < 0 || nr >= rows || nc < 0 || nc >= cols)
        return false;
    return true;    
}

int find_minimum_number_of_moves(int rows, int cols, int start_row, int start_col,int end_row, int end_col) {
    vector<int> r_mv = {2, 2, -2, -2, 1 , -1 , 1, -1};
      vector<int> c_mv = {1, -1, 1, -1, 2, 2, -2, -2};
    
    vector<vector<int> > chess(rows, vector<int>(cols, -1));
    
    queue<pair<int, int> > q;
    q.emplace(start_row, start_col);
    chess[start_row][start_col] = 0;
    while(!q.empty()){
        auto cell = q.front(); q.pop();
        if(cell.first == end_row && cell.second == end_col)
            break;
        for(int i = 0; i < 8; i++){
            int nr = cell.first + r_mv[i];
            int nc = cell.second + c_mv[i];
            // break out if reached the end spot
            
            if(isvalid(nr, nc, rows, cols) && chess[nr][nc] == -1){
                // not visited and valid move
                chess[nr][nc] = chess[cell.first][cell.second] + 1;
                q.emplace(nr,nc);
            }
        }
    }
    
    return chess[end_row][end_col];
}

#if 0



bool is_valid(int rows, int cols, int row, int col){
    // check bounds for row and col
    return row >= 0 && row < rows && col >= 0 && col < cols;
}



int find_minimum_number_of_moves(int rows, int cols, int start_row, int start_col,int end_row, int end_col) {
    // initialize the chess board and mark all cells not visited
    vector<vector<int> > chess(rows, vector<int>(cols, -1));
    
    // initialize chess moves for knight from start position
    vector<int> r_mv = {2, 1, -2,  1, -2, -1, -1,  2};
    vector<int> c_mv = {1, 2,  1, -2, -1, -2,  2, -1};
    // row, col and distance from start code
    queue<tuple<int, int, int> > q;
    
    q.emplace(start_row, start_col, 0);
    
    while(!q.empty()){
        auto tup = q.front();
        q.pop();
        // reached the position 
        if(get<0>(tup) == end_row && get<1>(tup) == end_col){
            return get<2>(tup);
        }
        // loop through the reachable cells
        for(auto i = 0; i < 8; i++){
            int r = get<0>(tup) + r_mv[i];
            int c = get<1>(tup)+ c_mv[i];
            // row and col position falls within the chees board
            // and cell has not been visited
            if(is_valid(rows, cols, r, c) && chess[r][c] == -1){
                chess[r][c] = 1;
                q.emplace(r,c, get<2>(tup) + 1);  
                //cout << "[" << r <<"]" << "[" << c <<"]" << "=" << (get<2>(tup) + 1);
            }
        }
        
    }
    return -1;
    
    
}
/*
5
5
0
0
4
1
*/

#endif
