my_time = int(input("What time is it in your place? (24 hour format): "))
print(my_time)

if my_time > 4 and my_time < 10:
    print("Good Morning")
elif my_time >= 10 and my_time < 17:
    print("Good Day")
elif my_time >= 17 and my_time < 23:
    print("Good Evening")
else:
    print("What are you doing up so late??")