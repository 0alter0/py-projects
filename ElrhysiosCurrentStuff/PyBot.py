import random
from datetime import date, datetime

today = date.today()

print("PyBot: Hi there! Im PyBot.")

while True:
    message = input("You: ").lower()

    if "hello" in message or "hi" in message or "hey" in message:
        print("PyBot: Hello! How can i help you? [help]")

    elif message == "help":
        print("Commands:\ngames\ncalculator\ntime\ndate\n")

    elif "date" in message:
        print("PyBot: It is currently:", today)

    elif "games" in message or "game" in message:
        print("PyBot: Welcome to the number guessing game!")
        number = random.randint(1, 100)

        while True:
            user_input = input("(quit to exit) Guess a number 1-100: ").lower()

            if user_input == "quit":
                print("Bye!")
                break

            try:
                guess = int(user_input)

                if guess == number:
                    print("You win!")
                    break
                elif guess > number:
                    print("Guess lower")
                elif guess < number:
                    print("Guess higher")

            except ValueError:
                print("Please input integers, not strings")

    elif "calculator" in message:
        print("Pybot: Welcome to the calculator!")

        while True:
            try: 
                dig1 = int(input("Enter the first digit: "))
                dig2 = int(input("Enter the second digit: "))

                operator = input("What operation do you want to do? [add/subtract/multiply/divide/exit] ").lower()

                if operator == "add":
                    print(dig1 + dig2)
                elif operator == "subtract":
                    print(dig1 - dig2)
                elif operator == "multiply":
                    print(dig1 * dig2)
                elif operator == "divide":
                    # Tip: Consider adding a check here so it doesn't crash on division by zero!
                    print(dig1 / dig2)
                elif operator == "exit":
                    print("Bye!")
                    break

            except ValueError:
                print("Invalid input, please only input integers")
