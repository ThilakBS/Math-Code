'''This code is made to calculate how many years it takes
to make a certain amount of money when it is compounded '''

# The variables below are made so that the user can input their own values

initial_investment = float(input("Enter your Initial Investment: "))
rate = float(input("Enter your growth rate: "))
time_compounded = float(input("Your investment is compounded after ___ days: "))
target_output = float(input("How much movey do you want to end up with: "))
range_lower = float(input("Enter the smallest number of years this could take "))
range_upper = float(input("Enter the largest number of years this could take "))

# the amount fuction is one to calculate after interest is taken into account

def amount(p0,rate,t,comps):
    for i in range(int(t*comps)):
        p0 += p0*rate/comps
    return p0

# Average is a basic function to take an average of 2 numbers

def average(a,b):
    return (a+b)/2

''' binary search is an algorithm made to find a target value by 
constantly taking averages and eventually getting to the target value '''

def bin_search(f,lower,upper,target):
    for i in range(20):
        avg = average(lower,upper)
        guess = f(initial_investment,rate,avg,time_compounded)
        if guess == target:
            return guess
        if guess > target:
            upper = avg
        else:
            lower = avg
    return avg




print("It would take " + str(bin_search(amount,range_lower,range_upper,target_output)) + " years to make $" + str(target_output))

