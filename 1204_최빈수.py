import sys

sys.stdin = open("1204_최빈수.txt","r")

T = int(input())
j = int(input())

for i in range(1,T+1):
    S = int(input())
    number = list(map(int,input().split()))
    score_check = max(number)
    for j in number:
        score_check[j] += 1


    print(str(i))