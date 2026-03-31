
if __name__ == '__main__':
    list_of_numbers = [10, 20, 30, 40, 50]
    for number in list_of_numbers:
        print(f"number: {number}")

    print("---------------------------------")
    list_of_strings = ["apple", "banana", "cherry"]
    for fruit in list_of_strings:
        print(f"fruit: {fruit}")

    print("---------------------------------")
    list_of_tuples = [(10, 20), (30, 40), (50, 60)]
    for tuple_item in list_of_tuples:
        print(f"tuple_item: {tuple_item}")

    print("---------------------------------")
    list_of_lists = [[10, 20], [30, 40], [50, 60]]
    for list_item in list_of_lists:
        for item in list_item:
            print(f"item: {item}")
