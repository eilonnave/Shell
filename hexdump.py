# -*- coding: utf-8 -*-
import sys
import os
EMPTY_STRING = ''
WRONG_PARAMS_1 = 'The function hexdump should receive 1 param '
WRONG_PARAMS_2 = ' is given'
FILE_IS_NOT_EXCISE = 'Can not locate the given file- '
SPACE = ' '
VALUE_ERROR_MESS = 'Invalid data from the file or the buffer'


def get_params():
    """
    the function gets the input params
    from the user
    :return: list of the giving params
    """
    params_list = sys.argv[1:]
    return params_list


def valid(params_list):
    """
    the function returns true if the
    params are valid, otherwise false
    :param params_list: list of the input params
    :return: whether the params are valid or not
    and if not a matching error message
    """
    global insert_stdin
    length = len(params_list)
    if length == 1:
        file_path = params_list[0]
        if os.path.isfile(file_path):
            return True, EMPTY_STRING
        else:
            return False, FILE_IS_NOT_EXCISE+file_path
    elif length == 0:
        insert_stdin = sys.stdin.read()
        if insert_stdin is not EMPTY_STRING:
            return True, EMPTY_STRING
    return False, WRONG_PARAMS_1+str(
        length)+WRONG_PARAMS_2


def convert_to_hex(binary_data):
    """
    the function convert the string of the
    binary number to hex string
    :b_numbers: the string of the binary number
    :return: the hex number
    """
    return hex(int(binary_data, 2))


def execute_function(params_list):
    """
    the function return matching input for the user
    according to the receiving params
    :param params_list: the list of the input
    params
    :return: matching output
    """
    if len(params_list) == 0:
        binary_data = insert_stdin
    else:
        file_path = params_list[0]
        with open(file_path, 'rb') as file_handle:
            binary_data = file_handle.read()
    hex_data = convert_to_hex(binary_data)
    return hex_data


def main():
    """
    main function
    """
    params_list = get_params()
    is_valid, mess = valid(params_list)
    if is_valid:
        print execute_function(params_list)
    else:
        print mess


if __name__ == '__main__':
    with open('assert bin.txt', 'w') as assert_file_handle:
        assert_file_handle.write('11110000')
    assert_params_list = ['assert bin.txt']
    assert valid(assert_params_list)[0]
    assert execute_function(
        assert_params_list).find('f0') != -1
    assert execute_function(
        assert_params_list).find('ff') == -1
    os.remove('assert bin.txt')
    assert not valid(assert_params_list)[0]
    main()
