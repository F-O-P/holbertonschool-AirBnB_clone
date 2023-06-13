#!/usr/bin/python3
''' command '''
import cmd
import json
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    ''' command class '''
    prompt = '(hbnb) '
    classes = ["Review", "Place", "State", "User",
            "BaseModel", "City", "Amenity"]

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
        if class_name not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return
        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in objects:
            print('** no instance found **')
            return
        obj = objects[key]
        print(obj)

    def do_destroy(self, arg):
        ''' Deletes an instance based on the class name and id
        (save the change into the JSON file) '''
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        class_name = args[0]
        instance_id = args[1]
        if class_name not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return
        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in objects:
            print('** no instance found **')
            return
        del objects[key]
        storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all instances'''
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in objects.values() if type(obj).__name__ == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all().get(key)
        if not objects:
            print('** no instance found **')
            return
        if len(args) < 3:
            print('** attribute name missing **')
            return
        attribute_name = args[2]
        if len(args) < 4:
            print('** value missing **')
            return
        attribute_value = args[3]
        setattr(objects, attribute_name, attribute_value)
        objects.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
