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



#if 0
struct vertex {
    int i,j, dist;
    //vertex():i(0),j(0), dist(0){}; not node needed for C style initializaion of struct
};

int row[] = {1, -1, 0, 0 };
int col[] = {0, 0, 1, -1};

bool issafe(int x, int y, int rows, int cols){
    // within bounds of grid
    if(x < 0 || x > rows-1 || y < 0 || y > cols -1)
        return false;
    return true;
};


// Do BFS on the matrix with guards starting as zero dist
vector<int> find_shortest_distance_from_a_guard(vector<vector<char>> d) {
    
    vector<vector<char> > grid = {
        {'O', 'O', 'O', 'O', 'G'},
        {'O', 'W', 'W', 'O', 'O'},
        {'O', 'O', 'O', 'W', 'O'},
        {'G', 'W', 'W', 'W', 'O'},
        {'O', 'O', 'O', 'O', 'G'}
    };
    // hardcode the  grid
    // scan the input grid and queue the position of the gurard. Set the open position 
    // as -1 and
    int rows = grid.size();
    int cols = grid[0].size();
    int op[rows][cols];
    cout << "rows " << rows;
    cout << "cols " << cols << endl;
    

    queue<vertex> q;
    for(int i = 0; i < rows; i++){
        cout << " grid" ;
         for(int j = 0; j < cols; j++){
            op[i][j] = -1;
             cout << grid[i][j];
            if(grid[i][j] == 'G'){
                vertex v = {i, j, 0};
                q.push(v);
                // guard has zero dist as have to find shortest dist from guard
                op[i][j] = 0; 
            }
        }   
        cout << endl;
    }
    
    while(!q.empty()){
        auto vert = q.front();
        // process all the four directions we can go from this cell 
        int x = vert.i; int y = vert.j; int dist = vert.dist;
        
        for(int pos = 0; pos < 4; pos++){
            
             if(issafe(x + row[pos], y + col[pos], rows, cols) 
                    && (grid[x + row[pos]][y + col[pos]] == 'O' 
                    && op[x + row[pos]][y + col[pos]] == -1)){
                  // update the output  matrix with dist value
                  op[x + row[pos]][y + col[pos]] = dist + 1;
                  //push the new cell into queue
                 vertex v = {x + row[pos], y + col[pos], dist+1};
                 //cout << v.i << " " << v.j << " " << v.dist << endl;
                 q.push(v);
             }
        }
        q.pop(); // done with the entry
    }
    
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            cout << setw(3) << op[i][j];
        }
        cout << endl;
    }

    return {};
}
