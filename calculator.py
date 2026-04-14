import math

def add(a,b): a+b

def sub(a,b): a-b

def mul(a,b): a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError('division by zero')
    return a/b

def log(a,b):
    if a<=0 or a==1 or b<=0:
        raise ValueError("Logarithm parameters must be positive and base cannot be 1.")
    return math.log(a,b)

def exp(a,b):
    return a**b

