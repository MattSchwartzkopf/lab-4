"""upload_client.py

    Run python autograder.py
    
TODO -- complete header docstring

Champlain College CSI-235, Spring 2018
This code builds off skeleton code written by 
Prof. Joshua Auerbach (jauerbach@champlain.edu)
"""

"""
Author:              Brian Nguyen And Matthew Schwartzkopf
Class:               CSI-235
Assignment:          Lab 3
Date Assigned:       Feb 2, 2018
Due Date:            March 2,2018 11:59 PM

Description:


This code has been adapted from that provided by Prof. Joshua Auerbach: 

Champlain College CSI-235, Spring 2018
The following code was written by Joshua Auerbach (jauerbach@champlain.edu)


"The following code are provided by Prof. Joshua Auerbach"
"And modified by Brian Nguyen"

"""

import argparse
import socket
import os
import constants

class UploadError(Exception):
    """Throws exception if there is an issue when uploading"""
    pass

    
class UploadClient:
    # TODO document this class and implement the specified functions
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.stored = b''
    
    def close(closer):
        closer.socket.close()
    
    def recv_all(self, length):
        receive_data = b''
        data = b''
        while(len(data) < length):
            receive_data = self.socket.recv(length - len(data))
            if not receive_data:
                raise UploadError()
            data += receive_data
        return data
    
    def recv_until_delimiter(self, byte):
        words = self.stored
        # Gets all the words being sent
        
        while byte not in words:
            # Gets all the words, but overwrites and adds the delimiter at the end
            words += self.socket.recv(constants.MAX_BYTES)
            
        fields = words.split(byte, 1)
        self.stored = fields[1]
        return(fields[0])
        


if __name__ == '__main__':    
    parser = argparse.ArgumentParser(description='TCP File Uploader')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=8900,
                        help='TCP port (default 8900)')
    args = parser.parse_args()
    upload_client = UploadClient(args.host, args.p)
    upload_client.upload_file("upload_client.py")
    print(upload_client.list_files())
    upload_client.close()
