from math import e
''' This code will tell you what percent of an element has remain after 
 x years with half life y, where x and y and user inputs '''


half_life = float(input("Enter Half Life here: "))   # Half life Y 
target_time = float(input("Enter the years of which you want to find out what % of the element remains: "))
# ^ x years

def average(a,b):
    return (a+b)/2

# Just a mathamathical formula
def pert(P,r,t):
    return P*e**(r*t)

def bin_search(f,lower,upper,target):
    for i in range(40):
        avg = average(lower,upper)
        guess = f(1,avg,half_life)
        if guess == target:
            return guess
        if guess > target:
            upper = avg
        else:
            lower = avg
    return avg

# The above commands, except pert, have been defined and explained in my previous code

# We use binary search to find the rate of decay
rate_of_decay = bin_search(pert,-20,0,0.5)

# And then we plug in the rate of decay into the pert formula for our answer
print(str(pert(1,rate_of_decay,800)*100) + "% remains after " + str(target_time) + " years" )
