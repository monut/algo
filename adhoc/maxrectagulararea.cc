/*
 * find maximum possible rectangular area formed by histogram
 */

long findMaxPossibleArea(vector<long> heights, int l, int r){
    
    int i = l;
    stack<int> st;
    long max_area = 0;
    long area = 0;
    // loop from [l , r] and index r inclusive
    
    while(i <= r){
        if(st.empty() || heights[st.top()] <= heights[i]){
            st.push(i++);
        } else{
            auto val = st.top();
            st.pop();
            // -1 becasue i has already moved and for empty stack we handle
            // the case where the popped elements was the only element 
            if(st.empty()){
                // number of bares from left to index
                area = heights[val] * (i-l);
            } else {
                area = heights[val] * (i-st.top()-1);
            }
             
            if(area > max_area ){
                max_area = area;
            }
        }
    }
    
    // pop rest of the elements from the stack
    while(!st.empty()){
        auto val = st.top();
        st.pop();
        
        if(st.empty()){
                // number of bares from left to index
                area = heights[val] * (i-l); 
            } else {
                area = heights[val] * (i-st.top()-1);
            }
        
        cout << " area " << area;
         cout << " area " << max_area;
        if( area > max_area){
            max_area = area;
        }
        
    }
    return max_area;
}
