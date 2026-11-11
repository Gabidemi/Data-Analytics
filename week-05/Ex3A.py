# Description:  This script tests various numeric 
#               conversion techniques
# Author: Gbolahan Abidemi

a = "  101.1 "
b = '55'
c = "403 Stevens" 
d = 'Number 5   '

# conversion for a
# aInt = int(a) ValueError: invalid literal for int() with base 10: '   101.1'
aFloat = float(a)
aIntFloat = int(float(a))
aSlice = str(a[2:])
aStrip = a.strip()

print('-' * 20)
print('This is for variable A')
print('-' * 20)
print(aFloat, type(aFloat))
print(aIntFloat, type(aIntFloat))
print(aSlice, type(aSlice))
print(aStrip, type(aStrip))

# conversion for b
bInt = int(b) 
bFloat = float(b)
bSlice = int(b[0:])

print('-' * 20)
print('This is for variable B')
print('-' * 20)
print(bInt, type(bInt))
print(bFloat, type(bFloat))
print(bSlice, type(bSlice))

# conversion for c 
# cInt = int(c) ValueError: invalid literal for int() with base 10: '403 Stevens'
# cFloat = float(c) ValueError: could not convert string to float: '403 Stevens'
cSlice = int(c[0:3])

print('-' * 20)
print('This is for variable C')
print('-' * 20)
print(cSlice, type(cSlice))

# conversion for d
# dInt = int(d) ValueError: invalid literal for int() with base 10: 'Number 5   '
# dFloat = float(d) ValueError: could not convert string to float: 'Number 5   '
dSlice = int(d[7:8])
dStrip = d.strip()

print('-' * 20)
print('This is for variable D')
print('-' * 20)
print(dSlice, type(dSlice))
print(dStrip, type(dStrip))