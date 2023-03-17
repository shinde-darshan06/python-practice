# Write a program in Python to check given number is prime or not.


num = int(input("enter number: ")
if num<=1:
    print("{} is not prime number".format(num))
else:
    is_prime = True
    for i in range(2,num//2+1):
            if num%i==0:
                is_prime=False
    if is_prime == True:
        print("{} is prime number".format(num))
    else:
        print("{} is not prime number".foramt(num))