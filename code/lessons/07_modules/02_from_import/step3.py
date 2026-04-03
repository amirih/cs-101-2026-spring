# you can only import the function that you want to use
# in this case, we are importing the function hello from step1 and step2
# and we are renaming the function to hello1 and hello2 respectively
# renaming the function is useful when you have two functions with the same name
from step1 import hello as hello1
from step2 import hello as hello2

if __name__ == '__main__':
    
    hello1()
    hello2()