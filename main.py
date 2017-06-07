
"""
Usage: DojoSpaceR>>>
DojoSpaceR>>> create_room <room_type> <room_name>...
DojoSpaceR>>> add_person <person_type> <first_name> <surname> [<wants_accommodation>]
DojoSpaceR>>> quit
DojoSpaceR>>> (-i | --interactive)
DojoSpaceR>>> (-h | --help)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo import DojoRoomAllocator


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            """Thrown for mismatched args.
            Prints the following message, and the applicable 'Usage' code block."""

            print("Something went wrong. Please use the following format.\n")
            print(e)
            return

        except SystemExit:
            """Prints the exit message as when 'quit' is called"""
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class DojoSpaceAllocator(cmd.Cmd):
    intro = """
      Welcome to the myDOJO SPACE ALLOCATOR APP. What would you like to do?
      Please type an applicable command.(See above for applicable commands)\n
       """
    prompt = 'DojoSpaceR' \
             '>>>'
    dojo = DojoRoomAllocator()

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        for i in arg['<room_name>']:
            (self.dojo.create_room(arg['<room_type>'], i))

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <person_type> <first_name> <surname> [<wants_accommodation>]"""
        if arg['<wants_accommodation>'] is None:
            arg['<wants_accommodation>'] = "n"
            (self.dojo.add_person(arg['<person_type>'], arg['<first_name>'], arg['<surname>'],
                                  "n"))
        else:
            (self.dojo.add_person(arg['<person_type>'], arg['<first_name>'], arg['<surname>'],
                                  arg['<wants_accommodation>']))

    def do_quit(self, arg):
        """Usage: quit"""
        print("Session has been terminated.\n")
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        print(__doc__)
        DojoSpaceAllocator().cmdloop()
    except KeyboardInterrupt:
        print("Exiting App...")