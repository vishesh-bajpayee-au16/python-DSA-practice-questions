# question link - https://www.codechef.com/CCSTART2/problems/FINDMELI

int_vals = list(map(int,input().split()))
N = int_vals[0]
K = int_vals[1]

n_intigers_lst = [int(i) for i in input().split()[:N]]

def if_k_exists(lst, k):
    if k in lst:
        return 1
    else:
        return -1
        
print(if_k_exists(n_intigers_lst,K))