"""
백준 9095번 다이나믹 프로그래밍 문제.
"""

if __name__ == "__main__":

    test_case = int(input())

    for _ in range(test_case):
        N = int(input())
        dp = [0] * (N-1)

        for i in range(1, N+1):
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            elif i == 3:
                dp[i] = 4
            else:
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[N])
