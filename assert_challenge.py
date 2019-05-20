
# TEST AFTER (CHALLENGE 1

def count_upper_case(message):
  """
    Count the number of upper case characters in a given message
    `message` is the piece of text to be checked
    
    Returns the number of uppercase characters in a message
  """
  return sum([1 for c in message if c.isupper()])

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("AA") == 2, "two upper case"
assert count_upper_case("a") == 0, "one lower case"
# An example of a failed test would be:
# assert count_upper_case("asdER") == 0, "2 upper case"

print("All tests are complete")



# TESTS BEFORE (CHALLENGE 2)

def even_number_of_evens(numbers):
  """
  Returns the number of even numbers in a list of numbers

  "numbers" should be a list containing numbers

  Returns either true or false based on a number of criteria.
    - if "numbers" is empty return false
    - if the number of even numbers is odd return false
    - if the number of even numbers is zero return false
    - if the number of even numbers is even return true

    """ 
  # check to see if the list is empty

  if numbers == []:
    return False
  else:
    # Set a number_of_evens variable that will be incremented each time
    # an even number is found
    evens = 0

  # Iterate of over each item and if its an even number increment the "evens" variable

  for number in numbers:
    if number % 2 == 0:
      evens += 1

  if evens == 0:
    return False
  else:
    return evens % 2 == 0

  
# our set of test cases

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

# If all the test cases pass, print some successful info to the console to let
# the developer know
print("All tests passed")





