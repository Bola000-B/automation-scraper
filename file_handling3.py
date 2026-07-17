# -----------------------------------------------
# -- file Handling => Write and Append In File --
# -----------------------------------------------

my_file = open(r"C:\Users\PC-2024\Desktop\my program\automation-scraper\bola.txt", "w")
# my_file.write("Hello From Python File With Love\n: ")
# my_file.write("third line")


# my_file.write("Elzero web School\n " *1999)

my_lsit = ["osama\n", "Ahmed\n", "Sayed\n"]

my_file.writelines(my_lsit)