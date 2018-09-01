int find_int(ifstresm *is){
    int bucks = 1<<16;
    vector<int> cnt(bucks,0);
    int x;
    while(*is >> x){
        // get the MSB 16
        cnt[x>>16]+=1;
    }
    
    int cand = 0;
    for(int i = 0; i < bucks; i++){
        if(cnt[bucks] != bucks){
            cand = i; break;
        }
    }
    
    is.clear(); is.seekg(0, ios.begin());
    bitset<bucks> bt_vec;
    while(*is >> x){
        if(x>>16 == cand){
            //get lower bits
            int low_bits = (1<<16 -1)&x;
            bit_vec.set(low_bits);
        }
    }
    
    for(int i = 0; i < bucks; i++){
        if(bit_vec[i] == 0){
            return (cand << 16) | i;
        }
    }

}


int find_an_integer_not_among_given_integers(vector<int> nos) {
    int radix = 16;
    int sz = nos.size() + 1; // one for the missing number
    int num_radix = (sz/radix) + 1;
    uint16_t bitar[num_radix] = {0};
    
    // bit mask
    for(auto val : nos){
        int byte_pos = val/radix;
        int bit_pos = val%radix;
        bitar[byte_pos] |= (1 << bit_pos);
    }
    int i = 0; int pos = 0;
    for(int i = 0; i < num_bits; i ++){
        if((bitar[i] ^ 0xffff)){
            // all bits are not set
            int pos = log2(bitar[i]) + 1 ;
            break;
        }
    }
     int num = (i*radix) + pos;
    cout << num;
    return num;
    
}

