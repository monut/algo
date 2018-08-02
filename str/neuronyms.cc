vector<string> neuronyms(string word){
    int len = word.size();
    vector<string> res;
    res.push_back(word.substr(0,1) + to_string(len-2) + word.substr(len-1));
    // The # of digits will go down from len - 2 to 2
    for(int i = len - 3; i >= 2; i--){ // number to be inserted in the middle
        for(int k = 0; k <= len-2-i ; k++){
            res.push_back(word.substr(0, k+1) + to_string(i) + word.substr(k+1+ i));
        }
    }
    return res;
    
}

vector<string> neuronyms1(string word) {
    /*
     * Write your code here.
     */
    auto i = 0 ;
    auto j = word.length() - 1;
    set<string> res;    
    while(++i < j-1){
        res.insert(word.substr(0,i) + to_string(j-i) + word.substr(j));
    }
    
    i = 1;
    while(i < j-1){
        res.insert(word.substr(0,i) + to_string(j-i) + word.substr(j));
        j--;
    }
    vector<string> out(res.begin(), res.end());
    return out;
}
