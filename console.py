#!/usr/bin/python3
''' command '''
import cmd

class HBNBCommand(cmd.Cmd):
    ''' command class '''
    prompt = '(hbnb) '

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
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
