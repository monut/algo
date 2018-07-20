#include "myutils.h"



/*
 * Complete the function below.
 */
bool is_start(char c){
    return c == '@';
}

bool is_stop(char c){
    return c == '+';
}

bool is_water(char c){
    return c == '#';
}

bool is_land(char c){
    return c == '.';
}

bool is_key(char c){
    return c >= 'a' && c <= 'j';
}

bool is_door(char c){
    return c >= 'A' && c <= 'J';
}

void 
find_startend(pair<int, int>& start, pair<int, int>& end, vector<string>& grid){
    size_t rows  = grid.size();
    size_t cols  = grid[0].length();
    for(size_t r = 0; r < rows; r++){
        for(size_t c = 0; c < cols; c++){
            if(is_stop(grid[r][c]))
                    end = {r, c};   
            if(is_start(grid[r][c]))
                    start = {r, c};   
        } 
    } 
    
}

vector < vector<int> > find_shortest_path(vector <string> grid) {
    pair<int, int> start, end;
    
    find_startend(start, end, grid);
    cout << start;
    cout << end;
    
    vector< vector<int> > res(2, vector<int>(3,-1));
    return res;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    vector < vector<int> > res;
    int grid_size = 0;
    cin >> grid_size;
    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    vector<string> grid;
    for(int i = 0; i < grid_size; i++) {
        string grid_item;
        getline(cin, grid_item);
        grid.push_back(grid_item);
    }

    res = find_shortest_path(grid);
    for(int res_i = 0; res_i < res.size(); res_i++) {
        for(int res_j = 0; res_j < res[res_i].size(); res_j++) {
            fout << res[res_i][res_j] << " ";;
        }
        fout << endl;
    }

    fout.close();
    return 0;
}
