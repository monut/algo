/*
given a grid of height from west (left) to east(right). Water can rise 
and fill the paths find the best path 
next_bst_row (c, r) {
   
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

