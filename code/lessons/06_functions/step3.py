
def returns_list_compact(number_of_elements):
    list_numbers=  [i for i in range(number_of_elements)]
    return list_numbers

def returns_list_explicit(number_of_elements):
    list_numbers = []
    for i in range(number_of_elements):
        list_numbers.append(i)
    return list_numbers


def returns_dict_compact(number_of_elements):
    dict_numbers = {i: i for i in range(number_of_elements)}
    return dict_numbers

def returns_dict_explicit(number_of_elements):
    dict_numbers = {}
    for i in range(number_of_elements):
        dict_numbers[i] = i
    return dict_numbers

def returns_set_compact(number_of_elements):
    set_numbers = {i for i in range(number_of_elements)}
    return set_numbers
