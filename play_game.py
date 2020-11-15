import json
import os
import time
def main():
    # TODO: allow them to choose from multiple JSON files?
    print("Select a game to play!")
    for element in range(len(os.listdir())):
        if os.listdir()[element].endswith('.json'):
            print(element, ".", os.listdir()[element])
    options = int(input(">"))
    with open(os.listdir()[options]) as fp:
        game = json.load(fp)
    print_instructions()
    print("You are about to play '{}'! Good luck!".format(game['__metadata__']['title']))
    print("")
    play(game)


def play(rooms):
    stopwatch = time.time()
    timer = 0
    time_second = time.time()/time.time()
    for time.time()/time.time():
        timer = timer + time.time()
        
    
    # Where are we? Look in __metadata__ for the room we should start in first.
    current_place = rooms['__metadata__']['start']
    # The things the player has collected.
    stuff = ['Cell Phone; no signal or battery...']

    while True:
        # Figure out what room we're in -- current_place is a name.
        here = rooms[current_place]
        # Print the description.
        print(here["description"])

        
        # TODO: print any available items in the room...
        
        print("The following items are in the room:", here["items"])
        # e.g., There is a Mansion Key.

        # Is this a game-over?
        if here.get("ends_game", False):
            break

        
        # Allow the user to choose an exit:
        usable_exits = find_visable_exits(here)
        # Print out numbers for them to choose:
        for i, exit in enumerate(usable_exits):
            print("  {}. {}".format(i+1, exit['description']))

        # See what they typed:
        action = input("> ").lower().strip()

        # If they type any variant of quit; exit the game.
        if action in ["quit", "escape", "exit", "q"]:
            print("You quit.")
            break
        
        #reprints instructions for 4 points
        if action == "help":
            print_instructions()
            continue
        
        if action == "stuff":
            print(stuff)
            continue
        
        if action == "take":
            for element in here["items"]:
                stuff.append(element)
            #take out stuff from items list 
            here["items"] = []
            continue
        
        if action == "drop":
            for index in range(len((stuff))):
                print(index + 1, ".", stuff[index])
            options = int(input(">"))
            here["items"] = [stuff[options-1]]
            stuff.pop(options-1)
            continue
            
        if action == "time":
            print(time.time())
            continue
        
        if action in ["search", "find"]:
            for exit in here['exits']:
                if "hidden" in exit:
                    exit["hidden"] = False
                #print(exit["destination"])
            continue
        
        # TODO: if they type "stuff", print any items they have (check the stuff list!)
        # TODO: if they type "take", grab any items in the room.
        # TODO: if they type "search", or "find", look through any exits in the room that might be hidden, and make them not hidden anymore!
        
        # Try to turn their action into an exit, by number.
        try:
            num = int(action) - 1
            selected = usable_exits[num]
            if "Mansion Key" not in stuff:
                if current_place == "crypt":
                    break
                if selected['destination'] == "outside":
                    print("You try to open the door, but it's locked!")
                    continue
            current_place = selected['destination']
            print("...")
        except:
            print("I don't understand '{}'...".format(action))
        
    print("")
    print("")
    print("=== GAME OVER ===")

def find_visable_exits(room):
    """
    Given a room, and the player's stuff, find a list of exits that they can use right now.
    That means the exits must not be hidden, and if they require a key, the player has it.

    RETURNS
     - a list of exits that are visible (not hidden) and don't require a key!
    """
    usable = []
    for exit in room['exits']:
        if exit.get("hidden", False):
            continue
        usable.append(exit)
    return usable

def print_instructions():
    print("=== Instructions ===")
    print(" - Type a number to select an exit.")
    print(" - Type 'stuff' to see what you're carrying.")
    print(" - Type 'take' to pick up an item.")
    print(" - Type 'quit' to exit the game.")
    print(" - Type 'drop' to drop item.")
    print(" - Type 'search' to take a deeper look at a room.")
    print("=== Instructions ===")
    print("")

if __name__ == '__main__':
    main()
