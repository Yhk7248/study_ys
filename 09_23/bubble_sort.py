def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 마지막 i개의 요소는 이미 정렬된 상태이므로 확인할 필요 없음
        for j in range(0, n-i-1):
            # 현재 요소와 다음 요소를 비교하여 큰 값을 뒤로 보냄
            if arr[j] > arr[j+1]:
                # 두 요소를 교환
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(array)
    print("정렬된 배열:", sorted_array)
    