# 快排 分治法
def quicksort(array):
    #递归出口
    if len(array) < 2:
        return array
    else:
        pivot_index = 0 # 第一个元素最为主元
        pivot = array[pivot_index]
        less_part = [
            i for i in array[pivot_index+1:] if i <= pivot
        ]
        big_part = [
            i for i in array[pivot_index+1:] if i > pivot
        ]
    return quicksort(less_part) + [pivot] + quicksort(big_part)










































