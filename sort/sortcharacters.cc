/*
    Create a frequency graph by going tjrough each character
    and incrementing the coutn for that charcter ( ASCII fro 0 to 256)
    Then creating the string by going through frequency graph and adding 
    the characters by the count of those characters.
*/
string sortCharacters(string inString) {
    
    vector<int> fg(256, 0);
    for(char c : inString) {
        int p = c;
        //fg[c-0] +=1;
        fg[p] +=1;
        
    }
    
    string res;
    
    for(int i = 0; i < 256; i++){
        int cnt = fg[i];
        while(cnt > 0){
            char c = i ;
            res += c;
            cnt--;
        }
    }
    return res;
}

