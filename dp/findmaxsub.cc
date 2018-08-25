int maxSubmatrix(vector < vector < int > > mtx) {
   /* 
    vector< vector<int> > mtx = {{0, 0, 1, 0}, 
                                 {0, 1, 1, 0},
                                 {0, 1, 1, 1}};
    */
    if(mtx.empty())
        return 0;
    int rows = mtx.size();
    int cols = mtx[0].size();
    
    vector< vector<int> > S(rows, vector<int>(cols, 0));
    // set the first row element to that of mtx
    for(int i = 0; i < rows; i++){
        S[i][0] = mtx[i][0];
    }

    // set the first col element to that of mtx
    for(int i = 0; i < cols; i++){
        S[0][i] = mtx[0][i];
    }

    for(int i = 1; i < rows; i++){
        for(int j = 1; j < cols; j++){
            if(mtx[i][j] == 0)
                S[i][j] = 0;
            if(mtx[i][j] == 1){
                S[i][j] = min(S[i-1][j], min(S[i][j -1], S[i-1][j-1]))+1;
            }
        }
    }
    
    // find max in matrix which point to the right left corner of
    // the largest sub matrix
    int max_i = 0, max_j = 0;
    int max = 0;
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            if(S[i][j] > max){
                max = S[i][j];
                max_i = i; max_j = j;
                //cout << " max " << max << endl;
            }
    
        }
    }
    //
    for(int i = max_i; i > max_i - max; i--){
        for(int j = max_j; j > max_j-max; j--){
            cout << setw(3) << mtx[i][j];
        }
        cout << endl;
    }
    return max;
}
//time compexity O(rows*cols) and space O(rows *cols)
