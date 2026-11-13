x = 100
y = 20
z = x//y

if z == 5:
    print('X divided by Y is 5')
    x = 1
else:
    print('Are the variables set up correctly?')

if (x * y) == y:
    print('Now X times Y is Y')
    x = 10
else:
    print(f"whoops, X equals: {x}")

if x < y:
    print("X is less than Y")
    x = x*2
else:
    print("uh oh, X is not less than Y")

if x > y:
    print("How is X greater than Y??")
else:
    print("X is NOT greater than Y")

print(f"The final value of X is: {x} and the final value of Y is: {y}")
