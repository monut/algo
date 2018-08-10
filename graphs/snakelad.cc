/*
There are N cells in the board. if Moves[i] != -1  points to position of ladder 
or snake.
- Do BFS from the first cell 
- and from each cell try out all the six options
*/
// number of cells and a flatout snakes and ladder

int getmindice(int N, vector<int>& lad){
    vector<bool> visited(N, false);
    
    queue<pair<int, int> > q;
    q.emplace(0,0); // first cell and dist 0;
    visited[0] = true;
    while(!q.empty()){
        auto val = q.front();
        int c = val.first; 
        if(c == N-1)
            break; // reached the end;
         q.pop();
        for(int i = c + 1; i <= c+6; i++){
            if(!visited[i]){
                visited[i] = true;
                if(lad[i]!=-1){
                    q.emplace(lad[i], val.second+1);
                } else {
                    q.emplace(val.first+1, val.second+1);
                }
            }
        }
        
    }
    
    
    return q.back().second;
}
#if 0
int 
getmindice(int N, vector<int>& mvs){
   // mark all cells as not visited
   vector<bool> visited(N, false);
   // {node #, distance}
   queue<pair<int,int> > q;
   q.push({0,0}); // {0, 0} try
   
  
   visited[0] = true;
   pair<int, int> qe;
  
   while(!q.empty()){
        qe = q.front();
        int v = qe.first;
        
        if(v == N -1)
            break;
            
        q.pop();
        // check all the 6 cells starting from v
        for(int i = v + 1; i <= (v + 6) && i < N; ++i){
            if(!visited[i]){ // visit now
                visited[i] = true;
                // distance from the current cell by 1 move 
                // so increase by 1
                pair<int, int> a ={0,0};
                a.second = qe.second + 1;
               
                if(mvs[i] != -1){
                    a.first = mvs[i];
                } else {
                    a.first = i;// normal cell
                }
                q.push(a);
            }
        }
   
   }
   cout << q.size() << endl;
   // The front element of the queus has the least distance to 
   // reach the end
   cout << "dist " << qe.second;
   return qe.second;
}

#endif

int find_min_no_of_dice_throws(vector<vector<int>> bd) {
    /*
     * Write your code here.
     */
     cout << bd.size();
     int N = 30;
     vector<int> moves(N, -1);
     // Ladders
    moves[2] = 21;
    moves[4] = 7;
    moves[10] = 25;
    moves[19] = 28;
 
    // Snakes
    moves[26] = 0;
    moves[20] = 8;
    moves[16] = 3;
    moves[18] = 6;
    return getmindice(30, moves);
 }

