import p1

if __name__ == '__main__':
    # exception wont help in this case because the module does not have the function
    # this is not a runtime error, this is a compile time error
    try:
        p1.hello()
    except ImportError as e:
        print(e)
    finally:
        print('finally block is always executed')
    print('after finally block')
