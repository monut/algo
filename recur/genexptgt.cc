
/*
 * Generate all possible expressions that evaluate to a givn target
 */

void helper(vector<string>& res,string s, string exp, long tgt, int pos, long curval, long last_val){
    if(pos == s.length()){
        if(tgt == curval){
            res.push_back(exp);
        }
        return;
    }
    
    for(int i = pos; i < s.length(); i++){
        auto str = s.substr(pos, i - pos + 1);
        auto val = stol(str);
        if(pos == 0){
            helper(res, s, exp +  str,tgt, i+1, val, val);
        } else {
            helper(res, s, exp + "+" + str, tgt, i+1, curval+val, val);
            
            helper(res, s, exp + "*" + str, tgt, i+1, curval-last_val + (last_val *val), last_val*val);
        }
    }
    
}

vector <string> generate_all_expressions(string s, long target) {
    vector<string> res;
    string exp;
    
    helper(res, s, exp, target,0, 0, 0);

    return res;
}
