# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import argparse
import logging


class BaseCommand(object):

    description = None

    def __init__(self):
        self.command_name = self.__class__.__module__.split(".")[-1]
        self.logger = logging.getLogger("commands.{}".format(self.command_name))

    def add_arguments(self, parser):
        pass

    def execute(self, argv, entry_file):
        parser = argparse.ArgumentParser(
            description=self.description,
            prog='{} {}'.format(entry_file, self.command_name)
        )
        self.add_arguments(parser)
        args_namespace = parser.parse_args(argv)
        self.handle(**vars(args_namespace))

    def handle(self, *args, **kwargs):
        raise NotImplemented()
