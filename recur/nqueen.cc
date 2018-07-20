#include "myutils.h"

using namespace std;
/*
 * Complete the function below.
 */

bool isgood(vector<string>& ires, int r, int c, int n){
    // check if this is valid
    if(r == 0){
        return true;
    }
    // check in each row if we have a queen in same column
    for(int a = 0; a < r; a++){
        if(ires[a][c] != '_')
            return false;
    }
    // left to right diagonal
    int i,j;
    for(i = r, j = c; i>= 0 && j >= 0; i--, j--){
        // diagonal l to r
            if(ires[i][j] != '_')
                return false;
    } 
        // diagnol to right top corner to l
    for(int i = r, j = c; i >= 0 && j < n ; i--, j++){
        if(ires[i][j] != '_')
            return false;
    }
    return true;
 }
void
helper(vector< vector<string> >& res, vector<string>& ires, int r, int pos, int n){
    if(r == n) {
        res.push_back(ires);
        return;
    }
    for(auto c = pos; c < n; c++){
        if(isgood(ires, r, c, n)) {
            // go on 
            ires[r][c] = 'q';
            helper(res, ires, r+1, 0,  n);
            ires[r][c] = '_';
        }
    }
 }

vector < vector<string> > find_all_arrangements(int n) {
   vector< vector<string> > res;
   string each_row(n, '_');
   vector<string> chess(n, each_row);
   helper(res,chess, 0, 0, n);
   cout << res;
   return res;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    vector < vector<string> > res;
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    res = find_all_arrangements(n);
    for(int res_i = 0; res_i < res.size(); res_i++) {
        for(int res_j = 0; res_j < res[res_i].size(); res_j++) {
            fout << res[res_i][res_j] << " ";;
        }
        fout << endl;
    }

    fout.close();
    return 0;
}

