def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    positive_num = 0
    negative_num = 0
    for num in arr:
        if num > 0:
            positive_num += 1
        if num < 0:
            negative_num += num
    return [positive_num, negative_num]