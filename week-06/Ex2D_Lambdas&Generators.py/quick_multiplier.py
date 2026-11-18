doubler = lambda n: n * 2

print(doubler(8))
print(doubler(-4))
print(doubler("banana"))

tripler = lambda n: n * 3

print(tripler(8))
print(tripler(-4))
print(tripler("banana"))


def multiplier(amount):
    return lambda n: n * amount


quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

print(quadrupler(8))
print(quintupler(8))
print(sextupler(8))
print(septupler(8))
print(octupler(8))
print(nonupler(8))
print(decupler(8))