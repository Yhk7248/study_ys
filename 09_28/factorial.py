def factorial_recursive(n):
    # n이 0 또는 1인 경우 1을 반환 (종료 조건)
    if n == 0 or n == 1:
        return 1
    # n! = n * (n-1)!
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    number = 5
    print(f"{number}! = {factorial_recursive(number)}")
