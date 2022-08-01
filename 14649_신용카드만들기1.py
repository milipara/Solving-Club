import sys

sys.stdin = open("14649_신용카드만들기1.txt","r")

T = int(input())

for i in range(1,T+1):
    print("#%d" , % (i))