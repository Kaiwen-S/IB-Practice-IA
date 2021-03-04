from add_to_like import *
from Function import *

print("Commands:")
print("[list] for the list of movies")
print("[edit] for changing and deleting elements in the list")
print("[sort] for sorting the movies")
print("[search] for searching if the movie exixts")
print("[quit] to exit")

movielist=[]

loop = True #enter the loop
chance = 3 #number of invalid commands permitted
while loop == True:
    c=input("Type in your anticipated action:")

    if c == "list":
        print(movielist)
    
    if c == "edit":
        edit_c=input("If you want to add, type [A}; if you want to delete, type [D}.")
        if edit_c=="A":
            
        if edit_c=="D":
    else:
        print("Your command is invalid, please try again.\n You have " + n + " more chances.")
        if chance==0:
            loop = False
        chance-=1
