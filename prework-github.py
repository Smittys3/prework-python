# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_USERNAME")


hello_name(user_name="hello_USERNAME")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

# def first_odds():
for first_odds in range(1, 100):
    if first_odds % 2 != 0:
        print(first_odds)
    first_odds = 0
    while first_odds < 100:
        first_odds += 1
        if first_odds % 2 == 0:
            continue
print(first_odds)


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below.

# def max_num_in_list(a_list):
num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(num1))


# Question 4
# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be boolean Type (true/false).

# def is_leap_year(a_year):
is_leap_year = 1900
if (is_leap_year % 400 == 0) and (is_leap_year % 100 == 0):
    print("True!")
elif (is_leap_year % 4 == 0) and (is_leap_year % 100 != 0):
    print("False")
else:
    print("False")


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.

# def is_consecutive(a_list):
