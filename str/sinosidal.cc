/*
 * decide on the number of rows. create a vector of vector with that 
 many rows and cols same as string length. Insert characters in array 
 while reducing the # of row, if # rows reaches zero start going in
 other direction by incrementing number of row.
 */
void print_string_sinusoidally(string s) {
    /*
     * Write your code here.
     */
    int len = s.length();
    int n = 3;
    vector< vector<char> > a(3, vector<char>(len,' ')) ;
    
    int row = 0;
    bool down = true;
    for(int i = 0; i < len; i++){
        a[row][i] = s[i];
        if(s[i] == ' ')
            a[row][i] = '~';
        if(row == n-1){
            down = false;
        } else if(row == 0){
            down = true;
        }
        
        (down)?row++:row--;
            
    }
    
    for(int i = 0; i < n; i++){
        
        
        for(int j = 0; j < len; j++){
            cout << a[i][j]  << " ";
        }
        cout << endl;
       
    }

}

