# Calculator Day 010

from header import header

print(header)


# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():

  num1 = float(input("What's the first number: -> "))

  for symbol in operations:
      print(symbol)

  continue_calculating = True

  while continue_calculating:
    operation_symbol = input("Choose an operation -> ")

    num2 = float(input("What's the other number: -> "))

    function = operations[operation_symbol]

    result = function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")
    previous_result = result

    next_step = input("Enter 'A' to do another operation, enter 'N' to have a new calculation, or 'E' to exit program->")
    
    if next_step == 'N':
        continue_calculating = False
        calculator()
    elif next_step == 'A':
        num1 = result
    else:
        continue_calculating = False
        print("Goodbye!")

# Begin calculator
calculator()


