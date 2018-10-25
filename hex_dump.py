# -*- coding: utf-8 -*-
import sys
EMPTY_STRING = ''
WRONG_PARAMS_1 = 'The function should receive 1 param '
WRONG_PARAMS_2 = ' is given'


def input_params():
    """
    the function gets the input params
    from the user
    :return: list of the giving params
    """
    return sys.argv[1:]


def valid(params_list):
    """
    the function returns true if the
    params are valid, otherwise false
    :param params_list: list of the input params
    :return: whether the params are valid or not
    and if not a matching error message
    """
    length = len(params_list)
    if length != 1:
        return False, WRONG_PARAMS_1+str(
            length)+WRONG_PARAMS_2
    return True, EMPTY_STRING


def convert_to_hex(binary_data):
    """
    the function convert the string of the
    binary number to hex string
    :b_numbers: the string of the binary number
    :return: the hex number
    """
    return hex(int(binary_data, 2))


def main():
    """
    main function
    """
    file_name = get_params()
    valid, binary_data = valid_input(file_name)
    if valid:
        print convert_to_hex(binary_data)
    else:
        print ERROR_MESSAGE


if __name__ == '__main__':
    main()