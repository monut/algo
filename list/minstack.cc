
template<typename T>
class minstack {
    private:
        stack<T> st;
        stack<T> minst;
    public:
        void push(T val){ 
            st.push(val); // prevent SEGV on empty stack
            if(minst.empty() || minst.top() >= val ){
                minst.push(val);
            }
            
        };
        
        void pop(){
            if(st.empty()) // 
                return;
            if(st.top() == minst.top()){
                minst.pop();
            }
            st.pop();
        }
    
        T min(){
            if(minst.empty())
                return -1;
            else
                return minst.top();
        }
};

#endif
vector<int> 
min_stack(vector<int> operations) {
    vector<int> res;
    minstack<int> mst;    
    for(auto val : operations){
        if(val == 0){
            res.push_back(mst.min());
        } else if(val == -1){
           mst.pop();
        } else {
            mst.push(val);    
        }
    }
    return res;
}

