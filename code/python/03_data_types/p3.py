# List is a collection of items. It is ordered and mutable.
# List can contain items of different data types.
# List is created using square brackets [].
if __name__ == '__main__':

    var_list_int = [1, 2, 3]
    print(f"var_list_int: {var_list_int}, type: {type(var_list_int)}")

    var_list_float = [1.1, 2.2, 3.3]
    print(f"var_list_float: {var_list_float}, type: {type(var_list_float)}")

    var_list_str = ["apple", "banana", "cherry"]
    print(f"var_list_str: {var_list_str}, type: {type(var_list_str)}")

    var_list_mixed = [1, 2.2, "cherry"]
    print(f"var_list_mixed: {var_list_mixed}, type: {type(var_list_mixed)}")