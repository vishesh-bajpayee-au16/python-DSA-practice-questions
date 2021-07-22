# question link - https://www.codechef.com/CCSTART2/problems/SQALPAT

N = int(input())
constant = 5 
pair_count = N//2

def arr_i(pair_count):
    arr_i = []
    for i in range(pair_count):
        arr_i.append(i)
    
    return arr_i


def arr_j(pair_count,arr_i, constant):
    arr_j = []
    for j in range(pair_count):
        if j == 0:
            arr_j.append(arr_i)
        arr_j.append([x*10 for x in arr_j[arr_j - 1]])
        
    return arr_j



print(arr_j(pair_count,arr_i(pair_count),10))        
    
