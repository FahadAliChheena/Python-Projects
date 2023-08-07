def add(*numbers):
    return sum(numbers)

def subtract(*numbers):
    total = numbers[0]
    for number in numbers[1:]:
        total -= number
    return total

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

def divide(*numbers):
    total = numbers[0]
    for number in numbers[1:]:
        total /= number
    return total

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print("Available operations:", ", ".join(operations.keys()))
    operation = input("What operation would you like to perform? ")

    if operation not in operations:
        print("Invalid operation")
        return

    numbers_input = input("Enter numbers separated by spaces: ")
    try:
        numbers = [float(number) for number in numbers_input.split()]
        result = operations[operation](*numbers)
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()