/*
 * Complete the function below.
 */


string decomp1(string str){
    string op;
    string num = "";
    for(auto c : str){
        if('0' <= c && c <'9')
            num = num + c;
        else {
            
            int cnt = stoi(num);
            while(cnt){
              op +=c; 
              cnt --;
            }
            num = "";
        }
    }
    return op;
}
// number can be only 127 so 1 byte
string decomp(string str){
    string op;
    int cnt = 0;
    int num = 0;
    for(auto c : str){
            if(cnt % 2 == 0){
                num = c -'0';
                cnt++;
                continue;
            }
            while(num){
              op +=c; 
                
              num --;
            }
            cnt++;
    }
    return op;
}

string RLE(string str) {
    string res;
    int pi = 0;
    int cnt = 0;
    for(int i = 0; i < str.size(); i++){
        if(str[pi] == str[i]){
            cnt++;
            pi = i;
            continue;
        } 
        
        if(cnt > 1) {
            res = res + to_string(cnt) + str[pi];
        } 
        if(cnt == 1)
            res = res +  str[pi];
        pi = i;
        cnt = 1;
    }
    
    if(cnt > 1) {
        res = res + to_string(cnt) + str[pi];
    } 
    if(cnt == 1)
        res = res + str[pi];
    
    cout << " " << res << endl;
    return res;
}

