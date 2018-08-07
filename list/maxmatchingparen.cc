/*
 * Brute Force : divide into substrings and see if each substring is balanced. O(N^2) for substrings
 * and for O(N) to check the validity => O(N^3). Space O(N)
 * O(N) space and time : push -1 in a stack push index when "("  and pop when ")"
  when popping subtract st.top from i to get maximum  possible string so far
  https://leetcode.com/articles/longest-valid-parentheses/
  O(N ) and no extra space
  start scanning from left. lft++ for every "(" and rt++ for every ")"
  if lft == rt maxlegth = 2*lft
  After that scan from right, lft. if lft == rt maxlength = max(2*rt , maxlength) 
 * if lft > rt then reset rt=lft = 0
 */
int find_max_length_of_matching_parentheses(string brackets) {
    stack<int> st;
    auto rslt = 0;
    st.push(-1);
    for(int i = 0; i < brackets.length() ; i++){
        if(brackets[i] == '(')
            st.push(i);
        else { // ')'
            st.pop();
            if(!st.empty()){
                
                rslt = max(i - st.top(), rslt);
                
            }else{
                st.push(i);
            }
        }
    }
    
    
    return rslt;
}
