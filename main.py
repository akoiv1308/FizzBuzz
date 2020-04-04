'''
Programm that simulates the game - FizzBuzz. It's a game where group of people has to say, in order, a sequence of numbers starting at 1, as fast as they can. If the number is multiple of 3, person should say "Fizz". If the number is multiple of 5, person should say "Buzz".
If the number is multiple of both 3 and 5, person should say "FizzBuzz"
'''
#FIZZ BUZZ PROGRAMM

for number in range (10):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

#SUM OF NUMBERS

userNumber = int(input("Enter your maximum:"))

sum = 0

for i in range(1, userNumber + 1):
  sum += i

print(sum)

#SUM OF THE ALL NON-FIZZ, BUZZ, FIZZBUZZ NUMBERS

userNumber = int(input("Enter a number:"))

sum = 0

for i in range(1, userNumber + 1):
  if not(i % 3 == 0 or i % 5 == 0):
    sum += i

print(sum)

#PRIME/COMPOSITE NUMBER DETERMINATOR

userNumber = int(input("Enter a number:"))

final_number = 0

for i in range(1, userNumber +1):
  if userNumber % i == 0:
    final_number +=1

if final_number == 2:
  print("It is a prime number")
else:
  print("It is a composite number")




