from sys import stdin


def findDuplicate(arr, n) :
    #Your code goes here
     arraysum = sum(arr)
     a = ((n-2)*(n-1))//2
     ans = arraysum-a
     return ans



