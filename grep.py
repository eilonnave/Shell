# -*- coding: utf-8 -*-
import sys
import os
EMPTY_STRING = ''
WRONG_PARAMS_1 = 'The function grep should receive 1 param '
WRONG_PARAMS_2 = ' is given'
FILE_IS_NOT_EXCISE = 'Can not locate the given file- '
SPACE = ' '
NEXT_LINE = '\n'


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
    length = len(params_list)
    if length == 2:
        file_path = params_list[0]
        if os.path.isfile(file_path):
            return True, EMPTY_STRING
        else:
            return False, FILE_IS_NOT_EXCISE+file_path
    elif length == 1:
        global insert_stdin
        insert_stdin = sys.stdin.read()
        if insert_stdin is not EMPTY_STRING:
            return True, None
    return False, WRONG_PARAMS_1+str(
        length)+WRONG_PARAMS_2


def execute_function(params_list):
    """
    the function return matching input for the user
    according to the receiving params
    :param params_list: the list of the input
    params
    :return: matching output
    """
    if len(params_list) == 1:
        file_data = insert_stdin
        find_string = params_list[0]
    else:
        with open(params_list[0], 'r') as file_handle:
            file_data = file_handle.read()
        find_string = params_list[1]
    return_string = ''
    file_data = file_data.split(NEXT_LINE)
    for line in file_data:
        if line.find(find_string) != -1:
            return_string += line+NEXT_LINE
    return return_string


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
    with open('hello world.txt', 'w') as assert_file_handle:
        assert_file_handle.write('hello world\nI am eilon')
    assert_params_list = ['hello world.txt', 'hello']
    assert valid(assert_params_list)[0]
    assert execute_function(
        assert_params_list) == 'hello world\n'
    assert_params_list = ['hello world.txt', 'am']
    assert execute_function(
        assert_params_list) == 'I am eilon\n'
    assert not execute_function(
        assert_params_list) == 'hello world\n'
    assert_params_list = ['hello world.txt', 'e']
    assert execute_function(
        assert_params_list) == 'hello world\nI am eilon\n'
    os.remove('hello world.txt')
    assert not valid(assert_params_list)[0]
    main()
