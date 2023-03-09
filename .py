
def max2(a, b):
    if a >= b:
        return a
    else:
        return b
def max3(a,b,c):
    return max2(max2(a,b),c)
# Driver code
a = int(input())
b = int(input())
c=  int(input()) 
print(max3(a, b,c))
