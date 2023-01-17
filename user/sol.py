import sys
try :
	sys.stdin = open("A.inp", "r")
	sys.stdout = open("A.out", "w")
except :
	sys.stdin = sys.__stdin__
	sys.stdout = sys.__stdout__
 
n, m = map(int, input().split())
s = input()
 
cnt = 0
for ch in s :
    if (ch.isdecimal()) :
        m -= int(ch)
    elif (ch == 'A') :
        m -= 1
    elif (ch != '*') :
        m -= 10  
    else :
        cnt += 1
 
ans = []
while (m > 0 and cnt > 0) :
    if (m < cnt) :
        break
    k = min(m - cnt + 1, 10, m)
    m -= k
    ans.append(k)
    cnt -= 1
 
res = ""
if (m == 0 and cnt == 0) :
    for i in range(n) :
        if (s[i] == '*') :
            x = ans.pop()
            if (x == 10) :
                res += 'T'
            elif (x == 1) :
                res += 'A'
            else :
                res += str(x)
        else :
            res += s[i]
    print("YES\n" + res)
else :
    print("NO")