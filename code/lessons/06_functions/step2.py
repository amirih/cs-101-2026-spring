def with_parameters_no_return(a, b, c):
    print(f"a: {a}, b: {b}, c: {c}")

def with_parameters_with_return(a, b, c):
    print(f"a: {a}, b: {b}, c: {c}")
    return a + b + c
    
def no_parameters_no_return():
    print("This function has no parameters")
    print("and it does not return anything.")

def no_parameters_with_return():
    print("This function has no parameters")
    print("but it returns a message.")
    return "Hello, World!"

def with_default_parameters(a, b=10, c=20):
    print(f"a: {a}, b: {b}, c: {c}")
    return a + b + c

if __name__ == '__main__':
    with_parameters_no_return(1, 2, 3)
    result = with_parameters_with_return(1, 2, 3)
    print(f"Result: {result}")
    
    no_parameters_no_return()
    message = no_parameters_with_return()
    print(f"Message: {message}")

    result_default = with_default_parameters(1)
    print(f"Result of with_default_parameters: {result_default}")
