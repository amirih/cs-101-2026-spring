# tuple 

if __name__ == '__main__':
    tuple_empty = ()
    print(f"tuple_empty: {tuple_empty}, type: {type(tuple_empty)}")

    # tuple are immutable
    tuple_int = (1, 2, 3)
    print(f"tuple_int: {tuple_int}, type: {type(tuple_int)}")
    print(f"tuple_int[0]: {tuple_int[0]}")

    # this will throw error
    # tuple_int[0] = 10

    # tuple can be nested and can contain list
    tuple_nested = ((1, 2, 3), [4, 5, 6], (7, 8, 9))
    print(f"tuple_nested: {tuple_nested}, type: {type(tuple_nested)}")

    print(f"tuple_nested[0]: {tuple_nested[0]}")
    print(f"tuple_nested[1]: {tuple_nested[1]}")
    print(f"tuple_nested[2]: {tuple_nested[2]}")

    # you can update list inside tuple
    tuple_nested[1][0] = 10
    print(f"tuple_nested[1]: {tuple_nested[1]}")
    print(f"tuple_nested: {tuple_nested}")
    
    # but this will throw error
    # tuple_nested[1] = [10, 11, 12]