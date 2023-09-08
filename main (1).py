num = int(input("Enter a number:"))
if num < 0:
  print("Factorial is not defined for negative numbers.")
else:
  Factorial = 1
for i in range(1, num + 1):
  Factorial *= i
  print("the factorial of",num,"is",factorial)