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

        if args in models.available_classes:
            new_model = models.available_classes[args]()
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
        elif show_split[0] not in models.available_classes:
            print("** class doesn't exist **")
        else:
            stored_key = "{}.{}".format(show_split[0], show_split[1])

            stored_data = models.storage.all()

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
        elif show_split[0] not in models.available_classes:
            print("** class doesn't exist **")
        else:
            stored_data = models.storage.all()

            for i in stored_data:

                if i == "{}.{}".format(show_split[0], show_split[1]):
                    del stored_data[i]
                    models.storage.save()
                    return
            print("** no instance found **")
            models.storage.save()

    def do_all(self, args):
        """
        outputs all instances as strings
        Usage: all
               all BaseModel
        """
        show_split = args.split()
        if len(show_split) >= 1:
            if show_split[0] not in models.available_classes:
                print("** class doesn't exist **")
            else:
                for i in models.storage.all():
                    print(i)
        else:
            for i in models.storage.all():
                print(i)

    def do_update(self, args):
        """
        updates the base model with new info
        Usage: Update BaseModel <info>
        """
        show_split = args.split()
        stored_data = models.storage.all()
        if class_name not in ['BaseModel', 'City', 'State',
                        'User', 'Review', 'Place',
                        'Ameinity']:
            print(**class doesnt exist**)
        if len(show_split) == 0:
            print("** class name missing **")
        if len(show_split) == 1:
            if show_split[0] not in models.available_classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        if len(show_split) == 2:
            if show_split[0] not in models.available_classes:
                print("** class doesn't exist **")
            else:
                print("** attribute name missing **")
        if len(show_split) == 3:
            print("** value missing **")
        if len(show_split) == 4:
            for i in stored_data:
                if i == "{}.{}".format(show_split[0], show_split[1]):
                    stored_obj = stored_data.get(i)
                    setattr(stored_obj, show_split[2], show_split[3])
                    models.storage.save()
                    return
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
