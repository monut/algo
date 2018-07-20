#include <iostream>

using namespace std;
/*
 * Total number of possible binary trees with n nodes
 * If we choose one node say i, there will be i-1 node
 * on left and n-i nodes on the right. t(i-1)* t(n-1).
 * multiply because the number of arrangement on the 
 * left is independent of that on the right.
 */

long numBST(int n) {
    if( n == 1 || n == 0)
           return 1;
    long sum = 0;
    for( auto i = 1; i <= n; i++) {
        long a = numBST(i-1); // left
        long b = numBST(n-i); // right
        sum += (a*b) ;
    }
    return sum ;
}

int main() {
    long num = 0;
    while(num < 21 ) {
            cout << " Number of nodes:";
            cin >> num;
            
            long numtrees = numBST(num);
            cout << "Number of BST from " 
                 << num << " nodes is " 
                 << numtrees << endl;
    }
}
