from sys import stdin

def reverse(arr , s, e):
    while s<e:
        arr[s],arr[e] = arr[e],arr[s]
        s += 1
        e -= 1


def rotate(arr, n, d):
    #Your code goes here
    n = len(arr)
    reverse(arr , 0, n-1)
    reverse(arr , 0, n-d-1)
    reverse(arr , n-d, n-1)

'''
def rotate(arr , n, d):
    n = len(arr)
    b = arr[0: d]
    c = arr[d : n]
    c.extend(b)
'''
    

    
    
#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1
