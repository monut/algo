
/*
loop through first "w" items and insert the index into queu if the array elemment 
is less than the element at the back of the queue
If it is more than pop that back index and insert.
For rest of the element check the front of the queue if the index has fallen outside the window
pop all the index which has fallen outside the window. 
Then follow the same steps as listed for forst "w" elements
The element at the front is the max element for each window

 */

vector <int> max_in_sliding_window(vector <int> arr, int w) {
 
    deque<int> dq;
    
    for(int i = 0; i < w; i++){
        while(!dq.empty() && arr[i] > arr[dq.back()] ){
            dq.pop_back();
        }
        dq.push_back(i);
    }
    
    // for the rset
    vector<int> res;
    res.push_back(arr[dq.front()]);
    cout << " arr " << arr[dq.front()];
    
    for(int i = w; i < arr.size(); i++){
        // pop elements which fall out of the window
        while(!dq.empty() && dq.front() <= i - w){
            dq.pop_front();
        }
        
        while(!dq.empty() && arr[i] > arr[dq.back()]){
            dq.pop_back();
        }
      
        dq.push_back(i);
        cout << " q.frot" << dq.front();
        cout << " arr " << arr[dq.front()];
        res.push_back(arr[dq.front()]);
    }
    return res;
}

/*
 [3 6 -6 0] W = 3 answer 6, 6
 */ 
#if 0
vector <int> max_in_sliding_window(vector <int> arr, int w) {
    deque<int> ins;
    vector<int> res;
    
    for(int i = 0; i < arr.size(); i++){
        while(!ins.empty() && arr[ins.back()] <= arr[i]) {
            ins.pop_back();
        }  
        ins.push_back(i);
        
        if(i >= w-1 ){
            // if index in the front is more than window removed
            // then pop it out 
            while(ins.front() <= i - w){
                ins.pop_front();
            }
            res.push_back(arr[ins.front()]);
            
        }
    }
    
    return res;

}

#endif
