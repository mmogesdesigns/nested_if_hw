# You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

# Buggy Code:

# place = input("Choose a place: forest or cave? ")

# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")
# Task 2: Setting the Scene

# Based on the corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

# Task 3: Default Path

# If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    print("You find a hidden treasure!")
    light_or_dark_input = input("Would you like to 'light a torch' or 'proceed in the dark'? ")
    if light_or_dark_input == 'light a torch':
         print("You light a torch and illuminate the cave. You find a hidden passage!")
    elif light_or_dark_input == 'proceed in the dark':
        print("You proceed in the dark and stumble upon a hidden trap. You fall into a pit!")
    else:
        pass
else:
    pass


#***********************************************

# Task 1: Code Correction

# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

# Buggy Code:

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)
# Task 2: Venue Selection

# Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like "audio system" or "projector" based on the number of attendees.

# Task 3: Catering Choices

# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
entertainment_system = "audio system" if attendees > 50 else 'projector'
print(venue)
print(entertainment_system)

food_input = input("Do you like vegetarian food? (yes/no) ")
food_type = "We Recommend Veggie Delight Caterers" if food_input == 'vegetarian' else "We recommend Gourmet Meals Caterers" 
print(food_type)