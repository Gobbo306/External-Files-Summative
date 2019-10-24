#------------------------------------------------
#Dylan Friesen
#External Files Mini Game
#Tuesday October 22 2019
#------------------------------------------------

#------------------Benefits & Specific Uses----------------------

#The benefits of using external files are quite extensive. It is great for operating games with
#save games, it can be used to clean up your code, in terms of removing the large lists from
#the program itself and moving into the external files, and it can also give the player or user
#a easier way to view the contents of what they have, instead of having a list in the program,
#they can just choose and option to call on all the contents of the appropriate file.

#They are a fair amount of uses for External files, from making save games, to running lists,
#You can control your gamesfrom outside of the game, instead of having those long winded,
#print this print that, to explain part of a game or a story, you can just write it all into a part of the,
#file, and print that, boom, so many less program lines used.

#--------------------Functions-------------------

def character_creation(): #deciding what their name, race and gender are, and writing that into file
    print("opening file")
    name = input("What is your name?")
    race = input("What is your race?")
    gender = input("What is your gender?")
    file = 'character' + '.txt'
    Randall = open(file, 'w')
    Randall.write("Name, ")
    Randall.write(name + ", ")
    Randall.write("Race, ")
    Randall.write(race + ", ")
    Randall.write("Gender, ")
    Randall.write(gender + ", ")
    Randall.close()
    print("closing file")
    
def weapon_selection():
    print("opening file")
    weapon = input("what weapon do you want to use?")
    file = open('character.txt', 'a')
    file.write("Weapon, ")
    file.write(weapon + ", ")
    file.close()
    print("closing file")

def look():
    file = open('character.txt', 'r')
    print("opening file")
    all_lines = file.read()
    print(all_lines)
    file.close()
    print("closing file")
    
def main():
    character_creation()
    weapon_selection()
    look()
    
#------------------------main code---------------
    
main()