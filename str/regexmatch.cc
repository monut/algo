/*
  "*" zero or more
  "." one character
  branch out in case * hold on to * or skip start
 */

bool helper(string str, string pat, int i, int j){
    
    if(j == pat.length()) return i == str.length();
    
    // edge condition if pattern has * at the end
    // txt = "abc"  pat = "abc*"
    if(i > str.length()) return true;
    
    if(pat[j] == '*')
        return (helper(str,pat, i+1,j) || helper(str, pat, i, j+1));
    
    if(str[i] == str[j])
        return helper(str, pat, i+1, j+1);
    if(pat[j] == '.')
        return helper(str, pat, i+1, j+1);
    return false;
}
