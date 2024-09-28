def quick_sort(arr):
    # 리스트의 길이가 1 이하인 경우 정렬이 필요 없으므로 그대로 반환
    if len(arr) <= 1:
        return arr

    # 기준(pivot)을 리스트의 첫 번째 요소로 설정
    pivot = arr[0]
    # 기준보다 작은 요소들로 구성된 리스트
    less = [x for x in arr[1:] if x <= pivot]
    # 기준보다 큰 요소들로 구성된 리스트
    greater = [x for x in arr[1:] if x > pivot]

    # 재귀적으로 less와 greater를 정렬하고, 기준을 가운데에 둠
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 10, 90]
    sorted_array = quick_sort(array)
    print("정렬된 배열:", sorted_array)
