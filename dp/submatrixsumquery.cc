#include <iostream>
#include <vector>

using namespace std;

// To execute C++, please define "int main()"
using vv = vector<vector<int>>;
vv findsum(vv& mat){
    vv res(mat.size(), vector<int>(mat.size(), 0));
    int m = mat.size();
    int n = mat[0].size();
    
    for(int c = 0; c < n; c++){
        res[0][c] = mat[0][c];
    }
    
    // column wise sum
    for(int r = 1; r < m; r++){
        for(int c = 0; c < n; c++){
            res[r][c] = res[r-1][c] + mat[r][c];
        }
    }
   
    // row wise sum
    for(int r = 0; r < m; r++){
        for(int c = 1; c < n; c++){
            res[r][c] += res[r][c-1];
        }
    }
    
    return res;
}

int 
sumquery(const vv &res, pair<int, int>& up, pair<int, int>& lo){
        int valr = (up.first > 0)?res[up.first - 1][lo.second]:0; 
        int valc = (up.second > 0)?res[up.second - 1][lo.first]:0;
        int aval = (up.first > 0 && up.second > 0)?res[up.first-1][up.second - 1] : 0;    
        return res[lo.first][lo.second] - valr - valc + aval; 
}

int main() {
   vv mat = {
       {2,3,1},{4,1,2},{1,2,1} 
   };
    
   vv res = findsum(mat);
   
   pair<int, int> a = {1,1};
   pair<int, int> b = {2,2};
   cout << sumquery(res, a, b) << endl;
    
   for(int i = 0; i < mat.size(); i++){
   for(auto val : res[i]){
       cout << val << " ";
   }
        cout << endl;
    }
}


