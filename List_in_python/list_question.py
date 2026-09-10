# Question 49: "
# Favourite Movies Create a list of 5 of your favourite movies. Print the first, last,
# and middle movie from your list using both positive and negative indexing where appropriate.
lis=["danus","monye","game of throne","stanger think","majo bou"]
n=len(lis)
print(f"fast movie = {lis[n-5]}")
print(f"last movie = {lis[n-1]}")
print(f" middel move = {lis[n//2]}")
    


# Question 50: 
# Number Replacement Create a list of 5 numbers (e.g., [10, 20, 30, 40, 50]). 
# Replace the second and fourth elements of this list with the number 0 using indexing. Pr

lis=[10, 20, 30, 40, 50]

lis[1]=0
lis[3]=0
print(f"replace the list second and fourth = {lis}")