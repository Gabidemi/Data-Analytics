pay_rate = float(input("How much are you paid per hour?: "))
hours_worked = float(input("How many hours did you work this week?: "))
gross_pay = pay_rate * hours_worked
Weeks = 52
annual_pay = gross_pay * Weeks

if hours_worked > 40:
    print("Exceeded 40 hours, Overtime pay included")
    print("These are your hours worked: ", hours_worked)
    print("This is your weekly pay: ", gross_pay)
    print("This is your annual pay: ", annual_pay)
    pay_rate = pay_rate * 1.5
else:
    print("No Overtime pay")
    print("These are your hours worked: ", hours_worked)
    print("This is your weekly pay: ", gross_pay)
    print("This is your annual pay: ", annual_pay)



annual_pay_check = float(input("Input your reported annual pay here: "))
filing_status = int(input("Are you a single filer or a joint filer?(1 or 2): "))

if annual_pay < 12000 and filing_status == 1:
    print("Your weekly pay will be taxed by 5%")
    print("The tax deduction is: ", gross_pay * 0.05)
    gross_pay = gross_pay - (gross_pay * 0.05)
    print("Your new weekly pay is: ", gross_pay)
elif annual_pay < 12000 and filing_status ==2:
    print("No Taxes")
    print("Your new weekly pay is: ", gross_pay)
elif annual_pay >= 12000 and annual_pay <= 24999.99 and filing_status == 1:
    print("Your weekly pay will be taxed by 10%")
    print("The tax deduction is: ", gross_pay * 0.10)
    gross_pay = gross_pay - (gross_pay * 0.10)
    print("Your new weekly pay is: ", gross_pay)
elif annual_pay >= 12000 and annual_pay <= 24999.99 and filing_status == 2:
    print("Your weekly pay will be taxed by 6%")
    print("The tax deduction is: ", gross_pay * 0.06)
    gross_pay = gross_pay - (gross_pay * 0.06)
    print("Your new weekly pay is: ", gross_pay)
elif annual_pay >= 25000 and annual_pay <= 74999.99 and filing_status == 1:
    print("Your weekly pay will be taxed by 15%")
    print("The tax deduction is: ", gross_pay * 0.15)
    gross_pay = gross_pay - (gross_pay * 0.15)
    print("Your new weekly pay is: ", gross_pay)
elif annual_pay >= 25000 and annual_pay <= 74999.99 and filing_status == 2:
    print("Your weekly pay will be taxed by 11%")
    print("The tax deduction is: ", gross_pay * 0.11)
    gross_pay = gross_pay - (gross_pay * 0.11)
    print("Your new weekly pay is: ", gross_pay)
elif annual_pay >= 75000 and filing_status == 1:
    print("Your weekly pay will be taxed by 20%")
    print("The tax deduction is: ", gross_pay * 0.20)
    gross_pay = gross_pay - (gross_pay * 0.20)
    print("Your new weekly pay is: ", gross_pay)
elif annual_pay >= 75000 and filing_status == 2:
    print("Your weekly pay will be taxed by 20%")
    print("The tax deduction is: ", gross_pay * 0.20)
    gross_pay = gross_pay - (gross_pay * 0.20)
    print("Your new weekly pay is: ", gross_pay)