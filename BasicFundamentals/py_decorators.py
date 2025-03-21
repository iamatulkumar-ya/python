"""
This file is used to understand the decorators in python. 
"""

# Let's understand the wrapper functions

def f1(func):
    def wrapper():
        print("Wrapper Started")
        func()
        print("Wrapper Ended")

    return wrapper


def f2():
    print("This is f2 function")




print(f1(f2)())