# in python, you do not need to specify the data type of the variable python will automatically determine the data type this is called dynamic typing
# you can use the type() function to determine the data type of a variable or the isinstance() function to determine if a variable is of a certain data type
if __name__ == '__main__':
    var_integer = 10
    var_float = 10.5
    var_string = "Hello, World!"
    var_boolean = True
    
    print(f"var_integer: {var_integer}, type: {type(var_integer)}")
    print(f"var_float: {var_float}, type: {type(var_float)}")
    print(f"var_string: {var_string}, type: {type(var_string)}")
    print(f"var_boolean: {var_boolean}, type: {type(var_boolean)}")
    
    # you can also use the isinstance() function to determine the data type of a variable
    print(f"var_integer is int: {isinstance(var_integer, int)}")
    print(f"var_float is float: {isinstance(var_float, float)}")
    print(f"var_string is str: {isinstance(var_string, str)}")
    print(f"var_boolean is bool: {isinstance(var_boolean, bool)}")

