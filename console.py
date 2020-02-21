#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Documentation"""
    prompt = '(hbnb) '
    class_types = ["BaseModel", "State", "User",
                   "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quits the console
        """
        return True

    def do_EOF(self, arg):
        """Quits the console
        """
        return True

    def emptyline(self):
        """This Function avoids the programm to be killed everytime
        a emptyline is typed in the command line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
