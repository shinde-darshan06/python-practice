# Capital indexes
'''Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0,2,4]. '''


# METHOD 1:
def capital_indexes(str):
    lst = []
    for i in range(len(str)):
        if str[i].isupper():
            lst.append(i)
    return lst


str = "HeLlO"
print(capital_indexes(str))


# METHOD 2:

def capital_indexes(str):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(str):
        if l in upper:
            result.append(i)
    return result


str = "HeLlO"
print(capital_indexes(str))

# Middle letter
'''Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".'''


# METHOD 1:
def mid(str):
    num = len(str)
    x = ""
    if num % 2 == 0:
        return x
    else:
        x = str[num // 2]
        return x

    print(mid("abc"))


# METHOD 2:
def mid(str):
    if len(str) % 2 == 0:
        return ""
    else:
        return (str[len(str) // 2])


str = "abc"
print(mid(str))

# Online status
'''

Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline".

Your function should return the number of people who are online.'''


# METHOD 1:
def online_count(statuses):
    lst = []
    for v in statuses.values():
        if v == "online":
            lst.append(v)
    return len(lst)


statuses = {"Alice": "online", "Bob": "offline", "Eve": "online"}
print(online_count(statuses))


# METHOD 2:
def online_count(people):
    count = 0
    for person, status in people.items():
        if status == "online":
            count += 1
    return count


# Randomness
'''Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.

Calling the function multiple times should (usually) return different numbers.

For example, calling random_number() some times might first return 42, then 63, then 1.'''

import random


def random_number():
    return random.randint(1, 100)


# Type check
'''Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.'''


def only_ints(a, b):
    if type(a) == int and type(b) == int:
        return True
    else:
        return False


print(only_ints("a", 1))

# Double letters
'''The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.'''


# METHOD 1:
def double_letters(str):
    for i in range(len(str) - 1):
        if str[i] == str[i + 1]:
            return True
    return False


str1 = "hello"
str2 = "nono"
print(double_letters(str1))
print(double_letters(str2))


# METHOD 2:
def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i + 1]
        if letter1 == letter2:
            return True
    return False


# Adding and removing dots
'''Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)'''


# method 1:
def add_dots(str):
    str1 = '.'.join(str)
    return str1

def remove_dots(str1):
    str2 = str1.replace(".", "")
    return str2

str = "test"
print(add_dots(str))
print(remove_dots(add_dots(str)))

# method 2:
def add_dots(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")

# pallindrom
num = int(input("enter number: "))
rev, temp = 0, num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if num == rev:
    print("{} is a pallindrom number".format(num))

else:
    print("{} number is not pallindrom".format(num))

# anagram:
# method 1:
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    str1_sorted = sorted(list(str1))
    str2_sorted = sorted(list(str2))

    if str1_sorted == str2_sorted:
        return True
    else:
        return False

print(is_anagram("aba", "baa"))
print(is_anagram("abaa", "baa"))

# method 2:
def is_anagram(str1, str2):
    if len(str1) == len(str2):
        for i in str1:
            if i in str2:
                return True
    return False


print(is_anagram("aba", "baa"))
print(is_anagram("abaa", "baa"))