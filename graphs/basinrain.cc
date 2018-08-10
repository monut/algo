*
 * Go through the matrix and find the sinks and queue them
 * The do dfs to find the basins for thise sinks
 */
bool isgood(int r, int c, int rows, int cols) {
    if(r<0 || r >= rows || c < 0 || c >= cols)
            return false;
    return true;
}

int r_mv[] = {1, -1, 0, 0};
int c_mv[] = {0, 0, -1, 1};

bool is_sink(int r, int c,vector<vector<int>>& emap){
    
    // if current cell is greatet than any of the surrounding cell 
    // then this can't be sink
    int min = emap[r][c];
    for(int i = 0; i < 4; i++) {
        int nr = r + r_mv[i]; 
        int nc = c + c_mv[i];    
        if(isgood(nr, nc, emap.size(), emap[0].size())) {
            if(min >  emap[nr][nc])
                return false;
        }
    }
    return true;
}

void find_basins(int r, int c, vector<vector<int> >& emap, vector<vector<bool> >& visited, int& sz){
        visited[r][c] = true;
        for(int i = 0; i < 4; i++) {
            int nr = r + r_mv[i]; 
            int nc = c + c_mv[i];    
            // is good and not visited check for that
            if(isgood(nr, nc, emap.size(), emap[0].size()) && !visited[nr][nc]) {
                if(emap[nr][nc] >= emap[r][c]){
                    // belong to same basin so increment the size
                    sz ++;
                    find_basins(nr, nc, emap, visited, sz);
                }
            }
        }
}
    
vector<int> calculate_sizes_of_basins(vector<vector<int>> emap) {
    int rows = emap.size();
    int cols = emap[0].size();
    
    queue<pair<int, int> > q;
    
    int cnt = 1;
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            if(is_sink(i,j,emap)){
               q.emplace(i,j);             
            }   
        }
    }
    
    vector<vector<bool> > visited(rows, vector<bool>(cols, false));
        
    vector<int> res;
    while(!q.empty()){
        auto s = q.front();
        q.pop();
        int r = s.first;
        int c = s.second;
        int sz = 1;
        find_basins(r, c, emap, visited, sz);
        res.push_back(sz);
    }
    return res;
}

