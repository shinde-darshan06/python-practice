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


# Fibonacci series using recursion

num = int(input("enter number for fibonacci series: "))

def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

print("fibonacci series are:")
for i in range(0,num):
    print(fibonacci(i))
