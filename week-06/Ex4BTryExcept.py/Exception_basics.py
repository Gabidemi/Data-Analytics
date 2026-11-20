# ValueError
try:
    number = int("banana")
except ValueError:
    print("ValueError: Cannot be converted to an integer.")
else:
    print(number)
finally:
    print("Let's try another one...")


# NameError
try:
    m = banana
except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable")
else:
    print(m)
finally:
    print("Let's try another one...")


# TypeError
try:
    result = 5 + "3"
except TypeError:
    print("TypeError: Cannot add an integer and a string.")
else:
    print(result)
finally:
    print("Let's try another one...")


# SyntaxError
try:
    result = exec('print("Hello, world" ')
except SyntaxError:
    print("SyntaxError: The expression is incomplete.")
else:
    print(result)
finally:
    print("Lets try another one...")
