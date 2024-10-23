"""
퀵 솔트
"""

def quick_sort(unsorted_list: list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list

    pivot = unsorted_list[0]
    low = []
    high = []

    for i in range(1, len(unsorted_list), 1):
        val = unsorted_list[i]
        if val >= pivot:
            high.append(val)
        else:
            low.append(val)

    low_result = quick_sort(low)
    pivot_result = [pivot]
    high_result = quick_sort(high)

    return low_result + pivot_result + high_result


if __name__ == "__main__":
    test_case = [4, 3, 2, 7, 6, 5]
    sorted_array = quick_sort(test_case)
    print("정렬된 배열:", sorted_array)
