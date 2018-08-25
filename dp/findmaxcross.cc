#include <iostream>
#include <vector>

using namespace std;


int findcross(vector<vector<int> >& mtx){
    int rows = mtx.size();
    int cols = mtx[0].size();
    
    vector<vector<int> >  topm(rows, vector<int>(cols, 0));
    vector<vector<int> >  botm(rows, vector<int>(cols, 0));
    vector<vector<int> >  rtm(rows, vector<int>(cols, 0));
    vector<vector<int> >  ltm(rows, vector<int>(cols, 0));
    
    // initialize top and bottom row 
    for(int j = 0; j < cols; j++){
        topm[0][j] = mtx[0][j];
        botm[rows -1][j] = mtx[rows-1][j];
    }
    
    // initialize left column and right most column 
    for(int i = 0; i < rows; i++){
        ltm[i][0] = mtx[i][0];
        rtm[i][cols -1] = mtx[i][cols-1];
    }
    
    // assumption is nXn matrix
    // left matrix 
    for(int r = 0; r < rows; r++){
        for(int c = 1; c < cols; c++){
            if(mtx[r][c] != 0){
                ltm[r][c] = ltm[r][c-1] +1;
            } else {
                ltm[r][c] = 0;
            }
            
            if(mtx[c][r] != 0){
                topm[c][r] = topm[c-1][r] +1;
            } else {
                topm[c][r] = 0;
            }
        }
    }
    
    for(int r = rows-1; r >= 0; r--){
        for(int c = cols -2; c >=0; c--){
            //right to left
            if(mtx[r][c] != 0){
               rtm[r][c] = rtm[r][c+1] +1; 
            } else {
               rtm[r][c] = 0;
            }
    
            if(mtx[c][r] != 0){
                botm[c][r] = botm[c+1][r] +1;
            } else {
                botm[c][r] = 0;
            }
        }
    }
                
    int all_max = 0;
    pair<int, int> rc;
    for(int r = 0; r < rows; r++){
        for(int c = 0; c < cols; c++){
           int m1 = min(topm[r][c], botm[r][c]); 
           int m2 = min(ltm[r][c], rtm[r][c]); 
           int mymin = min(m1, m2);
            if(all_max < mymin){
                rc = {r,c};
                all_max = mymin;
            }
        }
    }
    
    return 4 * (all_max - 1) + 1;
}
// To execute C++, please define "int main()"
int main() {
    vector<vector<int> >  mat = 
    {
        { 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
        { 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 },
        { 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 },
        { 0, 0, 0, 0, 1, 0, 0, 1, 0, 0 },
        { 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 },
        { 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 },
        { 1, 0, 0, 0, 1, 0, 0, 1, 0, 1 },
        { 1, 0, 1, 1, 1, 1, 0, 0, 1, 1 },
        { 1, 1, 0, 0, 1, 0, 1, 0, 0, 1 },
        { 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 }
    };
    
    cout << " size " << findcross(mat);
}
