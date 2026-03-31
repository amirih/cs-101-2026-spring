
if __name__ == '__main__':

    try:
        print(1/0)
    except ZeroDivisionError as e:
        print(f'Error: {e}')
    finally:
        print('finally block is always executed')
    print('after finally block')