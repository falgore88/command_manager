# -*- coding: utf-8 -*-
from __future__ import unicode_literals


if __name__ == '__main__':
    from command_manager import Manager
    manager = Manager(["commands"])
    manager.run()
