name_1 = "PRIYA SHARMA" 
name_2 = "bob NGUYEN" 
name_3 = "LaTonya Williams" 
salary_1 = "$82,500" 
salary_2 = "$74,000" 

# Converting each name to lower case
name_1 = name_1.lower()
name_2 = name_2.lower()
name_3 = name_3.lower()

print('-' * 20)
print("Lowercase testing")
print('-' * 20)

print(name_1)
print(name_2)
print(name_3)

# Converting each name to title case
name_1 = name_1.title()
name_2 = name_2.title()
name_3 = name_3.title()

print('-' * 20)
print("Title Case Testing")
print('-' * 20)

print(f'{name_1}\n{name_2}\n{name_3}')

# Replacing the $ in the salaries
print('-' * 20)
print("Salary Testing")
print('-' * 20)

print(salary_1.replace('$', ''), type(salary_1.replace('$', '')))
print(salary_2.replace('$', ''), type(salary_2.replace('$', '')))
# Both must be ints or floats and replace the commas to do mathematical operations

# Replacing the $ and , and making it an int
salary_1 = salary_1.replace('$','')
salary_1 = salary_1.replace(',','')
salary_1 = int(salary_1)
print('-' * 20)
print("Casting Testing")
print('-' * 20)

print(salary_1, type(salary_1))