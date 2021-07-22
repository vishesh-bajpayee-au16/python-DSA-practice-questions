# question link - https://www.codechef.com/CCSTART2/problems/ADDNATRL

N = int(input())


def findSum(num):
    return sum([x for x in range(num+1)])
        
print(        
findSum(N))