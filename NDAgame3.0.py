place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Do you want to climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass  # Invalid action, do nothing for now
elif place == "cave":
    action = input("Do you want to light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You illuminate the cave and find a stash of gold!")
    elif action == "proceed in the dark":
        print("You stumble in the darkness and fall into a pit!")
    else:
        pass  # Invalid action, do nothing for now
else:
    print("Invalid place! Please choose 'forest' or 'cave'.")
