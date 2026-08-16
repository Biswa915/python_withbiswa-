# Nested Loops
# A nested loop is a loop inside another loop. The inner loop completes all its
# iterations for every single iteration of the outer loop.
# q1
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 

for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()
