'''
Testing the Module Custom Error
'''
from custom_error import Error
import unittest

class CustomErrorTest(unittest.TestCase):
    '''
        Class CustomErrorTest
    '''
    def test_instance_error(self):
        '''Is equal to the message'''

        err = Error('message error', 'test instance')
        self.assertEqual('Error: message error - Type: test instance', err.info())

if __name__ == '__main__':
    unittest.main()
