if __name__ == '__main__':
    # you can use a general exception to catch all exceptions
    try:
        print(1/0)
    except Exception as e:
        print(f'Error: {e}')