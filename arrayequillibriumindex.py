from sys import stdin

def arrayEquilibriumIndex(arr,n) :
    #Your code goes here
    #n = len(arr)
    #for total sum
    ts = sum(arr)
    ls = 0
    index = 0
    while index < len(arr):
        rs = ts-ls-arr[index]
        if rs == ls:
            return index
        ls = ls +arr[index]
        index = index + 1
    return -1
