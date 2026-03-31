# nested for loops
if __name__ == '__main__':
    list_of_lists = [[10, 20], [30, 40], [50, 60]]
    for list_item in list_of_lists:
        print(f"list_item: {list_item}")
        for item in list_item:
            print(f"item: {item}")

    print("---------------------------------")
    dict_of_lists = {"one": [10, 20], "two": [30, 40], "three": [50, 60]}
    for key in dict_of_lists:
        print(f"key: {key}")
        for item in dict_of_lists[key]:
            print(f"item: {item}")

    print("---------------------------------")
    list_of_dicts = [{"one": 1, "two": 2}, {"three": 3, "four": 4}]
    for dict_item in list_of_dicts:
        print(f"dict_item: {dict_item}")
        for key in dict_item:
            print(f"key: {key}, value: {dict_item[key]}")
