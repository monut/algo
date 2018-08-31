#include <iostream>
#include <vector>

using namespace std;
void
rotmat(vector<vector<int> >& arr, int off){
    int n = arr.size() -1;
    for(int i = off; i < n - off -1; i++){
        for(int j = i ; j < n - i; j++){
         int tmp1 = arr[i][j];
         int tmp2 = arr[j][n-i];
         int tmp3 = arr[n-i][n-j];
         int tmp4 = arr[n-j][i];

         arr[i][j] = tmp4;
         arr[j][n-i] = tmp1;
         arr[n-i][n-j] = tmp2;
         arr[n-j][i] = tmp3;
        }
    }
}

int main() {
 vector< vector<int> > arr {
                            {1, 2, 3, 4},
                            {4, 5, 6, 7},
                            {8, 9, 10,11},
                            {12,13,14,15}
                            };

        for(int i = 0; i < arr.size(); i++){
            for(int j = 0; j < arr.size(); j++){
                cout << arr[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;
        for(int i = 0; i < arr.size()/2; i++){
            rotmat(arr, i);
        }
        for(int i = 0; i < arr.size(); i++){
            for(int j = 0; j < arr.size(); j++){
                cout << arr[i][j] << " ";
            }
            cout << endl;
        }
}
