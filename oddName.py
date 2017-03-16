"""Ally Smith"""

# User to Input Name
name = input("Enter Your Name: ")

# Check the Input isn't Blank
valid_entry = False
while not valid_entry:
    try:
        if len(name) != 0:
            valid_entry = True
    except:
        print("Invalid Input. Please try again.")

# Print every second letter in the name
if valid_entry is True:
    for char in name[::2]:
        print(char)
