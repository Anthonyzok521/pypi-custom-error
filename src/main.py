'''
Test of the module Custome Error
'''
from custom_error import Error

if __name__ == '__main__':
    try:
        number:float = -0.2

        if number < 0.0 or number > 1.0:
            raise Error("Only ranges between 0.0 and 1.0 are allowed", "Invalid Range")
    except Error as e:
        print(e.info())

    err = Error('Erro1')
    print(err.info())

    print(Error("Error 2", "Test").info())
