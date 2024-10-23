"""
DP: 다이나믹 프로그래밍

연산 횟수를 줄이고, 미리 계산해 둔 값들을 이용해 최적의 값을 찾는 기법

1. 재귀함수를 이용한 알고리즘들과의 차이점
    재귀함수는 반복된 같은 연산을 반복할 가능성이 있으므로 최적화 되어있지 않다.

2. DP 특징
    1. 메모리제이션을 이용해서 이전에 계산해서 기억하고 있던 값들을 재활용한다.
    2. 같은 연산을 하지 않음으로써 중복 연산이 줄어든다.
    3. 반복 연산이 등장한다.

3. DP 는 기억을 이용한 알고리즘
    정형화된 문제 유형이 없고 메모리제이션 기법을 사용하는 모든 문제들을 DP를 이용하여 풀 수 있다.
    DP식 문제 풀이법을 받아들이는 식으로 학습해야한다.

"""

def max_path_sum(triangle):
    # 맨 아래 행을 초기화
    dp = triangle[-1].copy()

    # 아래 행부터 위로 올라가며 계산
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + max(dp[j], dp[j + 1])

    # 맨 위의 최대 합 반환
    return dp[0]


if __name__ == "__main__":
    triangle = [
        [7],
        [3, 8],
        [8, 1, 0],
        [2, 7, 4, 4],
        [4, 5, 2, 6, 5]
    ]
    print(max_path_sum(triangle))
