# question link - https://www.codechef.com/CCSTART2/problems/ISBOTH


N = int(input())

def checkNum(num):
    
    if num%5 ==0 and num%11 == 0:
        print("BOTH")
    elif num%5 == 0:
        print("ONE")   
    elif num%11 == 0:
        print("ONE")    
    else: 
        print("NONE")
        

checkNum(N)
