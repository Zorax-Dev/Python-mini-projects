# basic Dungeon quest

print("Youve entered a dungeon. It's dark.......\n")

print("light torch = L")
print("keep walking = K")

choice = input("what will you do? : ").upper()

if choice == "L":
    print("\n-----------------------------------------------------------")
    print("youve on the torch and saw big hole infornt of you and goes by side\n")
    
    print("you walked some distance and suddenly")
    print("A goblin came infront of you\n")

    print("atack in goblin hand = H")
    print("attck in goblin head = A")

    choice = input("what will you do now?: ").upper()

    if choice == "A":
        print("\n-----------------------------------------------------------")
        print("Headshot goblin dies in one shot\n")

        print("other goblins noticed that their one members mana got diappared....means he died")
        print("they all came to kill you\n")
        
        print("run from there = R")
        print("summon your familier = S\n")

        choice = input("what will you do?: ").upper()

        if choice == "S":
            print("\n-----------------------------------------------------------")
            print("your familier is a dragon")
            print("dragon killed all zombies in a blink of a eye\n")

            print("dungeon boss appeared")
            print("your dragon fight him fight was intense and at end your dragon kiled it")
            print("but your dragon also got heavy damaged and died - RIP\n")

            print("THE END")
        elif choice == "R":
            print("\n-----------------------------------------------------------")
            print("you runed from that dungeon and eating bread at home")
            print("shame on you")
        else:
            print("\n-----------------------------------------------------------")
            print("your leg splipped and you died by bumping head in stone")
    elif choice == "H":
        print("\n-----------------------------------------------------------")
        print("goblin doged that attack and throwed his weapon at your head")
        print("weapon heat you hard in head\n")

        print("you died!")

    else:
        print("\n-----------------------------------------------------------")
        print("you did something stupid and died\n")

elif choice == "K":
    print("\n-----------------------------------------------------------")
    print("you didn't saw hole infront of you and died by falling in it")

else:
    print("\n-----------------------------------------------------------")
    print("you didnt goes into dungeona and goes back to home\n")
    print("shame on you coward")
