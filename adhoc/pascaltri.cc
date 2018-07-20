#include "myutils.h"

/* (n k) = (n-1 k -1) + (n-1 k);
 */
int 
main(){
    int n = 6;
    vector<vector<int> > ad(n, vector<int>(n, 0));
    ad[0][0] = 1;
    for(int i = 1; i < n; i ++) {
        for(int j = 0; j < i; j ++) {
            ad[i][j] =(((i-1) < 0 || (j-1) < 0)? 0 : ad[i-1][j-1]) + (
                          (i-1) < 0 ? 0 : ad[i-1][j]); 
            cout << ad[i][j] << " ";
        }
        cout << endl;
    } 
    
}
