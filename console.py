#!/usr/bin/python3
''' command '''
import cmd

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
        ''' creates a new instance of BaseModel '''
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            from models.base_model import BaseModel
            new = BaseModel()
            new.save()
            print(new.id)
    
    def do_show(self, arg):
        ''' prints the string representation of an instance 
        based on the class name and id '''
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            from models.base_model import BaseModel
            print(BaseModel())
    
    def do_destroy(self, arg):
        ''' deletes an instance based on the class name and id '''
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            from models.base_model import BaseModel
            new = BaseModel()
            new.save()
            print(new.id)

    def do_all(self, arg):
        ''' prints all string representation of all instances
        based or not on the class name '''
        if arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            from models.base_model import BaseModel
            print(BaseModel())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
