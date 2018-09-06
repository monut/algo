#include <iostream>
#include <vector>

using namespace std;

vector< vector<bool> > visited;
int r_mv[] = {0, 0, 1, -1};
int c_mv[] = { 1, -1, 0 , 0};
bool is_valid(int r, int c, int rows, int cols){
    if(r < 0 || r > rows - 1 || c < 0 || c > cols -1 ){
        cout << " r " << r << " c " << c << " false " << endl;
        return false;
    }
        cout << " r " << r << " c " << c << " true " << endl;
    return true;
}

void set_cell_unsafe(vector< vector<int> >& mat){
   for(int r = 0; r < mat.size(); r++){
    for(int c = 0; c < mat[0].size(); c++){
      if(mat[r][c] == 0) {
      
       for(int i = 0; i < 4; i++){
         int rn = r + r_mv[i]; 
         int cn = c + c_mv[i]; 
         if(is_valid(rn, cn, mat.size(), mat[0].size())) {
                mat[rn][cn] = 0;          
         }
       }
      }
    }
   } 
}


void safe_route(vector< vector<int> >& mat, int& mind, int r, int c, int curd) {
    cout << " curd " << curd << " col " << c << endl;
 
    
    if(c == mat[0].size() - 1){
        cout << mind << endl;
        mind = min(mind, curd);
        return;
    }
    if(curd > mind){
        return;
    }
    
    visited[r][c] = true;
    for(int i = 0; i < 4; i++){
       int rn = r + r_mv[i]; 
       int cn = c + c_mv[i]; 
      cout << " rn " << rn << " cn " << cn << endl;
       if(is_valid(rn, cn, mat.size(), mat[0].size())) {
          if(mat[rn][cn] == 1 && !visited[rn][cn]) { 
              cout << " rn " << rn << " cn " << cn << endl;
              safe_route(mat, mind, rn, cn, curd + 1);
          }
       }
    }
   visited[r][c] = false;
    
}

int main(){
    vector<vector<int> >  mat = 
    {
        { 1, 1, 1, },
        { 1, 1, 1, },
        { 1, 1, 1, },
        { 0, 0, 0, }
    };
    
    set_cell_unsafe(mat);
    
    int mind = numeric_limits<int>::max();
    // start from first column
    for(int r = 0; r < mat.size(); r++){
        visited.assign(mat.size(), vector<bool> (mat[0].size(), false));
        int curd = 1;
        cout << " starting with " << r;
        if(mat[r][0] == 1) {
            safe_route(mat,mind,r, 0, curd);
        }
        cout << " mind for row  " << r << " " << mind << endl;
    }
    
    cout << " Min dist " << mind;
}
