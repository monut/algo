/*
 * Give a number N, the left tree can have 0 to N nodes and
 for each of these choice the left tree will have the remaining 
 nodes. Number of trees on the left is independent of the number 
 of trees on the right so multiply the results. Also loop to 
 choose each of the node. 
 * O(N^N)
 */
long how_many_BSTsRecur(int n) {
    if(n == 0 || n == 1)
            return 1;
    long sum = 0;
    
    // all the way to n as the tree with zero node 
    for(int i = 1; i <= n; i++){
        long a = how_many_BSTsRecur(i-1);
        long b = how_many_BSTsRecur(n-i);
        sum += a*b;
    }
    return sum;
}

long how_many_BSTs(int n){
    return how_many_BSTsRecur( n);
}


long how_many_BSTsDP(int n){
    vector<long long int> bsts(n+1, 0);
    bsts[0] = 1;
    //bsts[1] = 1;
    
    for(int numNodes = 1; numNodes <= n; numNodes++){
        for(int numLnode = 0; numLnode < numNodes; numLnode++){
            int numRNode = numNodes - 1 - numLnode; // exclude the root node
            bsts[numNodes] += (bsts[numLnode] * bsts[numRNode]);
        }
    }
    return bsts[n];
}
