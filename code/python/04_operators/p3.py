# Logical operators

if __name__ == '__main__':
    and_operator_results = True and False
    print(f"True and False: {and_operator_results}")

    or_operator_results = True or False
    print(f"True or False: {or_operator_results}")

    not_operator_results = not True
    print(f"not True: {not_operator_results}")

    mixed_operator_results = True and False or not True
    print(f"True and False or not True: {mixed_operator_results}")

    mixed_operator_results = and_operator_results or or_operator_results and not_operator_results
    print(f"and_operator_results or or_operator_results and not_operator_results: {mixed_operator_results}")
