def calculator():
  """
  A simple calculator with basic arithmetic operations.
  """
  while True:
    try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      operator = input("Enter the operation (+, -, *, /): ")

      if operator == '+':
        result = num1 + num2
      elif operator == '-':
        result = num1 - num2
      elif operator == '*':
        result = num1 * num2
      elif operator == '/':
        if num2 == 0:
          print("Error: Division by zero")
          continue
        result = num1 / num2
      else:
        print("Invalid operator. Please enter +, -, *, or /.")
        continue

      print("Result:", result)
      break

    except ValueError:
      print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
  calculator()