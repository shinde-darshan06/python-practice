# Capital indexes

# METHOD 1:
def capital_indexes(str):
	for i in str:
		print(i)
		
str="HeLlO"
print(capital_indexes(str))


# METHOD 2:

def capital_indexes(str):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(str):
        if l in upper:
            result.append(i)
    return result
    
str="HeLlO"
print(capital_indexes(str))

