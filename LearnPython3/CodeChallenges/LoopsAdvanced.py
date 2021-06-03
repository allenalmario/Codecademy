# 1. Larger Sum

def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for num in lst1:
        sum1 += num
    for num in lst2:
        sum2 += num
    if sum1 >= sum2:
        return lst1
    else:
        return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))

# 2. Over 9000

def over_nine_thousand(lst):
    sum = 0
    if len(lst) == 0:
        return 0
    for num in lst:
        sum += num
        if sum > 9000:
            return sum
    return sum

print(over_nine_thousand([8000, 900, 120, 5000]))

# 3. Max Num

def max_num(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max

print(max_num([50, -10, 0, 75, 20]))

# 4. Same Values

def same_values(lst1, lst2):
    new_list = []
    for num in range(0, len(lst1)):
        if lst1[num] == lst2[num]:
            new_list.append(num)
    return new_list

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# 5. Reversed List

def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))