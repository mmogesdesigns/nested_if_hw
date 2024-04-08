# INITIALIZING DICTIONARIES
#creating an empty dictionary
kitchen ={}
print(kitchen)

#populate dictionary with key-value pairs
# dictionary in python is an ordered collection of key-value pairs
kitchen={
    # key: value
    # keys must be unique
    "spoon":"top drawer",
    "plates":"middle shelf",
    "cups":"top shelf"
}
print(kitchen)

# when accessing info from a dictionary, we access the value through the key
#similar to how we can grab an element in a list by its position
# dict['key] <-- return the value associated with that key
spoon_location = kitchen['spoon']
print(spoon_location)
cup_location = kitchen["cups"]
print(cup_location)

#you can have integers as keys
#just be careful not to confuse the syntax with a list
mall ={
    1: "general store",
    2: "tm's",
    3:"stat items"
}
first_floor = mall[1]
print(first_floor)
print(mall[3])

#trying to access a key in our dictionary that doesn't exsist
kitchen={
    # key: value
    # keys must be unique
    "spoon":"top drawer",
    "plates":"middle shelf",
    "cups":"top shelf"
}
# toaster_location = kitchen['toaster'] end up in KeyError

# safer way to access info from a dictionary
# dict.get("key were looking for","not found"or whatever error message you want to display)

kitchen={
    # key: value
    # keys must be unique
    "spoon":"top drawer",
    "plates":"middle shelf",
    "cups":"top shelf"
}
print(kitchen.get("plates"))
print(kitchen.get("glass","not found"))

# adding and updating our dictionary
community_center ={
    "yoga": "8 am",
    "art": "10 sm"
}
# dict['key to be added']= 'value to be added at that key'
community_center["smash tournment"]="7pm"
print(community_center)

community_center['valorant comp']="all day"
community_center['pottery class']='5 am'
community_center['dance']='5:30 am'
community_center['bingo']='9 am'
community_center['axe throwing']='10 pm, specifically after drinks'
community_center['coding camp']='6 pm'
print(community_center)

#to update/change dictionaries
# dict['key to be updated']="new value"
community_center['valorant comp']="TBD"
print(community_center)

# updating dictionary with update()
# dict.update ({'key to be added or updated':,"value for that key"})
community_center.update({"pickleball": "12 pm"})
print(community_center)

#updating with update()
community_center.update({"pottery class":"6 am"})
print(community_center)

#removing with dict.pop("key to be removed")
basket={
    "apples":30,
    "oranges":20,
    "bananas":14
}

removed_item = basket.pop('oranges')
print(removed_item)
print(basket)

#takes in optional 2nd argument that will be retrned if key not found
removed_item = basket.pop('strawberries','not found')
print(removed_item)
print(basket)

# dict.popitem() no parameters, it pops the last item in dictionary
user_data={
    'name': 'ash ketchum',
    'age': '10',
    'city':'pallet town'
}
print(user_data.popitem())
print(user_data)

# del removes variables from memory
name ='dark magician'
print(name)
del name #completely wipes name variable from memory
# print(name) which is why this will be an error

book_shelf={
    'fiction':10,
    'non-fiction':15,
    "manga":15
}
del book_shelf['manga']
print(book_shelf)

# dict.clear() deletes everything in the dictionary
session_data={
    'user_data':12345,
    'status':'active',
    'username':'urmomlol'
}
session_data.clear()
print(session_data)

# accessing information in our dictionary by loops
# .keys() .values() .items()
community_center = {
    "Yoga": "8 AM",
    "Art": "10 AM",
    "Smash Tournament": "7 PM",
    "Valorant Comp": "All Day, get here early nerds",
    "Pottery Class": "5 AM",
    "Dance Class": "5:30 PM",
    "Bingo": "9 AM",
    "Axe Throwing": "10 PM, specifically after drinks",
    "Coding Camp": "6 PM"
}
# .keys()(gives a tangible list of keys) looping thru the dict with no extra methods
for key in community_center:
    print(key)
print(community_center.keys())
for yaknow in community_center.keys():
    print(yaknow)

# looping with keys to access values in dictionary
for key in community_center.keys():
    print(community_center[key])

# dict.values() - looping through values
community_center = {
    "Yoga": "8 AM",
    "Art": "10 AM",
    "Smash Tournament": "7 PM",
    "Valorant Comp": "All Day, get here early nerds",
    "Pottery Class": "5 AM",
    "Dance Class": "5:30 PM",
    "Bingo": "9 AM",
    "Axe Throwing": "10 PM, specifically after drinks",
    "Coding Camp": "6 PM"
}
print(community_center.values())
for value in community_center.values():
    print(value)

