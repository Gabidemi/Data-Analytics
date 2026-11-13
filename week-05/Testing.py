Name = input("Enter your name here: ")
Score = float(input("Enter your score here: "))

if Score >= 90:
    print("Outstanding")
elif Score >= 80:
    print("Exceeds Expectations")
elif Score >= 70:
    print("Meets Expectations")
elif Score >= 60:
    print("Below Expectations")
else:
    print("Unsatisfactory")


