# Accessing List Elements: Indexing
# Every element in a Python list occupies a specific position, known as its index.
# It's crucial to remember that Python, like many programming languages, uses zero-based indexing.
# This means the first element is at index 0,
# the second at 1, and so forth.

lis=["biswa","guru","deep", 29,75,"datt"]
# print(lis[0])
# print(lis[3])
# print(lis[-2])

n=len(lis)
print(f"last elemat = {lis[n-1]}")


     # update list
lis=["biswa","guru","deep", 29,75,"datt"]

print(f"list={lis}")
lis[2]="mosks"
print(f"list={lis}")