# sorting my dictionaey's keys
# sorted() <-- creates a copy of the list and sorts it
for activity in sorted(community_center.keys()):
    print(f'{activity} starts at  {community_center[activity]}')

#***********MOST IMPORTANT********************
# dict.items()--> list of tuples. where the key is the first position and the second position
community_center = {
    "Yoga": "8 AM",
    "Art": "10 AM",
    "Smash Tournament": "7 PM",
    "Valorant Comp": "All Day, get here early nerds",
    "Pottery Class": "5 AM",
    "Dance Class": "5:30 PM",
    "Bingo": "9 AM",
    "Axe Throwing": "10 PM, specifically after drinks",
    "Coding Camp": "6 PM"
}
print(community_center.items())
for key, value in community_center.items():
    print(f'{key} starts at {value}')

for activity, time in community_center.items():
    if time == "6 PM":
        print(f'oh cool I can participate in {activity}')
    else:
        print('i can\'t do that')

kitchen={
    # key: value
    # keys must be unique
    "spoon":"top drawer",
    "plates":"middle shelf",
    "cups":"top shelf"
}
for utensil, location in kitchen.items():
    if location == "top drawer":
        print(f'yay I found the {utensil}')

#**********counter dictionary******************
names =['ryan','mary','haya','raymond','jessica','raymond','jessica','raymond','jessica','mary','raymond','jessica','mary']

name_count ={}
for name in names:
    if name not in name_count:
        name_count.update({name:1})
    else: 
        name_count [name]+= 1
print(name_count)

# dict.setdefault()
# return a value associated with a key in our dictionary
stock = {"apples":30, "oragnes": 20}
stock.setdefault("bananas", 15)
print(stock)

print(stock.setdefault("apples", 2376234))

my_stuff = []

def add_shirt():
    while True:        
      thing = input("What shirt would you like to add to your stuff? ")
      if thing == "quit":          
          break
      my_stuff.append(thing)

def add_game():
    while True:
      game = input("What game would you like to add to your stuff?")
      
      if game == "quit":
          break
      my_stuff.append(game)

def add_food():
    while True:
      food = input("What food would you like to add to your stuff?")
      if food == "quit":
          break
      my_stuff.append(food)
def show_stuff():
    print("Heres all your stuff: ")
    for stuff in my_stuff:
        print(stuff)

# add_shirt()
# add_game()
# add_food()
# show_stuff()

my_stuff ={
    'clothes': ["shirt", 'pants','socks'],
    'games':['super smash','half life 2','baldurs gate 3', 'valorant','call of duty'],
    'food':["peanut butter cups", "pizza", "vegetables"],
    'show stuff':[]
}
# shirt = my_stuff["clothes"[0]]
# print(shirt)

# games=my_stuff["games"]
# print(games)
# cool_game =games[2]
# print(cool_game)

# my_stuff["food"].append("tacos")
# print(my_stuff['food'])

# Convert the above code to keep track of your stuff in a dictionary
# your keys should be your categories (food, games, clothes, action figures, pokemon cards etc..)
# your values will be lists
# prompt the user to add items to each of their categories
# at the end print each category with the items inside each of those categories




#lists as values in dictionaries
library={
    'fantasy': ["Harry Potter", "The Hobbit","Lord of the Rings","Mean girls"],
    'Science Fiction':["Dune","Neuromancer"],
    "Mystery":["Sherlock Holmes", "And Then There Were None"]
}
# accessing our list
print(library['fantasy'])
# indexing into a list that is a value in a dictionary
print(library['fantasy'][1])
# looping through a list in a dictionary
for title in library['fantasy']:
    print(title)

# adding to a list of a dictionary
library['Mystery'].append("Syndrom e")

print(library["Mystery"])

scifi=library["Science Fiction"]
print(scifi)
scifi.append("Stargate SG1")
print(scifi)

# looping through lists in dictionaries
# start by looping through the dictionary items
# keys(), values(), are--> items()
for genre, titles in library.items():
    print(f"These are the books in your {genre} collection:")
    # second for loop to iterate through the titles, which are our lists(values)
    for title in titles:
        #prints each item in our list
        print(title)
print(library.items())

# list of dictionaries
art_gallery = [
    {"title":"Starry Night", "Artist": "van gogh", "year": 1890},
    {"title":"The Scream", "Artist": "drake murphy", "year": 1950},
    {"title":"Sguernica", "Artist": "picassp", "year": 1930}
]

for art in art_gallery:
    print(art['title'])
art_gallery.append({'title':"persistencce of memory", 'artist': 'dali', "year":1931})
print(art_gallery)

