# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

from exceptions import DuplicateCommandNameException
from utils import (COLORS, colored_string, get_files, import_string,
                   print_console)


class Manager(object):

    def __init__(self, command_modules):
        self.command_modules = [command_module.replace('.', os.path.sep) for command_module in command_modules]
        self.entry_file = os.path.basename(__file__)

    def run(self):
        argv = sys.argv
        try:
            commands = self.get_commands()
        except DuplicateCommandNameException as e:
            print_console('Error: {}'.format(unicode(e)), color=COLORS.RED)
            return

        if len(argv) < 2 or (len(argv) == 2 and argv[1] in ("-h", "--help")):
            self._print_commands_list(commands)
        else:
            command_name = argv[1]
            command_args = argv[2:]
            if not commands.get(command_name):
                print_console('Error: Command "{}" not found.'.format(command_name), color=COLORS.RED)
                return
            command = commands[command_name]()
            command.execute(command_args, self.entry_file)

    def get_commands(self):
        commands = {}
        for commands_module in self.command_modules:
            for command_file_path in get_files(commands_module, recursive=True, extension='py'):
                if not command_file_path.endswith("__init__.py"):
                    command_path, command_file = os.path.split(command_file_path)
                    command_name, _ = os.path.splitext(command_file)
                    command_module = os.path.join(command_path, command_name, "Command").replace(os.path.sep, ".")
                    try:
                        if commands.get(command_name):
                            raise DuplicateCommandNameException('Duplicate command name in {}.'.format(command_module))
                        commands[command_name] = import_string(command_module)
                    except ImportError:
                        print_console("Warning: Error import {}".format(command_module), color=COLORS.YELLOW)
        return commands

    def _print_commands_list(self, commands):
        print_console("Registered commands", color=COLORS.WHITE)
        print_console("{:<50} {:<100}".format(colored_string("Name", color=COLORS.CYAN), colored_string("Description", color=COLORS.CYAN)))
        for command_name, command_class in commands.items():
            print_console("{:<50} {:<100}".format(
                colored_string(command_name, color=COLORS.GREEN),
                colored_string(getattr(command_class, "description", "-") or "-", color=COLORS.WHITE)
            ))
