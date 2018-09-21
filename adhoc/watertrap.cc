/*
 * find water trapped
 */
int fmax(const vector<int>& v){
    int i = 0, j = v.size() -1;
    int max_a = 0;
    while(i < j){
        max_a = max(max_a, min(v[i], v[j]) *(j - i));
        if(v[i] < v[j]){
            i++;
        } else if(v[i] > v[j]) {
           j--; 
        } else {
            i++, j--;
        }
        
    }
    return max_a;
}
