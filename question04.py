# question link - https://www.codechef.com/CCSTART2/problems/SECLAR

inp_vals = list(map(int,input().split()))

def findSecondLargest(lst):
    lst.sort()
    return lst[1]

print(findSecondLargest(inp_vals))
    