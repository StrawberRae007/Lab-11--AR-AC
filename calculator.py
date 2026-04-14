#https://github.com/StrawberRae007/Lab-11--AR-AC
#Partner 1: Audrey Reid
#Partner 2: Andrea Mae Cecillano

import math

def square_root(a):
    try:
        if a<0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot take square root of a negative number.")

def hypotenuse(a,b):
    try:
        return math.hypot(a,b)
    except Exception as e:
        print(f"An error occured: {e}")
        raise

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def logarithm(a,b):
    if a<=0 or a==1:
        raise ValueError("The logarithm base of a cannot be negative, 0, or 1.")
    if b<=0:
        raise ValueError("The logarithm value of b must be greater than 0.")
    return math.log(b,a)

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError('division by zero')
    return b/a

def exp(a,b):
    return a**b
