#!/usr/bin/python2.7

# built-in classes
import Modules.data_transfer_service as servicer

def main(input_args):
    servicer.begin()

if __name__ == '__main__':
    main(sys.argv[1:])

class CLI:
    def __init__(self, input_args):
        pass
