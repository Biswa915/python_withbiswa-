# FOR loop
# A for loop is used to iterate over a sequence - a range of numbers, a string, a list,
# and so on. Unlike while, you don't manage a counter manually - Python
# handles it for you.

# for variable in sequence:
# this block runs for each item in the sequence

# Looping over a range of numbers
# for i in range(1, 6):
# print (i)
# Output: 1 2 3 4 5

# print 1 to 10
# for i in range(1, 12):
#     print(i,end=" ") 

#step in for loop
for i in range(1, 12,4):
     print(i,end=" ") 
    
# loop revers and divisible cheek
for i in range(100,0,-1):
    if i % 2==0 and i %3==0:
        print(i, end=" ")
