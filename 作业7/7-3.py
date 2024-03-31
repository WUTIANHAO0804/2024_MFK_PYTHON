def bin_search(lst):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = int(lst[mid])
        if mid_value == 1415:
            return mid
        elif mid_value < 1415:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # 如果列表中没有1415年的文档，返回-1