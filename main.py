# -*- coding: utf-8 -*-
import os.path
import subprocess
import sys
PATH_1 = 'C:/Windows/System32'
PATH_2 = '.'
RECEIVE_COMMAND_MESS = '> Enter command\n'
SPACE = ' '
FILE_ENDING = '.exe'
FILE_ENDING_PYTHON = '.py'
COMMAND_IS_NOT_EXCISE = 'Can not find the inputted command- '
PIPE_SIGN = '|'
EMPTY_STRING = ''
ERROR_MESS = 'Error with the command- '


def receive_commands():
    """
    the function receives the command-file name
    to execute and the params. The function supports
    several commands using pipes
    :return: list of the commands or command name and the params
    """
    input_line = raw_input(RECEIVE_COMMAND_MESS)
    input_line = input_line.split(PIPE_SIGN)
    commands = []
    for part in input_line:
        sub_part = part.split(SPACE)
        while EMPTY_STRING in sub_part:
            sub_part.remove(EMPTY_STRING)
        command = sub_part[0]
        params = sub_part[1:]
        commands.append((command, params))
    return commands


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


def start_process(params, path, insert_stdin):
    """
    the function starts the processes
    according to the giving params
    :param params: the list of the params for
    the process
    :param path: the full path of the command
    :param insert_stdin: the stdin object to run the program with
    :return: the process object
    """
    if path.split('/')[-1].split('.')[-1] == FILE_ENDING[1:]:
        call_list = [path]
    else:
        call_list = ['python', path]
    for param in params:
        call_list.append(param)
    return subprocess.Popen(call_list,
                            stdout=subprocess.PIPE,
                            stdin=insert_stdin,
                            stderr=subprocess.PIPE)


def handle_process_output(ps, command):
    """
    the function handles the process
    output and error
    :param ps: the process that has run
    :param command: the name of the process
    command
    :return: the output from the process
    and whether there was an error
    """
    recv_stdout = ps.stdout
    recv_stderr = ps.stderr.read()
    is_error = False
    if recv_stderr != EMPTY_STRING:
        print ERROR_MESS+command+'- '+recv_stderr
        is_error = True
    return recv_stdout, is_error


def search_commands(commands):
    """
    the function checks if all the
    commands for the processes excise
    :param commands: the list of the commands
    :return: update list of the commands
    with the path for each command. If command
    is not find than the function returns False
    """
    for command in commands:
        is_find, path = search_command(command[0])
        if is_find:
            commands[commands.index(command)] = (
                command[0], command[1], path)
        else:
            not_find_mess = path
            print not_find_mess+command[0]
            return False, command
    return True, commands


def main():
    """
    main function
    """
    while True:
        is_find, commands = search_commands(
            receive_commands())
        is_error = not is_find
        insert_stdin = None
        if not is_error:
            for command in commands:
                if not is_error:
                    ps = start_process(command[1], command[2], insert_stdin)
                    insert_stdin, is_error = handle_process_output(
                        ps, command[0])
            if not is_error:
                print insert_stdin.read()


if __name__ == '__main__':
    main()
