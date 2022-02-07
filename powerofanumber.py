def power(x, n):
    # Please add your code here
    pass
    if  n ==0:
        return 1
    small_power = power(x,n//2)
    if n%2 == 0:
        return small_power*small_power
    else:
        return x*small_power*small_power

    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
