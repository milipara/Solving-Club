import sys

sys.stdin = open("1228_암호문1.txt","r")

T = 10

for t in range(1,T+1):
    origin_len = int(input())
    origin_list =list(map(int,input().split()))

    command_len = int(input())
    command_list = input().split()
    i=0
    while i < len(command_list):
        command = command_list[i]

        if command == "I":
            x = int(command_list[0+1])
            y = int(command_list[i+2])
            number_list = command_list[i+3:i+3+y]

            for number in number_list[::-1]:
                origin_list.insert(x, int(number))
        i = i + 1
    print(f"#{t}",*origin_list[:10])