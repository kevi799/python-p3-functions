#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    
greet_programmer()    

def greet(name):
   
   print(f'Hello, {name}!')

greet('Kevin')

def greet_with_default(name="programmer"):
    
    print(f'Hello, {name}!')

greet_with_default()    

def add(num1, num2):
    sum = num1 +num2
    return sum

def halve(number):
    result = number / 2
    return result
halve(9)
