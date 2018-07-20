#include "myutils.h"

bool is_valid(int rows, int cols, int row, int col){
    // check bounds for row and col
    return row >= 0 && row < rows && col >= 0 && col < cols;
}

int find_minimum_number_of_moves(int rows, int cols, int start_row, 
            int start_col,int end_row, int end_col) {
    // initialize the chess board and mark all cells not visited
    vector<vector<int> > chess(rows, vector<int>(cols, -1));
    
    // initialize chess moves for knight from start position
    vector<int> r_mv = {2, 1, -2,  1, -2, -1, -1,  2};
    vector<int> c_mv = {1, 2,  1, -2, -1, -2,  2, -1};
    // row, col and distance from start code
    queue<tuple<int, int, int> > q;
    
    q.emplace(start_row, start_col, 0);
    
    while(!q.empty()){
        auto tup = q.front();
        q.pop();
        // reached the position 
        if(get<0>(tup) == end_row && get<1>(tup) == end_col){
            return get<2>(tup);
        }
        // loop through the reachable cells
        for(auto i = 0; i < 8; i++){
            int r = get<0>(tup) + r_mv[i];
            int c = get<1>(tup)+ c_mv[i];
            // row and col position falls within the chees board
            // and cell has not been visited
            if(is_valid(rows, cols, r, c) && chess[r][c] == -1){
                chess[r][c] = 1;
                q.emplace(r,c, get<2>(tup) + 1);  
                //cout << "[" << r <<"]" << "[" << c <<"]" << "=" << (get<2>(tup) + 1);
            }
        }
        
    }
    return -1;
    
}


int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int rows;
    cin >> rows;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int cols;
    cin >> cols;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int start_row;
    cin >> start_row;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int start_col;
    cin >> start_col;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int end_row;
    cin >> end_row;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int end_col;
    cin >> end_col;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int res = find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col);

    fout << res << "\n";
    cout << res << endl;
    fout.close();

    return 0;
}


