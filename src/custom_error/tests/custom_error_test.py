'''
Testing the Module Custom Error
'''
import unittest
from custom_error import Error

class CustomErrorTest(unittest.TestCase):
    '''
        Class CustomErrorTest
    '''
    def test_instance_error(self) -> None:
        '''Is equal to the message'''

        err = Error('message error', 'test instance')
        self.assertEqual('Error: message error - Type: test instance', err.info())

    def test_try_except(self) -> float | str:
        '''Using try-except'''
        try:
            a = 1
            b = 0
            if b != 0:
                return a / b
            raise Error('division by zero')
        except Error as err:
            self.assertEqual('Error: division by zero ', err.info())
            return err.info()

if __name__ == '__main__':
    unittest.main()
