# question link - https://www.codechef.com/LRNDSA01/problems/FLOW007


def input_list():
    T = int(input())
    arr = []
    for _ in range(T):
        inp = int(input())
        arr.append(inp)
    return arr
           
def reverseNumber(num):
   reverser_num = "".join(list(reversed(str(num))))
   return reverser_num

def reverse_arr(lst):
    reversed_num_arr = []
    for i in lst:
       reversed_num_arr.append(reverseNumber(int(i)))
    
    return "\n".join(reversed_num_arr)

       
print(reverse_arr(input_list()))

