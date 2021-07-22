# question link - https://www.codechef.com/CCSTART2/problems/TRIVALCH
import math



triangle_lengths = list(map(int,input().split()))

a,b,c = triangle_lengths

def isTriangle(a,b,c):
    if a + b > c and b + c > a and c + a > b:
        return "YES"
    
    return "NO"

print(isTriangle(a,b,c))