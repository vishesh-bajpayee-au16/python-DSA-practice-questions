# question link - https://www.codechef.com/LRNDSA01/problems/LAPIN


def input_arr():
    T = int(input())
    input_str_arr = []
    for i in range(T):
        input_str_arr.append(input())
    
    return input_str_arr

def check_lapindrome(str):
    ans_arr = []
    if len(str)%2 == 0:
        midpoint = len(str)//2
        if str[:midpoint] == str[midpoint:]:
            ans_arr.append("YES")
    return ans_arr

print(check_lapindrome(input_arr()))