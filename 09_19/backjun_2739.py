# https://www.acmicpc.net/problem/2739

n = int(input())

for i in range(n, 10):
    for j in range(1, 10, 2):
        print(i, '*', j, '=', i*j)
