import re

print("Hello! I am a simple chatbot that can perform basic mathematical operations. You can ask me to add, subtract, multiply, or divide numbers.")

while True:
    user_input = input("What would you like me to do? ")
    user_input = user_input.lower()

    # Check if the user wants to exit the program
    if user_input == "exit":
        print("Goodbye!")
        break

    # Use regular expressions to extract the numbers from the user's input
    numbers = re.findall(r'\d+', user_input)

    # Check if the user provided two numbers
    if len(numbers) != 2:
        print("Sorry, I need two numbers to perform an operation. Please try again.")
        continue

    # Convert the numbers to integers
    num1 = int(numbers[0])
    num2 = int(numbers[1])

    # Check which operation the user wants to perform
    if "add" in user_input:
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}.")
    elif "subtract" in user_input:
        result = num1 - num2
        print(f"The difference between {num1} and {num2} is {result}.")
    elif "multiply" in user_input:
        result = num1 * num2
        print(f"The product of {num1} and {num2} is {result}.")
    elif "divide" in user_input:
        if num2 == 0:
            print("Sorry, I cannot divide by zero.")
            continue
        result = num1 / num2
        print(f"The quotient of {num1} and {num2} is {result}.")
    else:
        print("Sorry, I don't understand that. Please try again.")
