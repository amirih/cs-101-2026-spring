# you can only import the function that you want to use
# in this case, we are importing the function hello from p1 and p2
# and we are renaming the function to hello1 and hello2 respectively
# renaming the function is useful when you have two functions with the same name
from p1 import hello as hello1
from p2 import hello as hello2

if __name__ == '__main__':
    
    hello1()
    hello2()