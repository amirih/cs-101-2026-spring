# list can be accessed using index.
# list can be sliced.
# list can be updated.
# list can be deleted.
if __name__ == '__main__':

    list_mix = [1, 2.2, "cherry"]
    print(f"list_mix: {list_mix}, type: {type(list_mix)}")

    # Access list using index
    print(f"list_mix[0]: {list_mix[0]}")
    print(f"list_mix[1]: {list_mix[1]}")
    print(f"list_mix[2]: {list_mix[2]}")

    # Slice list
    print(f"list_mix[0:2]: {list_mix[0:2]}")
    print(f"list_mix[1:]: {list_mix[1:]}")
    print(f"list_mix[:2]: {list_mix[:2]}")

    # Update list
    list_mix[0] = 10
    print(f"list_mix: {list_mix}")

    # Delete list
    del list_mix[0]
    print(f"list_mix: {list_mix}")
