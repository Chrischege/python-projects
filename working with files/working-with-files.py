# json is a syntax for storing and exchanging data
#json is a text written with javascript notation but we can work with built in json package in python

import os
os.path.join('usr','bin','spam')
#how to join a list of filenames to the end of a folders name
myfiles=['accounts.txt','details.csv','invite.docx']
for filename in myfiles:
    print(os.path.join('c:\\Users\\chris',filename))

#getting the current working directory
dir=os.getcwd()
print(dir)
#os.chdir ('c:\\windows\\System 32')
print(dir)

#you can create new folders with the os.makedirs
#os.makedirs('c:\\delicious\\wallnut\\waffles')

'''
The os.path module provides functions for returning the absolute path of a 
relative path and for checking whether a given path is an absolute path.
•	 Calling os.path.abspath(path) will return a string of the absolute path 
of the argument. This is an easy way to convert a relative path into an 
absolute one.
•	 Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.
•	 Calling os.path.relpath(path, start) will return a string of a relative path 
from the start path to path. If start is not provided, the current working 
directory is used as the start path.
'''


