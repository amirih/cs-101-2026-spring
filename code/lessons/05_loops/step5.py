# more complicated loops

if __name__ == '__main__':
    dict_of_lists_of_dicts = {
        "one": [{"a": 1, "b": 2}, {"c": 3, "d": 4}],
        "two": [{"e": 5, "f": 6}, {"g": 7, "h": 8}],
    }
    for key in dict_of_lists_of_dicts:
        print(f"key: {key}, value: {dict_of_lists_of_dicts[key]}")
        for list_item in dict_of_lists_of_dicts[key]:
            print(f"list_item: {list_item}")
            for dict_item in list_item:
                print(f"key: {dict_item}, value: {list_item[dict_item]}")