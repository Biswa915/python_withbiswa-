num=[10,25,33,9,17,20,71,42,55,24,27]
n=len(num)
# i=0
# while i <=n-1:
#     print(num[i], end=" ")
#     i +=1

# count=0
# while i <=n-1:
#     if num [i] %2==0:
#         count +=1
#     i+=1
# print(count)

# i=n-1
# while i>=0:
#     print(num[i],end=" ")
#     i-=1

total=0
for i in range(0,n):  
     total= total + num[i]
print(total)