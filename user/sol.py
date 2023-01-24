n = int(input())
arr = list(map(int, input().split()))

product = 1
for val in arr :
    product *= val
    
def power(base: int, exp: int) -> int :
    ans = 1
    while (exp > 0) :
        if (exp & 1) :
            ans *= base
        exp >>= 1
        base **= 2
    return ans

l, r = 0, max(arr) + 1
while (l + 1 < r) :
    m = (l + r) >> 1
    if (power(m, n) > product) :
        r = m
    else :
        l = m
        
print(r)