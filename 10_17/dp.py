"""
동적 계획법(Dynamic Programming, DP)의 개념
동적 계획법(DP)은 복잡한 문제를 작은 하위 문제들로 나누어 해결한 결과를 저장해두고, 이를 재사용하여 전체 문제를 해결하는 방법이다.

핵심 개념
    하위 문제 분할(Subproblem Decomposition):
    DP는 큰 문제를 여러 개의 작은 하위 문제로 나누어 해결합니다. 이 하위 문제들은 서로 중복될 수 있으며, 각 하위 문제는 독립적으로 해결됩니다.

    메모이제이션(Memoization):
    하위 문제의 결과를 저장하여, 동일한 문제가 다시 나타났을 때 다시 계산하지 않고 저장된 결과를 사용합니다. 이를 통해 계산 시간을 절약할 수 있습니다.

    최적 부분 구조(Optimal Substructure):
    문제의 최적해가 그 하위 문제들의 최적해로 구성될 수 있어야 합니다. 즉, 문제를 작은 단위로 나누었을 때도 각각의 하위 문제에서 최적의 해를 구하는 것이 중요합니다.

    중복되는 하위 문제(Overlapping Subproblems):
    하위 문제들이 중복되어 여러 번 계산될 때, DP는 이를 저장해두고 재사용하여 효율을 높입니다. 이 점에서 모든 하위 문제들이 독립적인 분할정복 알고리즘과 구별됩니다.

DP의 접근 방법
    탑다운(Top-Down) 방식:
    주어진 문제를 상위에서 시작하여 작은 하위 문제로 쪼개어 나가는 방식입니다.
    재귀와 메모이제이션을 사용하여 각 하위 문제를 해결합니다.

    바텀업(Bottom-Up) 방식:
    작은 하위 문제부터 차례대로 해결해 나가며, 최종적으로 큰 문제를 해결하는 방식입니다.
    이 방식은 보통 반복문을 통해 구현되며, 메모이제이션이 아닌 테이블을 사용하여 결과를 저장합니다.


"""


def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]


# 바텀업 방식의 DP
def fibonacci_bottom_up(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


if __name__ == "__main__":
    print(fibonacci(10))  # 결과: 55
    print(fibonacci_bottom_up(10))  # 결과: 55
