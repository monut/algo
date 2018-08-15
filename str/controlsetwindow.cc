/*
create a map with control set characters. set missing to # of characters 
in control set. loop through the text string. Increment the count for control
set characters as we find them. decreas the missing count when ever count of 
characters in the control set increases from 0 to 1. Start shrining the window
when missing count goes dwon to zero and continue till missing is zero. 
Missing is incrmented when any of the control characters count goes from 1 to 0.
Update the max index if previous was larger.
 */

#if 0
// no duplciates
string MinWindow(string strText, string strCharacters) {
    unordered_map<char, int> cs;
    
    int i = 0, j = 0;
    int missing = strCharacters.length();
    // setting up the map 
    for(auto val : strCharacters){
        cs[val]= 0;
    }
    pair<int, int> maxp = {0, strText.length() - 1};
    while(i < strText.length()){
        if(cs.find(strText[i]) != cs.end()){
            cs[strText[i]] ++;
            // whenever we find the character for the first time 
            // then only we decrement the missing by 1. so to account 
            // for duplicates 
            if(cs[strText[i]] == 1) 
                    missing --;
        
            // if missing goes to zero we should start the optimization phase
            if(missing == 0){
                // shrink the window
                while(missing == 0){
                    if(cs.find(strText[j]) != cs.end()){
                        cs[strText[j]]--;
                        if(cs[strText[j]] == 0)
                            missing++;
                    } 
                    j++;
                }
                if((maxp.second - maxp.first) > (i - j + 1)){
                    maxp = {j-1, i};
                }
            } 
        }    
        i++;
    }
    
    return strText.substr(maxp.first, maxp.second - maxp.first + 1);
}

#endif

// with duplicates in control string
string MinWindow(string strText, string strCharacters) {
    
    if(strCharacters.length() > strText.length())
        return "";
    unordered_map<char, int> cs;
    
    int i = 0, j = 0;
    int found = 0;
    // setting up the map 
    for(auto val : strCharacters){
        cs[val] += 1;
        cout << cs[val] << endl;
    }
    
    pair<int, int> maxp = {0, strText.length() + 1};
    while(i < strText.length()){
        if(cs.find(strText[i]) != cs.end()){
            cs[strText[i]] --;
            // whenever we find the character for the first time 
            // then only we decrement the missing by 1. so to account 
            // for duplicates 
            if(cs[strText[i]] >= 0) 
                    found ++;
        
            // if missing equals to length of contril string.
            // we should start the optimization phase as we have found all the characters
            while(found == strCharacters.length()){
                    if(cs.find(strText[j]) != cs.end()){
                        cs[strText[j]]++;
                        if(cs[strText[j]] > 0)
                            found--;
                    } 
                    cout << " maxp.second " << maxp.second << endl;
                cout << " maxp.first " << maxp.first << endl;
                    j++;
                    if((maxp.second - maxp.first) > (i - j)){
                        cout <<  " changing J : " << j;
                        maxp = {j-1, i};
                    }
                    
            } 
        }    
        i++;
    }
    
    cout << maxp.first << " " << maxp.second;
    if((maxp.second - maxp.first) > strCharacters.length()) return "";
        
    return strText.substr(maxp.first, maxp.second - maxp.first + 1);
}


