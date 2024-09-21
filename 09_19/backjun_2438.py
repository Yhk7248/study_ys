# https://www.acmicpc.net/problem/2438

inp = int(input())
for i in range(1,(inp+1)):
    print("*" * i)


for i in range(1, (inp+1)):
    s = ''
    for j in range(1, i+1):
        s += '*'
    print(s)