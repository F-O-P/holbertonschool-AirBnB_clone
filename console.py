#!/usr/bin/python3
''' command '''
import cmd
import json
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    ''' command class '''
    prompt = '(hbnb) '
    missing = "** class name missing **"
    unknown = "** class doesn't exist **"

    def do_quit(self, arg):
        ''' quit command '''
        return True
    
    def do_EOF(self, arg):
        ''' EOF command '''
        return True
    
    def do_help(self, arg):
        ''' help command '''
        cmd.Cmd.do_help(self, arg)
    
    def emptyline(self):
        ''' empty line '''
        pass

    def do_create(self, arg):
        ''' creates a new instance of BaseModel 
        saves it (to the JSON file) and prints the id'''
        if len(arg) == 0:
            print("** class name missing **")
            return
        else:
            try:
                instance = eval(arg)()
                instance.save()
                print(instance.id)
            except NameError:
                print("** class doesn't exist **")
                return

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        class_name = args[0]
        instance_id = args[1]
        if class_name not in HBNBCommand.class_list:
            print('** class doesn\'t exist **')
            return
        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in objects:
            print('** no instance found **')
            return
        obj = objects[key]
        print(obj)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
