# Euler's method is a way of finding y by slowly increasing the value of x by dx also known as delta x 


def euler(x0, y0, final_x, dx):  # dx is the change in x
    x, y = x0, y0
    while x < final_x:  # It has to be < instead of == in case that x>final_x and forces the code to run forever
        dy = x + y ** 2  # the change in y
        x += dx  # incrementation of x
        y += dx * dy  # incrementation of
    return y


# Allows user to be able to add their own data points go through the Euler's Method function
xi = int(input("Enter your initial x value: "))
yi = int(input("Enter your initial y value: "))
xf = int(input("Enter your final x value: "))
delta_x = int(input("Enter the increments that x increases by:  "))

print("Final y value is: "+ str(euler(xi, yi, xf, delta_x)))
