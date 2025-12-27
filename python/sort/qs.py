def choosePivot(a, st, end):
    pivot = st
    l = st + 1
    r = end
    while(l < r):
        while(a[l]<= a[pivot]):
            l=l+1
        while(a[r]> a[pivot]):
            r=r-1
        if (l < r):
            a[l], a[r] = a[r], a[l]
    a[pivot], a[r] = a[r], a[pivot] 
    return r
    
def qs(a, st, end):
    if st >= end : return
    pi = choosePivot(a, st, end)
    qs(a, st, pi - 1)
    qs(a, pi + 1, end)

if __name__ == "__main__":
    a = [6, 21, 4, 5, 16, 6]
    qs(a, 0, len(a)-1)
    print(f"Sorted array {a}")
