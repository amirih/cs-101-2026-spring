if __name__ == '__main__':
    
    message = "Hello, World!"
    number = 42

    print("This is a string:", message)
    print("Type of message:", type(message))
    print("This is a number:", number)
    print("Type of number:", type(number))

    message = 100
    print("This is a number now:", message)
    print("Type of message:", type(message))

    # you can use f to format a string with variables
    print(f"This is the message: {message} and this is the number: {number}")
