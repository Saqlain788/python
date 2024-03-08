# from typing import Union

# per : Union[int, float] = int(input("Enter your percentage:\t"))
# grade : Union[str, None] = None

# if (per >= 0) and (per < 33):
#     grade = "Fail"
# elif (per >= 33) and (per < 40):
#     grade = "E"
# elif (per >= 40) and (per < 50):
#     grade = "D"
# elif (per >= 50) and (per < 60):
#     grade = "C"
# elif (per >= 60) and (per < 70):
#     grade = "B"
# elif (per >= 70) and (per < 80):
#     grade = "A"
# elif (per >= 80) and (per < 100):
#     grade = "A+"

# print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade}")

user_name : str = input("Enter user id: \t")
user_passwrod : str = input("Enter password:\t")


if user_name == 'admin' and user_passwrod == 'admin':
    print("sent otp on you registered number")
    otp : str = input("Please inter otp")
    if otp == '123':
        print("Welcom PIAIC")
    else: 
        print("invalid otp")
else:
    print("Invalid user or password")