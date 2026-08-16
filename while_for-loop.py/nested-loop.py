# Nested Loops
# A nested loop is a loop inside another loop. The inner loop completes all its
# iterations for every single iteration of the outer loop.
# q1
'''''
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5
''''''''' 

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# q2
"""""
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""""
# for i in range(6,0,-1):
#     for j in range(1,6):
#         print(i, end=" ")
#     print()

# Q3
'''''
*
* *
* * *
* * * *
* * * * *
'''
# for i in range  (1,6):
#     for j in range(1,i+1):
#      print("*",end=" ")
#     print() 

# q4
''''
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5 
'''
# for i in range(1,6):
#     for j in range(1,i+1):
#      print(j, end=" ")
#     print()    
# q5
''''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
# n=int(input("enter your number="))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#      print(j,end=" ")
#     print() 

# q6
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()