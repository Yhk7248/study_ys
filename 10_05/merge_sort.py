"""
머지 솔트(합병 정렬), Divide and Conquer
"""


def merge_sort(unsorted_list: list) -> list:
    if len(unsorted_list) < 2:
        return unsorted_list

    mid = len(unsorted_list) // 2
    low_arr = merge_sort(unsorted_list[:mid])
    high_arr = merge_sort(unsorted_list[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


if __name__ == "__main__":
    test_case = [4, 6, 2, 8, -1, 0]
    sorted_array = merge_sort(test_case)
    print("정렬된 배열:", sorted_array)
