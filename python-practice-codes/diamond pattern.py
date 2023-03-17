# diamond pattern with * 

value = int(input("Enter value: "))
for i in range(value):
    print(' '*(value-1-i)+'* '*(i+1))
for i in range(value-1):
    print(' '*(i+1)+'* '*(value-i-1))