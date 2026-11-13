pay_rate = float(input("How much are you paid per hour?: "))
hours_worked = float(input("How many hours did you work?: "))
gross_pay = pay_rate * hours_worked

if hours_worked > 40:
    print("Exceeded 40 hours, Overtime pay included")
    print(gross_pay)
    pay_rate = pay_rate * 1.5
else:
    print("No Overtime pay")
    print(gross_pay)
