#include "myutils.h"



bool helper(string txt, string pat, int t, int p){
    if(pat.length() == p) return t == txt.length();
    // edge condition if pattern has * at the end
    // txt = "abc"  pat = "abc*"
    if(t > txt.length()) return true;
    
    // this check need to be done first.
    if(pat[p] == '*' || (pat[p] != txt[t] && pat[p+1] == '*')) {
        // hold on to *
        bool br1 = helper(txt, pat, t+1, p);
        // skip the *
        bool br2 = helper(txt, pat, t+1, p+1);
        return br1 || br2;
    }
    if(pat[p] == '.')
        return helper(txt, pat, t+1, p+1);
    
    if(pat[p] == txt[t])
        return helper(txt, pat, t+1, p+1);

    
    return false;
}
    
bool isMatch(string strText, string strPattern) {
        cout << true;
 return helper(strText, strPattern, 0 , 0);


}

int 
main() {
    ofstream fout(getenv("OUTPUT_PATH"));
    bool res;
    string _strText;
    getline(cin, _strText);
    
    string _strPattern;
    getline(cin, _strPattern);
    
    res = isMatch(_strText, _strPattern);
    fout << res << endl;
    
    fout.close();
    return 0;
}

