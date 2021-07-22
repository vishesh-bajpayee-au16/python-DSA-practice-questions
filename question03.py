# question link - https://www.codechef.com/CCSTART2/problems/DIFACTRS

N = int(input())

def findFactors(num):
    factorArr = []
    factorCount = 0
    for i in range(1,num+1):
        if num%i == 0:
            factorCount += 1
            factorArr.append(i)
    print(factorCount)
    # print(" ".join(str(x) for x in factorArr))
    print(*factorArr)
            

findFactors(N)