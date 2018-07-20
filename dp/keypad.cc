#include "myutils.h"

/*
 * Complete the function below.
 */
bool 
valid_position(int row, int col) {
    int num_rows = 4;
    int num_cols = 3;
    if(col < 0 || col >= num_cols){
        return false;
    }
    
    if(row < 0 || row >= num_cols){
        return false;
    }
    
    if(row == 3 && col != 1){
        return false;
    }
    
    return true;
}

pair<int,int> 
positioninkpad(int val, vector<vector<int> >& kpad){

    for(auto i = 0; i < 4; i++){
        for(auto j = 0; j < 3; j++){
            if(kpad[i][j] == val)
                return {i,j};
        }
    }
    return {-1, -1};
}

int
numPhoneNumbers(int startdigit, int phonenumberlength) {

    if(startdigit < 0 || startdigit > 9){
        return 0;
    }
    
    // didgits from 0 to 9 so 10 digits
    // 0 numbers with 0 lenght and 1 number for each digit with 1
    // phone number length
    vector< vector<int> > dp(10, vector<int>(phonenumberlength +1, 0));
    
    vector< vector<int> > kpad= {{1, 2, 3}, 
                                 {4, 5, 6}, 
                                 {7, 8, 9},
                                 {-1, 0,-1}};
                                 
    
    for(int i = 0; i < 10; i++){
        dp[0][i] = 0;
        dp[1][i] = 1;
    }
  
  for(int len = 2; len <= phonenumberlength; len++){
    for(int digit = 0; digit < 10 ; digit++){
        // find all digits which can be reached from "digit" in the kpad
        auto pd = positioninkpad(digit, kpad); // assuming the digit is valid
        auto i = pd.first;
        auto j = pd.second;
        bool p1 = valid_position(i+1,j+2);
        bool p2 = valid_position(i+1,j-2);
        bool p3 = valid_position(i-1,j+2);
        bool p4 = valid_position(i-1,j-2);
        bool p5 = valid_position(i-2,j+1);
        bool p6 = valid_position(i-2, j-1);
        bool p7 = valid_position(i+2,j+1);
        bool p8 = valid_position(i+2,j-1);
        cout << " (" << i << "," << j << ")" << endl;
        dp[len][digit] = (p1?dp[len-1][kpad[i+1][j+2]]:0)
                        +(p2?dp[len-1][kpad[i+1][j-2]]:0)
                        + (p3?dp[len-1][kpad[i-1][j+2]]:0)
                        + (p4?dp[len-1][kpad[i-1][j-2]]:0)
                        + (p5?dp[len-1][kpad[i-2][j+1]]:0)
                        + (p6?dp[len-1][kpad[i-2][j-1]]:0)
                        + (p7?dp[len-1][kpad[i+2][j+1]]:0)
                        + (p8?dp[len-1][kpad[i+2][j-1]]:0);
    }
  
  }
  
  return dp[phonenumberlength][startdigit];
  
}

int main()
{
    int startdigit = 1;
    int phonenumberlength = 1;
    int res = numPhoneNumbers(startdigit, phonenumberlength);
     cout << res;

    return 0;
}
