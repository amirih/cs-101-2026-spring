# you can have nested try-except blocks

if __name__ == '__main__':
    try:
        try:
            print(1/0)
        except ZeroDivisionError as e:
            print(f'Error: {e}')
        finally:
            print('inner finally block is always executed')
        print('after inner finally block')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        print('outer finally block is always executed')
    print('after outer finally block')