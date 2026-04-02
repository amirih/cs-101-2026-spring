# recursion examples
# recursion is a programming technique where a function calls itself in order to 
# solve a problem. It typically involves a base case that stops the recursion and 
# a recursive case that breaks the problem into smaller subproblems.

def sum_to_n(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    else:
        # Recursive case: return n plus the sum of the first n-1 natural numbers
        return n + sum_to_n(n - 1)
    
def factorial(n):
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    else:
        # Recursive case: return n multiplied by the factorial of n-1
        return n * factorial(n - 1)
    
def fibonacci(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Base case: if n is 1, return 1
    elif n == 1:
        return 1
    else:
        # Recursive case: return the sum of the two preceding Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def hanoi(n, source, target, helper):
        # Base case: if n is 1, move the disk from source to target
        if n == 1:
            print(f"Move disk 1 from {source} to {target}")
            return
        # Recursive case: move n-1 disks from source to helper, then move the nth disk from source to target, and finally move the n-1 disks from helper to target
        hanoi(n - 1, source, helper, target)
        print(f"Move disk {n} from {source} to {target}")
        hanoi(n - 1, helper, target, source)

def power(base, exponent):
    # Base case: if exponent is 0, return 1
    if exponent == 0:
        return 1
    else:
        # Recursive case: return base multiplied by the result of power with exponent decremented by 1
        return base * power(base, exponent - 1)
    
if __name__ == "__main__":
    print(f"Sum of first 5 natural numbers: {sum_to_n(5)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"10th Fibonacci number: {fibonacci(10)}")
    print(f"2 raised to the power of 3: {power(2, 3)}")
    num_disks = 3
    hanoi(num_disks, 'A', 'C', 'B')
