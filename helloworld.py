Thomas_age = 3
Age_at_kindergarten = 5
if Thomas_age > Age_at_kindergarten:
    print("Thomas is in primary level")
elif Thomas_age == Age_at_kindergarten:
    print("He is at kindergarten")


def print_kelvin():
    text = "My youtube channel is called kelvin cookies"
    print(text)
    print(text)
from itertools import count
from locale import windows_locale
from math import factorial

# finding a factorial using a function
num = int (input("Enter a number: "))
factorial = 1
if num < 0:
         print ("sorry,factorial does not exit for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
print(f"The factorial of {num} is", factorial)

# Counting vowels
vowel=["a", "e", "o","i","u" ]
word="vowel"
count = 0
for character in word:
    if character in vowel:
        count += 1
        print(count)

# counting consonants
vowel =["a", "e","i","o","u"]
word ="williams"
count = 0
for character in word:
    if character not in vowel:
        count +=1
        print(count)

# create a generator to produce first n prime  numbers.
def isprime (num):
    for i in range(2, num):
        if num%i == 0:
            return False
def prime_generator(n):
    num = 2
    while n:
        if isprime(num):

         yield num
        n-=1
    num+=1
x = int (input("Enter the no. of prime numbers required"))
it =prime_generator(x)
for e in it:
    print(0, end=" ")


# control loop.
while True:
    age = input("Please enter your age: ")
    if age.isdigit() and int(age) > 0:
        print(f"Thank you! You entered a valid age: {age}")
        break
    else:
        print("Invalid input. Please enter a positive integer.")

# bank systme /
balance = 1000.0 # Initial balance
while True:
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print(f"Your balance is: ${balance:.2f}")
    elif choice == "2":
            deposit = float(input("Enter amount to deposit: "))
    if deposit > 0:
        balance += deposit
        print(f"${deposit:.2f} deposited successfully.")
    else:
        print("Invalid deposit amount.")
        elif == "3"
    elif  == "3":
        withdraw = float(input("Enter amount to withdraw: "))
    if 0 < withdraw <= balance:
        balance -= withdraw
        print(f"${withdraw:.2f} withdrawn successfully.")
    else:
        print("Insufficient balance or invalid amount.")
        elif choice == "4";
    print("Thank you for using our ATM. Goodbye!")
    break
else:
    print("Invalid choice. Please try again.")






