print("Commands:")
print("[list] for the list of movies")
print("[edit] for changing and deleting elements in the list")
print("[sort] for sorting the movies")
print("[search] for searching if the movie exixts")
print("[quit] to exit")

loop = True #enter the loop
chance = 3 #number of invalid commands permitted
while loop == True:
    c=input("Type in your anticipated action:")

    if c == "list":
        
    elif c == "edit":

    elif c == "sort":

    elif c == "search":

    elif c == "quit":
        loop = False
    else:
        print("Your command is invalid, please try again.\n You have " + n + " more chances.")
        if chance = 0:
            loop = False
        chance-=1
