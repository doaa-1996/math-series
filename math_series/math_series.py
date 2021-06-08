# 0, 1, 1, 2, 3, 5, 8, 13, ...
# 2, 1, 3, 4, 7, 11, 18, 29, ..


def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)       


print(fibonacci(0))        
print(fibonacci(1))        
print(fibonacci(2))        
print(fibonacci(3))      
print(fibonacci(4))      



def lucas(n):
    if n==0:
        return 2
    if n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)    

print(lucas(0))        
print(lucas(1))        
print(lucas(2))        
print(lucas(3))        
print(lucas(4))  


# def sum_series (x,y=0,z=1):
#     if y==0 and z==1:
#         return fibonacci(x)
#     if y==2 and z==1:
#         return lucas(x)
#     else:
#         return  sum_series(x - 1, y, z) + sum_series(x - 2, y, z)   



def sum_series(n,x=0,y=1):
    if n==0:
        return x
    if n==1:
        return y
    return sum_series(n-1,x,y)+sum_series(n-2,x,y)


print(sum_series(0))
print(sum_series(1))
print(sum_series(2))
print(sum_series(3))



print(sum_series(0,2,1))
print(sum_series(1,2,1))
print(sum_series(2,2,1))
print(sum_series(3,2,1))

print(sum_series(0,7,12))
print(sum_series(1,7,12))
print(sum_series(2,7,12))
print(sum_series(3,7,12))
