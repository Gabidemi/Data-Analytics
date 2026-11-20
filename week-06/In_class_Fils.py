#Name: Gbolahan Abidemi
#Date: 11/19/2026
#Reading and writing files


# Write to a file
with open("Students.txt","w") as file:
    file.write('Alice\n')
    file.write('Bob\n')

# Reading from a file
with open("Students.txt", "r") as file:
    content = file.read()
    print(content)

# Another Example

# Writing to a file
with open("Example.txt", "w") as file:
    file.write('Hello World\n')

# Reading from the file
with open("Example.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to the end of a file
with open("Example.txt", "a") as file:
    file.write('\n new line added')

# opening a file as read and write
with open("Example.txt", "r+") as file:
    content = file.read()
    print(content)


try:
    with open("Test.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File NOT FOUND")
finally:
    print("Program Ran successfully")