
/*
 recursively go through each row starting from 0. and for row, 
 check all the columns in which Q can be placed. if good then place the queen
 and recursively check the next rows.  A cell is good if no no queen in rows
 above and the same column. Left diaginol (r--,c--) and right diagonal (r--, c++).
 */


bool 
isgood(vector<string>& ch, int r, int c){
    if(r == 0)
        return true;
        
    int num_rows = ch.size();
    int num_cols = ch[0].size();
    // check in rows above for the column
    for(int i = 0 ; i < r; i++){
        if(ch[i][c] == 'q'){
            return false;
        }
    }
    
    // check in the diagonal left
    int i = r, j = c;
    while(i >=0 && j >= 0){ // check i >= 0 
        if(ch[i--][j--] == 'q')
            return false;
    }
    
    // check in the diagonal right
    i = r, j = c;
    while(i >= 0 && j < num_cols){ // check for i >= 0
        if(ch[i--][j++] == 'q')
            return false;
    }
    return true;
}

void helper(vector<vector<string> >& res, vector<string> ch, int r, int n){
    if(r == n){
        res.push_back(ch);
    }
    
    for(int c = 0; c < n; c++){
        if(isgood(ch,r,c)) {
            // choose it and move to next row
            ch[r][c] = 'q';
            helper(res, ch, r+1, n);
            // reset
            ch[r][c] = '-';
        }
    }
}

vector <vector<string> > find_all_arrangements(int n) {
    vector< vector<string>> res;
    vector<string> chess(n, string(n,'-'));
    helper(res, chess, 0, n);
    return res;   
}

