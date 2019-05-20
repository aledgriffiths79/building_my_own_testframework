# CHALLENGE 1

def num_of_evens(numbers):
  return 0

def test_are_equal(actual, expected):

  """
  Test that 2 values are equal. Raises Assertion error if both values are not equal.
  "actual" is the actual value produced
  "expected" is the the value that was supposed to be produced

  """
  assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def test_not_equal(a, b):
  """
  Test that 2 values are not equal. Raises assertionerror if both values are not equal.
  "a" is the actual value produced
  "b" is the value that was supposed to be produced

  """

  assert a != b, "Did not expect {0} but got {1}".format(a, b)

def test_is_in(collection, item):
  """
  Check to ensure that a given collection contains a given value. Raises AssertionError if "item" is not in collection
  "colection" is the collection to be tested
  "item" is the item that is being searched for

  """

  assert item in collection, "{0} does not contain {1}".format(collection, item)

# Test to fail the "test_are_equal" function
# test_are_equal(num_of_evens([1, 2, 4, 6, 7, 9, 13]), 3)

# Test to fail the "test_not_equal" function
# test_not_equal(0, 0)

# Test to fail the "test_is_in" function
# test_is_in([1], 2)

def test_not_in(collection, item):
  assert item not in collection, "{0} is not in {1}".format(item, collection)

# Test to fail the "test_not_in" function
# test_not_in([1], 1)

def test_between(upper_limit, lower_limit, actual):
  assert lower_limit <= actual <= upper_limit, "{0} is not between {1} and {2}".format(actual, lower_limit, upper_limit)

# Test to fail the "test between" function

test_between(10, 1, 200)

test_between

print("All tests complete")































