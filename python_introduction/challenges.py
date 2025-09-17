import random

secret_number = random.randint(1, 10)
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it?"))

match guess:
  case x if x ==secret_number:
    print("Congratulations, you guessed it!")
  case _:
        if guess > secret_number:
          print("Nope, your guess is a bit high.")
        elif guess < secret_number:
          print("Nope, your guess is a bit low.")
        guess = int(input( "Give it another shot!"))

        match guess:
          case x if  x == secret_number:
            print("Congratulations, you guessed it!")
          case _:
              print("Nope, Your guess is incorrect. Try again later.")
