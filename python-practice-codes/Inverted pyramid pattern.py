# Inverted pyramid pattern 

rows = int(input("enter number of rows: "))
for i in range(rows):
    print(' '*i + '* '*(rows-i))