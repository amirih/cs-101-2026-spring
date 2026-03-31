# set cannot contain duplicate elements

if __name__ == '__main__':
    set_elements = {1, 2, 3}
    print(f"set_elements: {set_elements}, type: {type(set_elements)}")

    set_with_duplicate = {1, 2, 3, 1, 2, 3}
    print(f"set_with_duplicate: {set_with_duplicate}, type: {type(set_with_duplicate)}")

    set_mixed = {1, 2.2, "cherry"}
    print(f"set_mixed: {set_mixed}, type: {type(set_mixed)}")

    