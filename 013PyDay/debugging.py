# Day 13: Debugging exercise
#
# Debug the code below.
#
# The program should print each number from 1 to 100 in turn.
# When the number is divisible by 3, print "Fizz".
# When the number is divisible by 5, print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then print "FizzBuzz"
#
# for number in range(1, 100):
# if number % 3 == 0 or number % 5 == 0:
#   print("FizzBuzz")
# if number % 3 == 0:
#   print("Fizz")
# if number % 5 == 0:
#   print("Buzz")
# else:
#   print(number)

# Result:

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
