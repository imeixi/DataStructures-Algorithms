def swap(_list, i, j):
    tmp = _list[i]
    _list[i] = _list[j]
    _list[j] = tmp


# 选择排序 时间复杂度 O(N^2)
def selection_sort(_list):
    if _list is None or len(_list) < 2:
        return
    for i in range(0, len(_list)):
        min_index = i
        for j in range(i+1, len(_list)):
            if _list[j] < _list[min_index]:
                min_index = j
        swap(_list, i, min_index)


# 冒泡排序 时间复杂度 O(N^2)
def bubble_sort(_list):
    if _list is None or len(_list) < 2:
        return
    for i in range(0, len(_list)):
        for j in range(0, len(_list)-i-1):
            if _list[j] > _list[j + 1]:
                swap(_list, j, j + 1)


# 插入排序 时间复杂度 O(N^2)，时间复杂度与数据状况有关
def insertion_sort(_list):
    if _list is None or len(_list) < 2:
        return
    # 0 ~ 0 有序
    # 0 ~ i 有序
    for i in range(1, len(_list)):
        for j in range(i-1, -1, -1):
            if _list[j] > _list[j + 1]:
                swap(_list, j, j + 1)


