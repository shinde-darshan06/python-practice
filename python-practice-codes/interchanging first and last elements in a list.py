# interchange first and last elements in a list

# method 1:
def swap_lst(lst):
    temp=lst[0]
    size=len(lst)
    lst[0]=lst[size-1]
    lst[size-1]=temp
    
    return lst
    
lst = [12, 35, 9, 56, 24]

print("new list:",swap_lst(lst))

# method 2:
def swap_lst(lst):
    lst[0],lst[-1]=lst[-1],lst[0]
    
    return lst
    
lst = [12, 35, 9, 56, 24]

print(swap_lst(lst))

# method 3: Using * operand
def swap_lst(lst):
    new_lst=[]
    start, *middle, end = lst
    new_lst=[end, *middle, start]
    
    return new_lst
    
lst = [12, 35, 9, 56, 24]

print("new list:",swap_lst(lst))

