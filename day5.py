import random
"""78
while True:
    choice=input('roll the dice🎲 (y/n):').lower()
    if choice == 'y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f'{die1},{die2}')
    elif choice == 'n':
     print('thanks for playing!😊')
     break
    else:
       print('invalid input!😶') """

number_to_guess = random.randint(1, 100)
print("Welcome to the Guess the Number Game!")
# 'try'used for handling the exception if the user enters a non-integer value.
#  It will catch the ValueError and prompt the user to enter a valid number.
while True:
 try:
  user_input=int(input("Please enter a number between 1 and 100: "))
  if user_input < number_to_guess:
    print("Too low! Try again!👎🏻")
  elif user_input > number_to_guess:
    print("Too high! Try again!👎🏻")
  else:
    print("Congratulations! You've guessed the number!🎊")
    break
 except ValueError:
    print("Invalid input. Please enter a valid number!🙂")
 



 