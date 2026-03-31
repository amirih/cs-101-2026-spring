# dictionaries can contain items of different data types
# dictionaries can be nested
# dictionaries can be empty
# dictionaries cannot contain duplicate keys
# dictionaries can contain duplicate values
if __name__ == '__main__':

    dict_mixed = {"a": 1, "b": 2.2, "c": "cherry"}
    print(f"dict_mixed: {dict_mixed}, type: {type(dict_mixed)}")

    dict_nested = {"a": {"b": 2, "c": 3}, "d": [4, 5, 6], "e": {"f": 7, "g": 8}}
    print(f"dict_nested: {dict_nested}, type: {type(dict_nested)}")
    print(f"dict_nested['a']: {dict_nested['a']}")
    print(f"dict_nested['a']['b']: {dict_nested['a']['b']}")

    dict_duplicate_key = {"a": 1, "a": 2}
    print(f"dict_duplicate_key: {dict_duplicate_key}, type: {type(dict_duplicate_key)}")

    dict_duplicate_value = {"a": 1, "b": 1}
    print(f"dict_duplicate_value: {dict_duplicate_value}, type: {type(dict_duplicate_value)}")
