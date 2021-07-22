# question link - https://www.codechef.com/CCSTART2/problems/VALTRI

N = int(input())

def checkBus(num):
    if num%6 == 0 or num%5 == 0:
        print("YES")
    else: 
        print("NO")
        
checkBus(N)