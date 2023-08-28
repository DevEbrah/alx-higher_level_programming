def safe_print_list(x=0, my_list=[]):
    """Print x elememts of a list.

    Args:
        x (int): The number of elements of my_list to print.
        my_list (list): The list to print elements from.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return ret

if __name__ == "__main__":
    example_list = [1, 2, 3, 4, 5]
    num_elements = 3
    safe_print_list(num_elements, example_list)
