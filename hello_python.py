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


hello_python = HelloPython()
hello_python.hello_python()
hello_python.hello_user('Peter')
