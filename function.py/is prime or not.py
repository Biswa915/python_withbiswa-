def is_prime(num):
    count= 0
    for i in range(1, num + 1):
        if num % i == 0:
            count =count+1
        elif count == 2:
         return True
    return False
        
    
print(is_prime(17))
print(is_prime(10))

