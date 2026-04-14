"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(a):
    if a<0:
        raise ValueError("Can't take square root of negative number")
    math.sqrt(a)
def hypotenuse(a,b):
    math.hypot(a,b)
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if a==0:
        raise ZeroDivisionError("a is 0, can't divide by zero.")
    return b/a
def logarithm(a,b):
    if a<=0 or a==1:
        raise ValueError("The logarithm base of a cannot be negative, 0, or 1.")
    if b<=0:
        raise ValueError("The logarithm value of b must be greater than 0.")
    return math.log(b,a)
def exponent(a,b):
    return a**b

