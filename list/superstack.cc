
/*
 * Complete the function below.
 */

vector<string> tokenize(string str) {
    vector<string> res;
    string tmp;
    stringstream ss(str);
    while (getline(ss, tmp, ' ')) {
        if (!tmp.empty()) res.push_back(tmp);
    }
    return res;
}

class MyStack {
    private:
        vector<int> st;
    public:
        void push(int val){
            st.push_back(val);
        }
        void pop() {
            if(st.empty())
                return;
            st.pop_back();
        }
        
        void inc(int n, int val){
            if(st.empty())
                return;
            for(int i = 0; i < n && i < st.size(); i++){
                st[i] += val;   
            }
        }
}

void 
superStack(vector <string> operations) {

    MyStack()
    regex re(" ");
    vector<string> res;
    for(auto str : operations){
        res.clear();
        copy(sregex_token_iterator(str.begin(), str.end(), re, -1),
            sregex_token_iterator(), back_inserter(res));
            
    }
}
