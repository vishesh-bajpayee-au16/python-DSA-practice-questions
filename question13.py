# https://www.codechef.com/CCSTART2/problems/EXTRICHK

side_length_arr = list(map(int,input().split()))

def checkTriangle(lst):
    lst_set = set(lst)
    if len(lst_set) == 1:
        print(1)
    elif len(lst_set) == 2:
        print(2)
    elif len(lst_set) == 3:
        print(3)
    else:
        print(-1)
        

checkTriangle(side_length_arr)