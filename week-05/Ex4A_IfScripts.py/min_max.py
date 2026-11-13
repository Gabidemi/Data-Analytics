a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
c = float(input("Enter a number: "))

if a > b and a > c and b > c:
    print("Your first number is the biggest number")
    print("Your third number is the smallest number")
if a > b and a > c and c > b:
    print("Your first number is the biggest number")
    print("Your second number is the smallest number")
elif b > a and b > c and a > c:
    print("Your second number is the biggest number")
    print("Your third number is the smallest number")
elif b > a and b > c and c > a:
    print("Your second number is the biggest number")
    print("Your first number is the smallest number")
elif c > a and c > b and a > b:
    print("Your third number is the biggest number")
    print("Your second number is the smallest number")
elif c > a and c > b and b > a:
    print("Your third number is the biggest number")
    print("Your first number is the smallest number")
else:
    print("2 or more of your numbers may have the same values")