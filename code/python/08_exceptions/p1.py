# Exceptions are errors that occur during the execution of a program. When that error occurs, Python generates an exception that can be handled, which avoids your program to crash.
if __name__ == '__main__':
    try:
        print(1/0)
    except ZeroDivisionError as e:
        print('Error:', e)