"""
The mod module
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
        print self.user_name
    def hello_python(self):
        """
        A method defination, always called with instance, requires to pass self.
        """
        print self.user_name

def hello_python():
    """
    A function defination, doesn't require instance to call.
    """
    print 'Hello Python!!'


HELLOPYTHON = HelloPython('Peter')
HELLOPYTHON.hello_user()

hello_python()

