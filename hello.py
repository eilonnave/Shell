# -*- coding: utf-8 -*-
import sys
import getpass
EMPTY_STRING = ''
WRONG_PARAMS_1 = 'The function hello should receive 0 param '
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
    if length != 0:
        return False, WRONG_PARAMS_1+str(
            length)+WRONG_PARAMS_2
    return True, EMPTY_STRING


def execute_function():
    """
    the function return hello + the user name
    :return: hello + the user name
    """
    name = getpass.getuser()
    return 'hello '+name


def get_params():
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
    params_list = get_params()
    is_valid, mess = valid(params_list)
    if is_valid:
        print execute_function()
    else:
        print mess


if __name__ == '__main__':
    assert not valid(['null', 'null'])[0]
    assert valid([])[0]
    main()
