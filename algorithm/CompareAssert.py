import random
from SortAlgorithm import *

def generate_list(max_value, max_length):
    new_list = []
    for i in range(max_length):
        obj = random.randint(0, max_value)
        new_list.append(obj)
    return new_list


# sample 抽样，max_length < len(range(max_value))
def generate_list_with_random_sample(max_value, max_length):
    return random.sample(range(max_value), k=max_length)


# 推荐
def generate_list_with_random_choices(max_value, max_length):
    return random.choices(range(max_value), k=max_length)


if __name__ == '__main__':
    # print(generate_list(10, 10))
    # print(generate_list_with_random_sample(20, 10))
    # print(generate_list_with_random_choices(30, 50))
    lst = generate_list_with_random_sample(15, 10)
    lst1 = lst[:]
    lst2 = lst.copy()
    print('lst:', lst)
    selection_sort(lst)
    print(lst)

    print('lst1', lst1)
    bubble_sort(lst1)
    print(lst1)

    print('lst2', lst2)
    insertion_sort(lst2)
    print(lst2)