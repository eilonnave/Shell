# -*- coding: utf-8 -*-
import os.path
import subprocess
PATH_1 = 'C:/Windows/System32'
PATH_2 = '.'
RECEIVE_COMMAND_MESS = '> Enter command\n'
SPACE = ' '
FILE_ENDING = '.exe'
FILE_ENDING_PYTHON = '.py'
COMMAND_IS_NOT_EXCISE = 'Can not find the inputted command'


def receive_command():
    """
    the function receives the command-file name
    to execute and the params
    :return: the command name and the params
    """
    input_line = raw_input(RECEIVE_COMMAND_MESS)
    input_line = input_line.split(SPACE)
    command = input_line[0]
    params = input_line[1:]
    return command, params


def search_command(command):
    """
    the function checks if the command is
    an excise file and return the path of it
    if  does or error message if not
    """
    path = PATH_1
    path += '/'+command+FILE_ENDING
    if os.path.isfile(path):
        return True, path
    path = PATH_2
    path += '/'+command+FILE_ENDING_PYTHON
    if os.path.isfile(path):
        return True, path
    return False, COMMAND_IS_NOT_EXCISE


def main():
    """
    main function
    """
    while True:
        command, params = receive_command()
        is_find, path = search_command(command)
        if is_find:
            if path.split('/')[-1].split('.')[-1] == FILE_ENDING[1:]:
                call_list = [path]
                for param in params:
                    call_list.append(param)
                subprocess.call(call_list)
            else:
                call_list = ['python', path]
                for param in params:
                    call_list.append(param)
                subprocess.call(call_list)
        else:
            error_mess = path
            print error_mess


if __name__ == '__main__':
    main()