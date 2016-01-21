# pylint: disable=R0201
'''
@author: rajendrap
'''
class HelloPython(object):
    '''
    hello world in python
    '''
    def __init__(self):
        pass
    def hello_python(self):
        '''
        method doc string
        '''
        print 'Hello Python!!'
    def hello_user(self, user_name):
        '''
    	print hello with user name
    	'''
        print user_name


HELLOPYTHON = HelloPython()
HELLOPYTHON.hello_python()
HELLOPYTHON.hello_user('Peter')
