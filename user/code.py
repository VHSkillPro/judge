n, S = map(int, input().split())
 
str = input()
ans = 0
cntJoker = 0
for i in range(n):
    if (str[i] == "*"):
        cntJoker += 1
        continue
    if str[i] == 'J' or str[i] == 'Q' or str[i] == 'K' or str[i] == 'T':
        ans += 10
    elif str[i] == 'A':
        ans += 1
    else:
        ans += int(str[i])
if cntJoker == 0:
    if S == ans:
        print("YES")
        print(str)
    else:
        print("NO")
    exit(0)
# print(ans, cntJoker)
if ans + cntJoker <= S and ans + cntJoker * 10 >= S:
    print("YES")
else:
    print ("NO")
    exit(0)
ave = (S - ans) // cntJoker
avef = (S - ans) / cntJoker
if ave == avef:
    for i in range(n):
        if (str[i] == '*'):
            if ave == 1:
                print("A", end = "")
            elif (ave == 10) :
                print("J", end = "")
            else:
                print(ave, end = "")
        else:
            print(str[i], end = "")
    exit(0)
j = 0
for i in range(n):
    if str[i] == '*' and cntJoker > 0:
        cntJoker -= 1
        if (cntJoker == 0) :
            if S == 1:
                print("A", end = "")
            elif (S == 10):
                print("J", end = "")
            else:
                print(S, end = "")
            S = 0
            continue
        if (cntJoker * ave != S):
            if ave == 1:
                print("A", end = "")
            elif ave == 10:
                print("J", end = "")
            else:
                print(ave, end = "")
            S -= ave
        else:
            if ave == 0:
                print("A", end = "")
            elif ave + 1 == 10:
                print("J", end = "")
            else:
                print(ave + 1, end = "")
            S -= (ave + 1)
    else:
        print(str[i], end = "")
        if str[i] == "J" or str[i] == "Q" or str[i] == "K" or str[i] == "T":
            S -= 10
        elif str[i] == "A":
            S -= 1
        else:
            S -= int(str[i])
    j += 1