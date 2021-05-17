# 1 Append Size
def append_size(lst):
    length = len(lst)
    lst.append(length)
    return lst
print(append_size([23, 42, 108]))

# 2 Append Sum
def append_sum(lst):
    for x in range(0, 3):
        lst.append(lst[-2] + lst[-1])
    return lst
print(append_sum([1, 1, 2]))

# 3 Larger List
def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# 4 More Than N
def more_than_n(lst, item, n):
    # use count function to count the number of times item appears in lst
    if lst.count(item) > n:
        return True
    else:
        return False
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# 5 Combine Sort
def combine_sort(lst1, lst2):
    combined_list = lst1 + lst2
    combined_list.sort()
    return combined_list
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))