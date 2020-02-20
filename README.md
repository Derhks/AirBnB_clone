# AirBnB clone - The console

- How to create a Python package
- How to create a command interpreter in Python using the `cmd` module
- What is Unit testing and how to implement it in a large project
- What is an `UUID`
- What is `*args` and how to use it
- What is `**kwargs` and how to use it



## How to create a Python package?

By performing the following steps we will create a python package:

- Create a directory and give it your package's name.
- Put your classes in it.
- Create a `__init__.py`  file in the directory

The `__init__.py` file is necessary because with this file, Python will know that this directory is a Python package directory.



## How to create a command interpreter in Python using the `cmd` module?

To create a python command interpreter you have to import the `cmd ` module 

`import cmd`

We must declare a class where we will include the methods that our command interpreter will have, these methods are also the commands that we will be able to use inside the console.

`class HBNBCommand(cmd.Cmd):`

We can use the `prompt` attribute to modify the default prompt to show the one we want to appear every time our command interpreter is executed. Additionally we can use the attribute `intro` to show a text when we execute the application.

this is the new prompt `(hbnb)`

Now let's add the `do_*` methods which will be the commands of our command interpreter.

like `do_create`

It's necessary to add documentation to the methods. To do this we can use either of the following two ways, adding the `docstrings` to each of the `do_* ` methods or adding a `help_*` method to each of the `do_*` methods.

example:

def do_create(self, arg):

```
This method creates a new instance of a given class
        and stores the dictionary representation of that object
        in a file, if the arguments are not the ones specified,
        the program will not do anything
usage: create <Basemodel type>
```

Finally we're going to implement inside our command interpreter the `End of File` to be able to exit the program so we're going to include the `do_EOF` method, which will be called when the user presses `Ctrl + d`.

within our interpreter we can use the statement

`if __name__ == "__main__":`

With this we can verify if the module has been imported or not. Besides, we can include in this condition some features that only work if the module is executed directly.



## What is Unit testing and how to implement it in a large project?

Is a framework was originally inspired by JUnit. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

The first thing we have to do is create a test file

`test_base_model.py`

inside this file we will import the unittest module

`import unittest` 

and the module we're testing

`from models.base_model import BaseModel`

Then we will declare a class that will have the keyword test and followed by the name of the class to be evaluated as 

`class Test_BaseModel(unittest.TestCase):` 

which inherits from unittest.TestCase. Now inside the class we're going to declare the methods we're going to test. Each of the methods will have the keyword test_* at the start and the name of the method we're going to test, for example 

`def test_save(self):`

then within each of the methods of our class we will use the assert methods of the TestCase class to check the correct behavior of our method. Finally we'll add at the end of our file

```
if __name__ == '__main__':
    unittest.main()
```

With these steps we will create our test module.



## What is an `UUID`

It is a module that provides immutable UUID objects, so if we want a unique ID we must call `uuid.uuid4` which creates a random UUID, this ID is stored in one instance and then assigned to an object.



## What is `*args` , `**kwargs` and how to use it

`*args` allows to pass a variable number of positional arguments, which are packaged in a single iterable object called args, this iterable object is a tuple, since this type of data is immutable and this allows the integrity of the data to be maintained.

**kwargs works the same as *args, but instead of accepting positional arguments it accepts keyword arguments, like dictionaries.

For example:

```
def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    format_tm = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, format_tm)
                elif key != '__class__':
                    setattr(self, key, value)
```



## Built With

[Python](https://www.python.org/_(programming_language)) - Programming language



## Authors

- **Adrián Hernandez [AdrianCHdz]** https://github.com/AdrianCHdz
- **Julián Sandoval [derhks]** https://github.com/Derhks



## Acknowledgments

I take this opportunity to thank each of the pages that helped us along the way to find a way to build our little program. In a special way I thank each colleague who dedicated part of his precious time helping us to resolve doubts and solve difficulties that we encountered throughout this process, thank you because it has been a challenge of great proportions.

- https://www.pythoncentral.io/how-to-create-a-python-package/
- https://code-maven.com/interactive-shell-with-cmd-in-python
- https://es.stackoverflow.com/questions/32165/qu%C3%A9-es-if-name-main
- https://docs.python.org/3/library/unittest.html
- https://docs.python.org/3/library/unittest.html#module-unittest
- https://realpython.com/python-testing/#writing-your-first-test
- https://docs.python.org/3/library/uuid.html
- https://realpython.com/python-kwargs-and-args/
- https://www.python.org/
