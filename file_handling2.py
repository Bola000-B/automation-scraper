# --------------------------------
# -- File Handling => Read File --
# --------------------------------
# [66]
# [r] == read
import os

my_file = open(r"C:\Users\PC-2024\Desktop\my program\automation-scraper\bola.txt","r")

# print(my_file) # File Data Object
# print(my_file.name)
# print(my_file.mode) 
# print(my_file.encoding) 


# print(my_file.read())  # For Read all in bola.txt
# print(my_file.read(5)) # Print the first 5 character

# print(my_file.readline(2)) #    read the first 2 character
# print(my_file.readline())  # continue the line after 2 character
# print(my_file.readline())  # read the new line    # the next line



# print(my_file.readlines())      # read the all line in txt and return in list
# print(my_file.readlines(52)) 

# print(type(my_file.readlines())) 

for line in my_file:
    print(line)

    if line.startswith("03"):
        break

# # Close the Flie
# my_file.close()