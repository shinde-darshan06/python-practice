# swap two elements in a list

# METHOD 1:
def pos_change(lst):
    pos1=int(input("enter first number position to swap: "))
    pos2=int(input("enter second number position to swap: "))
    lst[pos1-1],lst[pos2-1]=lst[pos2-1],lst[pos1-1]
    return lst

lst = [23, 65, 19, 90]
print("List after changing position of elements:",pos_change(lst))

# METHOD 2: Using Inbuilt list.pop() function 

def swap_position(lst, pos1, pos2):
    first_element = lst.pop(pos1)
    second_element = lst.pop(pos2-1)
    
    lst.insert(pos1,second_element)
    lst.insert(pos2, first_element)
    
    return lst
    
lst = [1,2,3,4,5]
pos1, pos2 = 1,3

print(swap_position(lst, pos1-1, pos2-1))

# METHOD 3: Using tuple variable

def swap_position(lst, pos1, pos2):
    
    get = lst[pos1],lst[pos2]
    
    lst[pos2], lst[pos1] = get
    return lst
    
lst = [1,2,3,4,5]
pos1, pos2 = 1,3

print(swap_position(lst, pos1-1, pos2-1))