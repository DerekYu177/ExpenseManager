#!/usr/bin/python2.7

from modules.data_transfer_service import DataTransferService

def main():
    servicer = DataTransferService()
    servicer.begin()

if __name__ == '__main__':
    main()
