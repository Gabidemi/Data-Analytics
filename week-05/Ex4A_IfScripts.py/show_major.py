student_name = input("Enter your name: ")
print("Major List: BIOL, CSCI, ENG, HIST, MKT")
student_major = input("What is the code of the Major on your Schedule?: ")

if student_major == 'BIOL':
    print("Your Major is Biology")
    print("Office Location: Science Bldg, Room 310")
elif student_major == 'CSCI':
    print("Your Major is Computer Science")
    print("Office Location: Sheppard Hall, Room 314")
elif student_major == 'ENG':
    print("Your Major is English")
    print("Office Location: Kerr Hall, Room 201")
elif student_major == 'HIST':
    print("Your Major is History")
    print("Office Location: Sheppard Hall, Room 114")
elif student_major == 'MKT':
    print("Your Major is Marketing")
    print("Office Location: Westly Hall, Room 310")
else:
    print("<Unknown>")
    




