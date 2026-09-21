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


# Question 51: 
# Given a list of numbers, write Python code using a loop to find and print the
# largest element. Do not use the built-in max() function.

nums = [6, -5,4, 2, 10, 91, -75, 49, 9]

maxi=float("-inf")
for num in nums:
     if num>maxi:
          maxi=num
print(f"maximum number is = {maxi}")

# Question 52: 
# Write a program that takes a list and a target number. Use a loop to determine if
# the target number exists in the list. Do not use the in operator.

num=[10,-19,2,3,29,9,27,18,20,21]
def biswa_target(list,target):
     for num in list:
         if num==target:
              return True
     return False
     
print(biswa_target(num,8))
print(biswa_target(num,27))

