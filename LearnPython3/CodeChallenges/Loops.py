# 1. Divisible By Ten

def divisible_by_ten(nums):
    counter = 0
    for num in nums:
        if num % 10 == 0:
            counter += 1
    return counter

print(divisible_by_ten([20, 25, 30, 35, 40]))

# 2. Greetings

def add_greetings(names):
    newList = []
    for name in names:
        greeting = "Hello, " + name
        newList.append(greeting)
    return newList

print(add_greetings(["Owen", "Max", "Sophie"]))

# 3. Delete Starting Even Numbers

def delete_starting_evens(lst):
    while(len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# 4. Odd Indicies

def odd_indices(lst):
    new_list = []
    for num in range(0, len(lst)):
        if num % 2 == 1:
            new_list.append(lst[num])
    return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))

# 5. Exponents

def exponents(bases, powers):
    new_list = []
    for base in bases:
        for power in powers:
            new_list.append(base ** power)
    return new_list

print(exponents([2, 3, 4], [1, 2, 3]))