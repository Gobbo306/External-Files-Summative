#------------------------------------------------
#Dylan Friesen
#External Files Mini Game
#Tuesday October 22 2019
#------------------------------------------------

#-------------------Imports----------------------


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