# dictionaries are mutable
# dictionaries are unordered
# dictionaries are indexed
# dictionaries are created using curly braces {}
# dictionaries are key-value pairs
if __name__ == '__main__':
    dict_empty = {}
    print(f"dict_empty: {dict_empty}, type: {type(dict_empty)}")

    dict_int = {"a": 1, "b": 2, "c": 3}
    print(f"dict_int: {dict_int}, type: {type(dict_int)}")
    print(f"dict_int['a']: {dict_int['a']}")

    # you can update value of a key
    dict_int["a"] = 10
    print(f"dict_int['a']: {dict_int['a']}")

    # you can add new key-value pair
    dict_int["d"] = 4
    print(f"dict_int: {dict_int}")

    # you can delete key-value pair
    del dict_int["d"]
    print(f"dict_int: {dict_int}")
