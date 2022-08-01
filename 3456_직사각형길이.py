import sys

sys.stdin = open("3456_직사각형길이.txt","r")

T = int(input())

for i in range(1,T + 1):
    LLEN = list(map(int,input().split()))
    result = 0

    if LLEN.count(LLEN[0]) == 3 :
        result = LLEN[0]
    else :
        if LLEN.count(max(LLEN)) == 1 :
            result = max(LLEN)
        else :
            result = min(LLEN)

    print('#%d %d' % (i, result))