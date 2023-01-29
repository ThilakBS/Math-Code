velocity = float(input("Enter the velocity of the particle: "))
target_height = float(input("Enter the height of the particle of which you want to find the time of (in meters): "))


v = velocity
g = 9.8    # makes sure the code only applies to problems on Earth
h = 0
t = 0

def height(v0, h0, t):
    inc = 0.0005
    v, h = v0, h0
    for i in range(int(t / inc)):
        v -= g * inc
        h += v * inc
    return h


def average(a, b):
    return (a + b) / 2


def bin_search(f, lower, upper, target):
    for i in range(40):
        avg = average(lower, upper)
        guess = f(29, 0, avg)
        if guess == target:
            return avg
        if guess < target:
            upper = avg
        else:
            lower = avg
    return avg


print( "It takes "+ str(bin_search(height, 0, 10000, target_height)) + " seconds for the particle to reach " + str(target_height) + " meters" )
