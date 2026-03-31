# for loops in Python
if __name__ == '__main__':
    # for loop with range
    for loop_counter in range(5):
        print(f"loop_counter: {loop_counter}")

    print("---------------------------------")
    # for loop with range and start
    for loop_counter in range(10, 15):
        print(f"loop_counter: {loop_counter}")

    print("---------------------------------")
    # for loop with range, start and step
    for loop_counter in range(20, 30, 2):
        print(f"loop_counter: {loop_counter}")

    print("---------------------------------")
    # for loop with range, start, step and negative step
    for loop_counter in range(30, 20, -2):
        print(f"loop_counter: {loop_counter}")