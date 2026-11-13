dept_code = int(input("Enter a department code - 1, 5, 10, 12, 18, 20: "))
match dept_code:
    case 1:
        print("This is the Marketing department")
    case 5:
        print("This is the Human Resource department")
    case 10:
        print("This is the Accounting department")
    case 12:
        print("This is the Legal department")
    case 18:
        print("This is the IT department")
    case 20:
        print("This is the Customer Relations department")
    case _:
        print("This department code does not exist")