valorant_agents ={
    'good agents': ['todd','jeff'],
    'bad agents':['everyone else',"specifically whoever haya plays"]
}
for quality, agents in valorant_agents.items():
    print(f"here are the {quality} agents")
    for agent in agents:
        print(agent)
for quality, agents in valorant_agents.items():
    print(quality, agents)
for key in valorant_agents.keys():
    print(key)
for value in valorant_agents.values():
    print(value)
    for agent in value:
        print(agent)

artist_singles ={
    'drake':"still here",
    'the beatles':'strawberry fields',
    'sufjan stevens': 'chicago',
    'bille': 'what was i made for',
    'stevie wonder':'isnt she lovely',
    'SZA':'snooze',
    'black sabbath': 'war pigs',
    'all american rejects':'gives you hell',
    'logic': '5 am'
}

print(artist_singles["bille"])

#grabbing a key that doesn't exsist
#print(artist_singles['wilco'])-->ERROR
#.get() does not give u error ---> NONE
print(artist_singles.get('wilco',"artist not found"))

numbers=[12,56,17,1,23]
print(numbers[2]) #<-- grabbing a list element by index
# print(artist_singles['5 am'])# <-- accessing a values by key in a dictionary the data structure determine if we are "indexing" or not. You can index into a list but not into a dicitionary

artist_singles ={
    'drake':["still here",'hold on were going home','one dance','over'],
    'the beatles':['strawberry fields','in my life','hey bulldog'],
    'sufjan stevens': 'chicago',
    'bille': 'what was i made for',
    'stevie wonder':'isnt she lovely',
    'SZA':'snooze',
    'black sabbath': 'war pigs',
    'all american rejects':['gives you hell','dirty little secret','move along'],
    'logic': '5 am'
}


# dictionaries in dictionaries
museum_exhibits={
    "ancient egypt":{
        "artifacts":["sphinx","pyramid"],
        "famous pharaoha":["king tutunkhamun","cleopatra"]
    },
    "renaissance art":{
        "noble artists": ["leonardo","michelangelo","rapheal","donatello"],
        "key works":["mona lisa","the last supper","defeating shredder"]
    }
}
# grabbing regular keys from nested dictionaries
print(museum_exhibits["ancient egypt"])

# going farther into the nested dictionaries
# print(museum_exhibits["ancient egypt"]["artifacts"])
# # setting variable break points
# exhibit = museum_exhibits["ancient egypt"]
# print(exhibit["artifacts"[1]])

# # access defeating shredder
# print(museum_exhibits["renaissance art"]["key works"][2])

# adding to a neested dictionary
museum_exhibits["ancient egypt"]["recent discovery"]=["new tomb","the scary slab from courage the cowardly dog"]
print(museum_exhibits)

# looping through our nested dictionaries
museum_exhibits={
    #exhibit
    "ancient egypt":{ #details
        #section       information
        "artifacts":["sphinx","pyramid"],
        #section       information
        "famous pharaoha":["king tutunkhamun","cleopatra"]
    },
    #exhibit
    "renaissance art":{ #details
        #section
        "noble artists": ["leonardo",
        "michelangelo","rapheal","donatello"],
        #section
        "key works":["mona lisa","the last supper","defeating shredder"]
    }
}

for exhibit, details in museum_exhibits.items():
    print(f"exhibits: {exhibit}")
    for section, information in details.items():
        print(f"{section}: {information}")

pokemon={
    "abilities":[
        {
            "ability":{
                "name":"swarm",
                "description":"power up bug type moves"
            }
        },
        {
        "ability":{
                "name":"guts",
                "description":"increases attack"
            }
        }
    ]
}
print(pokemon["abilities"][0]["ability"]["name"])

# copying a dictionary
#shallow copy - copy is independent from the orginal one
# deep copy
original_artists ={"picasso": 1881, "van gogh": 1853,"monet":1840}
# dict.copy()
copied_artists =original_artists.copy()
 
print(original_artists)
print(copied_artists)
copied_artists["van gogh"]=1900
print("original",original_artists)
print("copied",copied_artists)

# DEEP COPY
import copy
# copy.deepcopy()
original_paintings = {"The Starry Night": "Van Gogh", "The Scream": "Munch" }
reproduced_paintings = copy.deepcopy(original_paintings)

# Change a value in the deep copy
reproduced_paintings["The Starry Night"] = "Da Vinci"
print("Original: ", original_paintings)
print("Reproduced ", reproduced_paintings )

copied_paintings = original_paintings
copied_paintings['The Scream'] = "Donatello"
print("Original", original_paintings)
print("Copied", copied_paintings)







