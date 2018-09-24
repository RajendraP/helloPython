from hello_python.src.main.hello_world import HelloWorld


class TestHelloWorld(object):
    def test_hello_world(self):
        """
         HelloWorld positive test
        """
        assert HelloWorld.say_hello(), 'Hello World'

    def test_hello_world_failed(self):
        """
        HelloWorld -ve test
        """
        assert HelloWorld.say_hello(), 'world'

    def test_hello_world_next_failed(self):
        """
        HelloWorld another -ve test
        """
        assert HelloWorld.say_hello() == 'hello'
