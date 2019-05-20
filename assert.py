# Assertions

# A test thats true

"""
x = 1
y = 2

assert x < y, "x should be less than y"

print(x + y)

"""

# A test that isnt true

"""
x = 2
y = 1

assert x < y, "x should be less than y"

print(x + y)

"""

# or a better/more useful information in the terminal if we write:

"""
x = 2
y = 1

assert x < y, "{0} should be less than {1}".format(x, y)

print(x + y)

"""

"""
def count_ups_inword(message):
  count = 0
  for c in message:
    if c.isupper():
      count += 1
  return count
print(count_ups_inword("HI FRIend"))

"""

"""

def count_upper_case(message):
  count = 0
  for c in message:
    if c.isupper():
      count += 1
  return count

print(count_upper_case("Hello World"))

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$!&*") == 0, "Special characters"

print("All tests are passed")

"""
# TEST DRIVEN DEVELOPMENT
# The process of testing incremently

"""

def even_number_of_evens(numbers):
  if numbers ==[]:
    return False
  else:
    evens = 0

  for n in numbers:
    if n % 2 == 0:
      evens += 1

  if evens == 0:
    return False
  else:
    return evens %2 == 0

assert even_number_of_evens([]) == False, "No Numbers"
assert even_number_of_evens([2, 4]) == True, "2 even numbers"
assert even_number_of_evens([4]) == False, "1 even number"
assert even_number_of_evens([1, 3, 9]) == False, "3 odd numbers"

print("All tests have passed!")

"""

#  Refactoring (A method of driving our development using tests.)
# it allows us to build and refactor our code using tests.How do you use it? We think about and write tests to drive the behaviour of an individual function. We can then use extra tests to refactor and add extra functionality. This is how we can start to refactor our code using the DRY principle so that we're not repeating ourselves and still using our tests to make sure that they all pass. (DRY: Dont Repeat Yourself)

"""

def is_even(number):
  return number % 2 == 0

def even_number_of_evens(numbers):
  
  evens = 0
  for n in numbers:
    if is_even(n):
      evens += 1

  if evens == 0:
    return False
  else:
    return is_even(evens)

assert even_number_of_evens([]) == False, "No Numbers"
assert even_number_of_evens([2, 4]) == True, "2 even numbers"
assert even_number_of_evens([4]) == False, "1 even number"
assert even_number_of_evens([1, 3, 9]) == False, "3 odd numbers"

print("All tests have passed!")

"""

# We can often reduce functions that have loops like this down to a line or 2. This is known as pythonic python or idiomatic python

def is_even(number):
  return number % 2 == 0

def even_number_of_evens(numbers):
  
  evens = sum([1 for n in numbers if is_even(n)])
  return False if evens == 0 else is_even(evens)

assert even_number_of_evens([]) == False, "No Numbers"
assert even_number_of_evens([2, 4]) == True, "2 even numbers"
assert even_number_of_evens([4]) == False, "1 even number"
assert even_number_of_evens([1, 3, 9]) == False, "3 odd numbers"

print("All tests have passed!")

























