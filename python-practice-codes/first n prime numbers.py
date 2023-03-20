# generate first n prime numbers

num = int(input("enter number value: "))
count = 0
num1 = 2
while True:
    is_prime=True
    for i in range(2, num1//2+1):
        if num1%i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(num1)
        count = count+1
   
    if count == num:
        break
    num1=num1+1
