#include <algorithm>

using namespace std;
/*
12 10 20 8
15 9  11 9
20 7  10 30
10 8  12 15

given a grid of height from west (left) to east(right). Water can rise
and fill the paths find the best path
next_bst_row (c, r) {
    indexof = max(g[r-1][c-1], g[r][c-1], g[r+1][c-1]);
}

 best_height = 0;
 loop(rows)
    nxt_row = r;
    while(c < max_col-1){
       bst_row = next_best_row(r,c);
       min_height = min(g[r][c], g[c+1][bst_row]);
       nxt_row = bst_row
    }
    best_height = max(best_height, mi_height);
 }

 return best_height

*/

int
next_row(vector<vector<int> >& g, int r, int c){

    priority_queue<pair<int, int> > pq;

    if(r > 0 && r < g.size() && c < g.size())
            pq.emplace(g[r-1][c], r-1);

    if(r < g.size()-1 && c < g.size())
        pq.emplace(g[r+1][c], r+1);

    if(c < g.size())
        pq.emplace(g[r][c], r);

    auto val =  pq.top();
    return val.second;
}

int
best_height(vector<vector<int> >& g){
    int bh = 0;
    int N = g.size();

    for(int r = 0; r < N; r++){
        int nxt_r = r;
        int pmin = g[r][0]; // left most column
        for(int c = 1; c < N; c++){
            nxt_r = next_row(g, nxt_r, c);
                        pmin = min(pmin, g[nxt_r][c]);
        }
        bh = max(bh, pmin);
    }
    return bh;
}

int main() {
    vector<vector<int> > g = {
                            {12, 10, 20, 8},
                            {15, 9,  11, 9},
                            {20, 7,  10, 30},
                            {10, 8,  12, 15}
                        };
    cout << " Best Height " << best_height(g);
}

