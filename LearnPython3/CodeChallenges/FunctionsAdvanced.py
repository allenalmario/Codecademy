# 1. First Three Multiples

def first_three_multiples(num):
    print(num * 1)
    print(num * 2)
    print(num * 3)
    return num * 3

print(first_three_multiples(10))
# should print 10, 20, 30, and return 30
print(first_three_multiples(0))
# should print 0, 0, 0, and return 0

# 2. Tip

def tip(total, percentage):
    return (total * percentage) / 100

print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

# 3. Bond, James Bond

def introduction(first_name, last_name):
    intro = last_name + ", "
    intro += first_name
    intro += " "
    intro += last_name
    return intro

print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

# 4. Dog Years

def dog_years(name, age):
    return name + ", you are " + str(age * 7) + " years old in dog years"

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

# 5. All Operations

def lots_of_math(a, b, c, d):
    result1 = a + b
    print(result1)
    result2 = c - d
    print(result2)
    result3 = result1 * result2
    print(result3)
    return result3 % a

print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0