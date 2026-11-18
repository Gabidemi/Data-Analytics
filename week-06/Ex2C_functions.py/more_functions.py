def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(city + ", " + state + " " + zip)
    print()


def add_numbers(*numbers):
    total = 0
    calculation = ""
    for number in numbers:
        if calculation == "":
            calculation = str(number)
        else:
            calculation = calculation + " + " + str(number)

        total = total + number
    print(calculation + " = " + str(total))


def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due: ,.2f}")
    print(f"Amount Paid: ${amount_paid: ,.2f}")
    print()
    if amount_paid >= total_due:
        change_due = amount_paid - total_due
        print(f"Change Due: ${change_due: ,.2f}")
    else:
        remaining_balance = total_due - amount_paid
        print(f"Remaining Balance: ${remaining_balance: ,.2f}")
    print()


display_mailing_label(
    "Alex Smith", "123 Main Street", "Hartford", "CT", "06103"
)

display_mailing_label(
    "Jordan Brown", "456 Oak Avenue", "New Haven", "CT", "06510"
)

add_numbers(5)
add_numbers(5, 10)
add_numbers(5, 10, 15, 20)

display_receipt(500.00, 521.00)
display_receipt(487.92, 487.92)
display_receipt(250.00, 157.00)