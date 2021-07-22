# question link - https://www.codechef.com/CCSTART2/problems/BUYPLSE

# taking value in one line 
# format = [a,b,x,y]

input_vals = list(map(int,input().split()))

def cost_of_pens(count,price):
    return count*price

def cost_of_pencils(count,price):
    return count*price

def total_price():
    return (cost_of_pens(input_vals[0],input_vals[2]) + cost_of_pencils(input_vals[1],input_vals[3]))

print(total_price())