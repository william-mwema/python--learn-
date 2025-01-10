# print("hello world")
# Thomas_age =5,
# Age_kindergarten = 5,
# if Thomas_age > Age_kindergarten:
#     print("Thoams is at primary level")
# elif Thomas_age == Age_kindergarten:
#     print("Thomas is at kindergaetn")
# # else:
# #     print("he will join the school next year")
# def print_kelvin():
#     text = "It is amazing to learn python "
#     name = "williams has been folowing me closely"
    
# print_kelvin()

# FINDING A FACTORIAL

num = int (input("Enter a number: "))
factorial = 1
if num < 0:
         print ("sorry,factorial does not exit for negative mumbers")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print(f"The factorial of {num} is", factorial)
    
health = -2
if health <=0:
     print("You need to get well first")
elif health >=20:
    print("keep going with the game")
else: 
    print("Heathy is key to excellence")
