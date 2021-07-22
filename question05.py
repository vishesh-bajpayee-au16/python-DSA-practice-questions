# question link - https://www.codechef.com/CCSTART2/problems/RNGEODD


inp_val = list(map(int,input().split()))

L = inp_val[0]
R = inp_val[1]

def getOddNums(l,r):
    odd_num_arr = []
    for i in range(l,r+1):
        if i%2 != 0:
            odd_num_arr.append(i)
    print(*odd_num_arr)
    

getOddNums(L,R)