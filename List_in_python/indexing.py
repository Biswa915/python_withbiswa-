# Accessing List Elements: Indexing
# Every element in a Python list occupies a specific position, known as its index.
# It's crucial to remember that Python, like many programming languages, uses zero-based indexing.
# This means the first element is at index 0,
# the second at 1, and so forth.

lis=["biswa","guru","deep", 29,75,"datt"]
print(lis[0])
print(lis[3])
print(lis[-2])
print(lis[-5])

n=len(lis)
print(f"last elemat = {lis[n-1]}")


     # update list
lis=["biswa","guru","deep", 29,75,"datt"]

print(f"list={lis}")
lis[2]="mosks"
print(f"list={lis}")

# Create a list of 5 numbers (e.g., [10, 20, 30, 40, 50]). Replace the second and
# fourth elements of this list with the number 0 using indexing.
# Print the updated list.

# num=[10,20,30,40,50]
# num[1]=0
# num[3]=0
# print(num)