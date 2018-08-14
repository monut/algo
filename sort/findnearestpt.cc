// Complete the find_nearest_neighbours function below.
int mypartition(vector<pair<long, int> >& pts, int lft, int rt){
    int pvt = pts[lft].first;
    int i = lft; int j = rt;
    while( i < j){
        while(pts[i].first <= pvt)i++;
        while(pts[j].first > pvt)j--;
        swap(pts[i], pts[j]);
    }
   
    swap(pts[lft], pts[j]);
    return rt;
  
}
void
findtopK(vector<pair<long, int> >& pts, int lft, int rt, int k){
    if(lft > rt) return;
    int pi = mypartition(pts, lft, rt);
    if(k == pi) return;
    if(pi < k){
        findtopK(pts, pi+1, rt, k);
    } else if( pi > k) {
        findtopK(pts, lft, pi-1, k);
    } 
}

long 
getdistance(int x1, int y1, int x2, int y2){
    return (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1);    
}
vector<vector<int>> find_nearest_neighbours(int px1, int py1, vector<vector<int>> n_points1, int k1) {

    cout << " In Main " << endl;
    // {dist, index}
    int px = 3; int py = 2;
    int k = 4;
    vector<vector<int> > n_points = {{0,0}, {5,5}, {2,0}, {0,0}, {1, 7}, {5, -1}, {-1, 1},{9, 3}};
    vector<pair<long, int> > dist;
    int num_pts = n_points.size();
    for(int i = 0; i < num_pts; i++){
        cout << " Distnace  for point " << i << endl;
        long tmp = getdistance(px, py, n_points[i][0], n_points[i][1]);
        dist.emplace_back(tmp, i);
    }
    
    cout << " going to do findtop" << endl;
    
    findtopK(dist, 0, dist.size()-1, k);
    
    cout << " Done findtop" << endl;
     
    vector<vector<int> > res(k, vector<int>(2,0));
    
    
    for(int i = 0; i < k; i++){
         cout << " Points " << i << endl;
        res[i][0] = n_points[dist[i].second][0];
        res[i][1] = n_points[dist[i].second][1];
    }
    return res;
}
