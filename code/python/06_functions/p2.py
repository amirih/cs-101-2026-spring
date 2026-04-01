def function_with_args(a, b, c):
    print(f"a: {a}, b: {b}, c: {c}")

def function_with_default_args(a, b, c=3):
    print(f"a: {a}, b: {b}, c: {c}")

def function_with_return(a, b, c):
    result = a + b + c
    return result
    
def function_without_args():
    print("This function has no arguments.")

if __name__ == '__main__':
    function_without_args()
    function_with_args(1, 2, 3)
    function_with_args(4, 5, 6)
    function_with_args(7, 8, 9)
    print("---------------------------------")

    function_with_default_args(1, 2,8)
    function_with_default_args(4, 5)
    print("---------------------------------")

    result = function_with_return(1, 2, 3)
    print(f"result: {result}")
    # you can just print the return value directly
    print(f"result: {function_with_return(4, 5, 6)}")




