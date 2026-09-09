# 1. crating a list
# x=["biswa","moti","guru"]
# print(x)
# print(type(x))

# oparation in list 
# marks=[8,5,7,5,]
# print(marks*5)
# marks=[8,5,7,5,]
# marks1=[1,8,5,7,5,]

# print(marks+marks1)

    #   2.# bulit in function
# len()get length
# mark=[2,6,7,56,7,5]
# print(len(mark))

# min() - Smallest Value
# Returns the smallest item from a list of numbers.
mark=[37,45,56,23,54]
print(min(mark))

# max() - Largest Value
# Returns the largest item from a list of numbers.
mark=[37,45,56, 24,23,54]

print(max(mark))

# sum() - Sum of Elements
# Returns the sum of all numeric elements in the list.
mark=[37,56,45,56, 24,23,54]
print(sum(mark))

# Create Sorted List
# Returns a new list containing all items from the iterable in ascending order. The original list remains
# unchanged.
# mark=[37,56,45,56, 24,23,54]
# new_list=sorted(mark)
# print(f"new list is assending oder={new_list}")
mark=[37,56,45,56, 24,23,54]
new_list=sorted(mark,reverse=True)
print(f"new list is dissending oder={new_list}")