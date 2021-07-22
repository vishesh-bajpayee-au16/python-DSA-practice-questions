# question link - https://www.codechef.com/CCSTART2/problems/REVMEE

N = int(input())

int_lst = [int(i) for i in input().split()[:N]]


def reverseList(lst):
    lst.reverse()
    return lst

print(*reverseList(int_lst))

