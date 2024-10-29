
if __name__ == "__main__":
    N = int(input())
    score = [0]

    for i in range(N):
        score_stone = int(input())
        score.append(score_stone)

    dp = [0] * 301

    if N > 0:
        dp[1] = score[1]
    if N > 1:
        dp[2] = score[1] + score[2]
    if N > 2:
        dp[3] = max(score[1] + score[3], score[2] + score[3])

    for i in range(4, N+1):
        dp[i] = max(score[i] + score[i-1] + dp[i-3], score[i] + dp[i-2])

    print(dp[N])
