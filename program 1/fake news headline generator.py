# import the random module

import random

# create subject
subjects= [
    "sharukh khan",
    "virat kholi",
    "nirmala sita raman",
    "a group of thief",
    "narander modi",
    "crome",
    "mahatma gandhi",
    "baba tilu",
    "prince"

]

actions =[
    "jumps ",
    "eats",
    "is dancing ",
    "orders",
    "celebrates",
    "is going",
    " is meeting"
]


place_or_things= [
    "in  red fort",
    "in mumbai",
    "in market",
    "inside kotha",
    "in india gate",
    "at school",
    "mango",
    "on king's house"
]

# state the headling generation loop

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)
    
    headling = f"BREAKING NEWS:- {subject} {action} {place_or_thing}"
    print("\n"+ headling)
    
    user = input("\n do you want another headling? (yes/no)").strip().lower()
    
    if user == "no":
        break
    
# print goood bye statement

print("\nthank you for using the fake news generator . have a nice day")