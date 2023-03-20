# pallindrom

num = int(input("enter number: "))
rev, temp = 0, num
while temp>0:
    digit = temp%10
    rev = rev*10 + digit
    temp = temp//10

if num == rev:
    print("{} is a pallindrom number". format(num))
else:
    print("{} number is not  pallindrom number".format(num))