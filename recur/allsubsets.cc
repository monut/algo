/*
 * include or exclude the i'th character and form the set as you go
 * add to the result set when i == string.length()
 */

void helper(vector<string>& res, string s, string exp, int i){
    if(i == s.length()){
        res.push_back(exp);
        return ;
    }
    
    // include a char 
    helper(res, s, exp + s[i], i+1);
    // exclude a char
    helper(res, s, exp, i+1);
}

vector <string> generate_all_subsets(string s) {
    vector<string> res;
    string exp;
    helper(res, s, exp, 0);
    return res;
}
