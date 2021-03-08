from add_to_like import *
from Function import *

print("Commands:")
print("[list] for the list of movies")
print("[edit] for changing and deleting elements in the list")
print("[sort] for sorting the movies")
print("[search] for searching if the movie exixts")
print("[quit] to exit")
print("[output] to write your movielist into your_movie_list.txt")
print('Warning! Use [search] before [edit]')

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
            print(Result)
            print('type in the name of those movies that you want to add')
            print('type [quit] if you want to end editing')
            instruction = input()
            while instruction != 'quit':
                movielist.append(instruction)
                print('Successfully added!')
        elif edit_c=="D":
            for i in movielist:
                print(i)
            print('type in the movies that you want to delete')
            print('type [quit] if you want to end deleting')
            instruction = input()
            while instruction != 'quit':
                movielist.remove(instruction)
                print('Successfully deleted!')
    if c == "sort":
        sorting_alphabet(movielist)
    if c == "search":
        print('Use _ (underline) to denote space')
        item = input('Type in key words:')
        StringInsideString(item,FileIntoList("database.txt"))
    if c == 'output':
        Output(movielist)
    if c == "quit":
        break
    
    else:
        print("Your command is invalid, please try again.\n You have " + n + " more chances.")
        if chance==0:
            loop = False
        chance-=1
