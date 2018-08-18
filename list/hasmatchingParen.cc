/*
 Keep a map from the closing bracket to the open bracket
 Push if see any of the braces and pop if we see corresponding
 matching bracket else push the bracket. Handle the case where 
 stack can be empty. 
 */

bool 
hasMatchingParantheses(string strExpression) {
    stack<char> st;
    unordered_map<char, char> mp = {{']','['}, {'}', '{'}, {')','('}};
    string bks("[]{}()");
    
    for(auto c : strExpression){
        if(bks.find(c)!= string::npos){
            if(!st.empty()){
                if(st.top() == mp[c]){
                    st.pop();
                } else {
                    st.push(c);
                }
            } else {
                st.push(c);
            }
        }
    }
    return st.empty();  
}






#if 0
bool hasMatchingParantheses(string strExpression) {
    stack<char> st;
    unordered_map<char, char> mb = { {'}','{'}, {']','['},{')', '('} };
    string paren("{}[]()");
    
    for(auto i = 0; i < strExpression.length(); i++){
        if(paren.find(strExpression[i]) == -1){
              continue;// not parenthesis continue
        }
        if(strExpression[i] == '{' ||
            strExpression[i] == '[' ||
           strExpression[i] == '('){
                cout << " pushing " << strExpression[i] << endl;
                st.push(strExpression[i]);
                continue;
        }
        // closing parenthesis so stack top should have matching opening paren
        // if not found return with false 
        if(!st.empty()  && st.top() != mb[strExpression[i]]){
                return false;
        }else {
            if(st.empty())
                return false;
            st.pop();
        }
            
    }
    
    return (st.empty())?true:false;
    
}
#endif
