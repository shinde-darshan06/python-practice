# Fibonacci series

first, second = 0,1
num = int(input("enter number: "))
lst = []

for i in range(0, num):
    if i<1:
        result = i
    else:
        result = first + second
        first, second = second, result
    lst.append(result)
    
print("fibonacci series are: ", lst)
