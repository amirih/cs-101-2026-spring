# List can be nested.
# List can be empty.
# List can contain duplicate items.

if __name__ == '__main__':
    list_nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"list_nested: {list_nested}, type: {type(list_nested)}")

    list_empty = []
    print(f"list_empty: {list_empty}, type: {type(list_empty)}")

    list_duplicate = [1, 2, 3, 1, 2, 3]
    print(f"list_duplicate: {list_duplicate}, type: {type(list_duplicate)}")

    list_mixed_nested = [[1, 2.3, 3], [4.4, "5", 6.6], ["apple", 2, "cherry"]]
    print(f"list_mixed_nested: {list_mixed_nested}, type: {type(list_mixed_nested)}")
