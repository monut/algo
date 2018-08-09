/*  Create adjaceny list if not given
    Do topological sort.
    set distfrom = -1 as we want to find the maximum
    set parent[for all vertice ] = null
    set dist[from_node] to 0 as this is the source node
    Iterate through the graph in topological order setiing the dist for a
    vertiex if a path increase that value. Setting the parent node also 
    for that node.
     
	For the weighted graph:
	1. The number of nodes is <name>_nodes.
	2. The number of edges is <name>_edges.
	3. An edge exists between <name>_from[i] to <name>_to[i] and the weight of the edge is <name>_weight[i].
*/
void dfs(int from, vector<vector<pair<int, int> >>& adl, vector<int>& top_ord, vector<bool>& visited) {
    visited[from]=true;
    for(auto val : adl[from]){
        int to = val.first;
        if(!visited[to]){
            dfs(to, adl, top_ord, visited);
        }
    }
    // add in the order visited(revrse)
    top_ord.push_back(from);
}

vector<int> topological_sort(int dag_nodes, vector<vector<pair<int, int> > >& adl){
    vector<int> top_ord;
    vector<bool> visited(dag_nodes + 1, false);
    // iterate through all the nodes;
    for(int i = 1; i <= dag_nodes; i++){
        if(!visited[i]){
            dfs(i, adl, top_ord, visited);
        }
    }
    // reverse as the order to get the actual order
    reverse(top_ord.begin(), top_ord.end());
    return top_ord;
}

vector <int> find_longest_path(int dag_nodes, vector <int> dag_from, vector <int> dag_to, vector <int> dag_weight, int from_node, int to_node) {
    int num_edges = dag_from.size();
    // { From, {{n1, w1}, {n2, w2}}}
    vector<vector<pair<int, int> > > adjlist(dag_nodes + 1, vector<pair<int, int> >(0));
    for(int i = 0; i < dag_from.size(); i++){
        adjlist[dag_from[i]].emplace_back(dag_to[i], dag_weight[i]);
    }
    
    vector<int> top_ord = topological_sort(dag_nodes, adjlist);
    // longest path will contain longest path from from_node to ith node
    vector<long long int> longest_path(dag_nodes+1, -1);
    // parent [i] contains node through which longest_path[i] got updated last time
    vector<int> parent(dag_nodes + 1, 0);
    
    // start from the the from_node so the longest path from from_node to itself is zero
    longest_path[from_node] = 0;
    
    // iterate through the nodes in topological order. # of nodes is topological vector 
    // will be equal to total number of nodes.
    
    for(int i = 0; i < dag_nodes; i++){
        int from = top_ord[i];
        
        cout << " for node " << from;
        // the longest path will start from the from_node as only that is set to 0
        if(longest_path[from] >=0){
            
            // as we have updated information from_node to to_node for which longest 
            // path as been asked.
            if(from == to_node)
                break;
            for(auto ver : adjlist[from]){
                int to = ver.first;
                long long int wt = ver.second;
                // update the path if adding the edge is greater than
                // already found path length to "to" vertex 
                
                if(longest_path[to] <= longest_path[from]+wt){
                    longest_path[to] = longest_path[from] + wt;
                    parent[to] = from;
                }
            }
            
        }
    }
    // longest path 
    cout << " Longest Path :" << longest_path[to_node];
    // reconstruct the path
    vector<int> rslt;
    rslt.push_back(to_node);
    
    while(to_node != from_node){
        cout <<  " to_node " <<  to_node << endl;
        cout <<  " from_node " << from_node<< endl;
        to_node = parent[to_node];
        rslt.push_back(to_node);
        cout <<  " AFTER to_node " <<  to_node << endl;
        cout <<  " AFTER from_node " << from_node<< endl;
        
    }
    reverse(rslt.begin(), rslt.end());
    return rslt;
}
