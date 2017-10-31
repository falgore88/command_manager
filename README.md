command_manager
===================


Entry point for Python scripts.
Helps you structure additional scripts of your application within one or more Python packages and call them from one place.

Installation
-------------
Install using `pip`...

    pip install command_manager

Using
-------------------
Create a Python package anywhere in your application.

For example, the package `commands` and the entry point `manager.py`

    .
    ├── commands
    │   ├── __init__.py
    │   └── my_first_command.py
    ├── src
    └── manager.py

In `manage.py` add the following:

    if __name__ == '__main__':
        import logging.config # Optional for logging
        from command_manager import Manager

        logging.config.dictConfig(settings.LOGGING) # Optional for logging
        manager = Manager(["commands"])
        manager.run()

In `my_first_command.py` add the following:

    from command_manager.commands import BaseCommand
    
    
    class Command(BaseCommand):
    
        description = "Simple command"
    
        def add_arguments(self, parser):
            parser.add_argument("--arg1", help="argument arg1")
            parser.add_argument("--arg2", help="argument arg2")
    
        def handle(self, *args, **kwargs):
            print "Hello Word: arg1={arg1} arg2={arg2}".format(**kwargs)

> **Warning:**
> The class must be called the `Command` and inherited from `BaseCommand`

Now call `manage.py` from the console.
![python manage.py](/asserts/manage.png)

Call our command `my_first_command.py`
![python manage.py my_first_command](/asserts/command_call.png)
