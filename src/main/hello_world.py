"""
The HelloPython module
@author: rajendrap
@date: Jan 31, 2016
"""


class HelloPython(object):
    """
    hello world in python
    """
    def __init__(self, user_name=None, user_age=None):
        self.user_name = user_name
        self.user_age = user_age

    def hello_user(self):
        """
        A method defination, always called with instance, requires to pass self.
        """
        print(self.user_name)

    def hello_python(self):
        """
        A method defination, always called with instance, requires to pass self.
        """
        print(self.user_name)


def hello_python():
    """
    A function definition, doesn't require instance to call.
    """
    print('Hello Python!!')


HELLO_PYTHON = HelloPython('Peter')
HELLO_PYTHON.hello_user()

hello_python()

