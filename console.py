#!/usr/bin/python3
"""
hbnb terminal app
"""
import cmd
from models.base_model import BaseModel
import models

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

    def do_create(self, args):
        """
        creates an object of class BaseModel
        usage: create BaseModel
        """
        #print(args)
        if args == 'BaseModel':
            new_model = BaseModel()
            print("{}".format(new_model.id))
        elif not args:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        prints the string representation of the object
        Usage: show BaseModel 1234-1234-1234
        """
        show_split = args.split()
        if len(show_split) == 0:
            print("** class name missing **")
        elif len(show_split) == 1:
            print("** instance id missing **")
        elif show_split[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            stored_key = "{}.{}".format(show_split[0], show_split[1])
            #print(stored_key)
            stored_data = models.storage.all()
            #print(stored_data)
            if stored_key in stored_data:
                print(stored_data[stored_key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        removes an object of the class
        Usage: destroy BaseModel 121212
        """
        show_split = args.split()
        if len(show_split) == 0:
            print("** class name missing **")
        elif len(show_split) == 1:
            print("** instance id missing **")
        elif show_split[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            stored_data = models.storage.all()
            #print(stored_data)
            for i in stored_data:
                #print("i is: {}".format(i))
                if i == "BaseModel.{}".format(show_split[1]):
                    del stored_data[i]
                    models.storage.save()
            print("** no instance found **")
            models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
