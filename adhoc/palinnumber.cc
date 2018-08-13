/*
 Set the indexes i and j in the middle of the number converted to string
 j will be mid if # of digits is even else mid+1. i = mid -1
 travel left and right from the middle  till digits change
 mirror the left to the right. 
 start from mid - 1 and mid + 1. copy elements from left to right. If the 
 given number is a palindrome need to increment the mid number ( or tthe middle 
 two number if there are even digits). Adding carry to left and mirroring it to 
 right. Specia case also if left digit is found to be less than the right digit 
 while traversig out from the moddle. 
 */

#if 0
 
string convert2pal(string a, int& cval){
    int n = a.size();
    
    int mid = n/2;
    int i =  mid - 1;
    int j =0;
    // set the index i & j around mid.
    if(n%2 == 0){
        j = mid;
    } else {
        j = mid + 1;
    }
    
    while(i>=0 && a[i] == a[j]){
        i--; j++;
    }
    bool leftsm = false;
    if(i < 0 || a[i] < a[j]) {
        leftsm = true;
    }
    
    while(i >= 0){
        a[j++] = a[i--]; 
    }
    
    int carry = 0;
    if(leftsm){
        carry = 1;
        i = mid-1;
        if(n%2 != 0) {
            // odd
            int num = a[mid] - '0';
            num = num + 1;
            cout << " NUM " << num;
            carry = num /10;
            num = num % 10;
            a[mid] = num+'0';
            j = mid+1;
        } else {
            // even 
            j = mid;
        }
        
        while(i>=0){
            int num = a[i] + carry;
            carry = num/10;
            num = num%10;
            a[j++] = a[i--];
        }
    }
    
    cval = carry;
    return a;
}

#endif

string convert2pal(string a, int& cval){
    int n = a.size();
    bool leftsmall = false;
    int mid = n/2;
    int i = mid-1;
    
    int j = (n%2)?mid + 1 : mid ; // odd start adter mid

    // ignore the middle same elements
    while( i >= 0 && a[i] == a[j]){
        i--; j++;
    }
    // cant directly mirror if left digit is less that right
    // also if the given number is a palindrome we have
    // increment the middle digit
    if(i < 0 || a[i] < a[j])
        leftsmall = true;
    // mirror the left to right
    
    while(i >=0){
        a[j++] = a[i--];
    }
    // handle the case where the middle digit is to be 
    // incremented
    int carry = 0;
    if(leftsmall){
        carry = 1;
        i = mid - 1;
        
        // for odd we have to add 1 to middle number and 
        // progressivelt add carry to left  digits and then
        // mirroring the number
        if(n % 2){
            // odd
            int num = a[mid] - '0';
            num = num + 1;
            cout << " num " << num;
            
            carry = num /10;
            
            
            a[mid] = (num % 10) + '0';
            cout << " a[mid]" << a[mid] << endl;
            j = mid + 1;
        } else {
            // even 
            j = mid;
        }
        
        while(i >= 0){
            int num = (a[i] - '0') + carry;
            
            carry = num/10;
            
            a[i] = (num % 10) + '0';
            a[j++] = a[i--];
        }
    }
    cval = carry;
    return a; 
}


long next_palindrome(int n) {
    int cval = 0;
    string res = convert2pal(to_string(n), cval);
   cout << res << " out" << endl;
     // handle "999" . add 2 to the number.
     // 
    if(cval){
        char c = cval + '0';
        res = c+ res + c;
    }
    cout << " Res " << res << endl;
    return stol(res);
}
