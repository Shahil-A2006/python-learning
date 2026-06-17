"""   UNITTEST  """

# Unit testing checcks small pieces of code (like functions or class) to confirm they work correctly.
# Unittest framework allows developers to verify thatt functions produce the expected results.
# A testcase is created is inheriting from unittest.TestCase and defining methods that starts with test_ .
# Unittest is a built-in pyhton module used for performing Unit testing.
# Without importing unittest,we cannot use classes like TestCase or methods like asserEqual() for testing our code.

""" The Main parts of a Unit Test   """

# 1. Import the testing module = import unittest ,so that python can perform testing.
# 2. Code to be tested         = This is the function,method,or class that you want to test
# 3. Test class                = Create a class that inherits from Unittest.TestCare
# 4. Test Method               = A method whose name starts with test_ 
# 5. Asertion                  = Asertions compare the actual result with the expected results
# 6. Test Runner               = Runs all the tests.This searches for all test class and test methods and executes them

"""    SYNTAX of Unittest  """

# import unittest                             #1. Import

# def add(a,b):                                 #2. Code to be tested
#     return a + b

# class TestAdd(unittest.TestCase):               #3. Test Class

#     def test_add(self):                          #4. Test Method
#         self.assertEqual(add(3,2), 5)             #5. Assertion

# unittest.main()    #OK                              #6. Test Runner


#================================================================================================================

import unittest

def square(n):
    return n * n

class Testsquare(unittest.TestCase):

    def test_square_positive(self):
        self.assertEqual(square(5),25)              #ok = 25

    def test_square_not_equal(self):
        self.assertNotEqual(square(5),30)            #ok bcoz 30 !=25

    def test_square_greater(self):
        self.assertGreater(square(5),20)           #ok bcoz 25 > 20

    def test_square_smaller(self):
        self.assertLess(square(5),30)               #ok bcoz 25 < 30

unittest.main()