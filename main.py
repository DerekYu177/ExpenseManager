#!/usr/bin/python2.7

# built-in classes
from m.data_transfer_service import DataTransferService

def main():
    servicer = DataTransferService()
    servicer.begin()

if __name__ == '__main__':
    main()
