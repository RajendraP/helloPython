import logging
from src.main.hello_world import HelloWorld
from hamcrest import assert_that, equal_to


class TestHelloWorld(object):
    logging.basicConfig(filename='hello_python.log', level=logging.INFO)
    logging.info('Started')

    def test_hello_world(self):
        """
         HelloWorld positive test
        """
        assert HelloWorld.say_hello() == 'Hello World'

    def test_hello_world_failed(self):
        """
        HelloWorld -ve test
        """
        # jiraReservedChars = "[\\.\\,\\;\\?\\|\\*\\/\\%\\^\\\\\$\\#\\@\\[\\]]"

        assert HelloWorld.say_hello() == 'TBI9FPQXIB9EQFH2YSSTN3HOOHHY7SQX2YJI2S2NZT9WAXSHQBTPG3FXDZALNJCPC5KL6G1CV0DFU9G95524AR51CJFAAR818ROX3NOCF3NEEVY9GSO7UFHKIFVQ2NGZ78Y5WSHXA7GWOAKB6JU4E86JOQET2A8DV9JD1RQVGU3RCU7NMAZZVIYTZDXPTGOZZDGZV5HAHP9L9ZAQ2W4JEAZU8VK5C8SEODU2NNTKXDWVJOXOV5KK4UP3CUVYM4E', 'TBI9FPQXIB9EQFH2YSSTN3HOOHHY7SQX2YJI2S2NZT9WAXSHQBTPG3FXDZALNJCPC5KL6G1CV0DFU9G95524AR51CJFAAR818ROX3NOCF3NEEVY9GSO7UFHKIFVQ2NGZ78Y5WSHXA7GWOAKB6JU4E86JOQET2A8DV9JD1RQVGU3RCU7NMAZZVIYTZDXPTGOZZDGZV5HAHP9L9ZAQ2W4JEAZU8VK5C8SEODU2NNTKXDWVJOXOV5KK4UP3CUVYM4E'

    def test_hello_world_next_failed(self):
        """
        HelloWorld another -ve test
        """
        assert_that(HelloWorld.say_hello(), equal_to('hello'), '{} {}'.format(HelloWorld.say_hello(), 'hello'))

    logging.info('Finished')

    def test_hello_world_1(self):
        """
         HelloWorld positive test
        """
        assert HelloWorld.say_hello() == 'HelloWorld'


    def test_hello_world_next_failed_2(self):
        """
        HelloWorld another -ve test 2 failed
        """
        assert_that(HelloWorld.say_hello(), equal_to('hello'), '{} '.format('hello'))

    logging.info('Finished')
