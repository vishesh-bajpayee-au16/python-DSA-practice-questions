# question link - https://www.codechef.com/CCSTART2/problems/ANGTRICH

angle_lst = list(map(int,input().split()))

def check_if_triangle(lst):
    if sum(lst) == 180:
        print("YES")
    else:
        print("NO")
        

check_if_triangle(angle_lst)