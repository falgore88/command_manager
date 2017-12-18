# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from command_manager.commands import BaseCommand


class Command(BaseCommand):

    description = "Simple command"

    def add_arguments(self, parser):
        parser.add_argument("--arg1", help="argument arg1")
        parser.add_argument("--arg2", help="argument arg2")

    def handle(self, *args, **kwargs):
        print("Hello Word: arg1={arg1} arg2={arg2}".format(**kwargs))
