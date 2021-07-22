# question link - https://www.codechef.com/CCSTART2/problems/SUMEVOD

N = int(input())


def get_odd_num(count):
    odd_arr = []
    for  i in range(count*2):
        if i%2 != 0:
            odd_arr.append(i)
    
    return sum(odd_arr[:count])
            

def get_even_num(count):
    even_arr = []
    for  i in range(count*2):
        if i%2 == 0:
            even_arr.append(i)
    
    return sum(even_arr[:count])
            

def answer_func(odd,even):
    ans_arr = [odd,even]
    print(*ans_arr)
    
answer_func(get_odd_num(N),get_even_num(N))