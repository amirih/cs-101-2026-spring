if __name__ == '__main__':
    dict_of_numbers = {"one": 1, "two": 2, "three": 3}

    for key in dict_of_numbers:
        print(f"key: {key}, value: {dict_of_numbers[key]}")

    print("---------------------------------")
    for key, value in dict_of_numbers.items():
        print(f"key: {key}, value: {value}")

    print("---------------------------------")
    for value in dict_of_numbers.values():
        print(f"value: {value}")

    print("---------------------------------")
    for key in dict_of_numbers.keys():
        print(f"key: {key}")

    print("---------------------------------")
    # This will only print the keys
    for x in dict_of_numbers:
        print(f"x: {x}")

    