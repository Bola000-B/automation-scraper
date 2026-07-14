# -------------------
# -- file Handling --
# -------------------
# "a" Append    open file for appending values, create file if not exists
# "r" Read      [default value] open file for read and give error if file is not exists
# "w" Write     open file for writing, create file if not exists
# "x" Creat     create file, give error if file exists
# ----------------------------------------------------
# [65]

import os

print(os.getcwd()) 

print(os.path.dirname(os.path.abspath(__file__)))

print(os.path.abspath(__file__))

# file = open("osama.txt", "w")
