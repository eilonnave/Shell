# -*- coding: utf-8 -*-
import sys
EMPTY_STRING = ''
WRONG_PARAMS_1 = 'The function should receive 1 param '
WRONG_PARAMS_2 = ' is given'


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


def execute_function(params_list):
    """
    the function return matching input for the user
    according to the receiving params
    :param params_list: the list of the input
    params
    :return: matching output
    """
    name = params_list[0]
    return 'hello '+name


def input_params():
    """
    the function gets the input params
    from the user
    :return: list of the giving params
    """
    return sys.argv[1:]


def main():
    """
    main function
    """
    params_list = input_params()
    is_valid, mess = valid(params_list)
    if is_valid:
        print execute_function(params_list)
    else:
        print mess


if __name__ == '__main__':
    assert not valid(['null', 'null'])[0]
    assert valid(['null'])[0]
    assert execute_function(
        ['null']).find('null') != -1
    main()