#!/usr/bin/python3
"""
hbnb terminal app
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    methods for the basic controls of the hbnb terminal app
    """
    prompt = '(hbnb)'

    def do_quit(self, *args):
        """
        use quit to exit the terminal
        """
        return True

    def do_EOF(self, *args):
        """
        use ctrl+d (EOF) to exit the terminal
        """
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
