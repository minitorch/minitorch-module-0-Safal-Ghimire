"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable,Union,TypeVar

Number=Union[int,float]
T=TypeVar("T")
#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$



# TODO: Implement for Task 0.1.
def mul(a:Number,b:Number)-> Number:
  """returns the product of two numbers
  
  args:
  a(int or float): the first number
  b(int or float): the second number

  returns:
  int or float: product of first and second number
  
  """
  return a * b

def id (x:T)-> T:
  """returns the input unchanged
  
  args:
  x(T): any data type
  
  returns:
  T:same data type as x
  
  """
  return x

def add(x:Number,y:Number)->Number:
  """Adds two numbers
  
  args:
  x(int or float): first number
  y(int or float): second number
  
  returns:
  int or float: product of first and second number"""
  return x + y

def neg(x:Number)-> Number:
  """Negates a number
  
  args:
  x(int or float) :Number
  
  returns:
  int or float: negation of number"""
  return -x

def lt(x:Number,y:Number)-> bool:
  """checks if one number is less then another
  
  args:
  x(int or float): first number
  y(int or float): second number
  
  returns:
  bool: True if x is less than y, else False."""
  
  return x < y

def eq(x:Number,y:Number)-> bool:
  """Checks if two numbers are equal
  
  args:
  x(int or float): first number
  y(int or float): second number
  
  returns
  bool: True if numbers are equal, else False"""

  return x == y

def max(x:Number,y:Number)-> Number:
  """Returns the larger of two numbers
  
  args:
  x(int or float): first number
  y(int or float): second number
  
  returns
  int or float: the largest of two numbers"""
  if x>y: 
    return x
  return y
  
def is_close(x: Number, y: Number) -> bool:
  """Returns the larger of two numbers
  
  args:
  x(int or float): first number
  y(int or float): second number
  
  
  returns
  bool: True if the absolute difference between x and y is less than or equal to 1e-9, else False
  """
  return abs(x-y) <= 1e-9
  
def sigmoid(x:Number) -> float:
  """computes the sigmoid activation function
  
  args:
  x(int or float): input value
  
  returns
  float: sigmoid of x, range (0,1)
  """
  return 1 / (1 + math.exp(-x))

def relu (x:Number)-> float:
  """Applies the ReLU activation function
  
  Args:
    x(int or float): The input value
  
  Returns:
    float: ReLU activation of x, 0 if negative no else the input value
  """
  if x<0:
    return 0
  
  return x

def log(x:Number)->float:
  """Calculates the natural logarithm
  
  Args:
    x(int or float): The input number
    
  Returns:
    float: Logarithm of x
  """
  return math.log(x)

def exp(x:Number)-> float:
  """Calculates the exponential function
  
  Args:
    x(int or float): The input number
  
  Returns:
    float: The exponential function of x, e^x
  """
  return math.exp(x)

def inv(x:Number)-> float:
  """Calculates the reciprocal
  
  Args:
    x(int or float): The input number
    
  Returns:
    float: Reciprocal of the given number, 1/x"""
  
  return 1/x

def log_back(x:Number,y:Number)-> float:
  """Computes the derivative of log times a second log
  
  Args:
    x(int or float): The value to keep inside log
    y(int or float): Multiplication factor

  Returns:
    float: derivative of reciprocal of log of x times y

  notes:
    -log is natural logarithm
    -derivative of log of x  is 1/x 
    """
  return y*(1/x)

def inv_back(x:Number,y:Number) -> float:
  """Computes the derivative of reciprocal times a second arg
  
  Args:
    x(int or float): The value whose derivative of reciprocal is to be calculated
    y(int or float): Multiplication factor
    
  Returns:
    float derivative of reciprocal of log of x times y, y* (-1/x^2)
  
  Notes:
    derivative of 1/x is -1/(x^2)"""
  
  return y* (-1/x**2)

def relu_back(x:Number,y:Number)-> float:
  """Computes the derivative of ReLU times a second arg
  Args:
    x(int or float): value to plug in ReLU
    y(int or float): Multliplication factor
  
  Returns:
    float: Derivative of relu of x times y
      
  Notes:
    derivative of ReLU  for x is negative is 0
    derivative of ReLU foe x is positive is 1 """

  if x<0:
    return 0
  return y
# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def negList():
  pass

def addLists():
  pass

def sum():
  pass

def prod():
  pass
# TODO: Implement for Task 0.3.
