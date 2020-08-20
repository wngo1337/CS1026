# Assignment 1 program ("Coffee or tea, I see")
# Written by William Ngo

# define price constants for size (coffee and tea cost the same)
SMALL = 1.50
MEDIUM = 2.50
LARGE = 3.25
# define price constants for coffee flavoring
VANILLA = 0.25
CHOCOLATE = 0.75
MAPLE = 0.50
# define price constants for tea flavoring
LEMON = 0.25
MINT = 0.50
NOFLAVOR = 0
# works for both coffee and tea
# placeholder strings for printing the final line
stringSize = ""
stringFlavor = ""
flavor = ""

# prompt customer for their name
name = input("Hello, please enter your name: ")

if name.isalpha():
    name = name
elif name.isalnum():
    print("Your name cannot contain numbers.")
    exit()
else:
    print("Your name cannot contain any spaces or special characters.")
    exit()

# prompt for type of drink
drinkType = input("Please enter your choice of beverage (coffee or tea): ")
# convert all input to lowercase for easier validation
drinkType = drinkType.lower()

if drinkType == "c" or drinkType == "coffee":
    drinkType = "coffee"
elif drinkType == "t" or drinkType == "tea":
    drinkType = "tea"
else:
    print("We do not sell that drink here.")
    exit()

# prompt user for size of drink
size = input("Please enter the size of drink you would like (small/medium/large): ")
size = size.lower()

if size == "s" or size == "small":
    size = SMALL
    stringSize = "small"
elif size == "m" or size == "medium":
    size = MEDIUM
    stringSize = "medium"
elif size == "l" or size == "large":
    size = LARGE
    stringSize = "large"
else:
    print("That's not a valid size. Hello from the other... size?")
    exit()

# Check if user selected coffee and asks for flavoring
if drinkType == "coffee":
    flavorCheck = input("Please enter the type of flavoring you would like in your coffee (vanilla/chocolate/maple/none): ")
    flavorCheck = flavorCheck.lower()

    if flavorCheck == "vanilla" or flavorCheck == "v":
        flavor = VANILLA
        stringFlavor = "vanilla"
    elif flavorCheck == "chocolate" or flavorCheck == "c":
        flavor = CHOCOLATE
        stringFlavor = "chocolate"
    elif flavorCheck == "maple" or flavorCheck == "m":
        flavor = MAPLE
        stringFlavor = "maple"
    elif flavorCheck == "" or flavorCheck == "none":
        flavor = NOFLAVOR
        stringFlavor = "no"
    else:
        print("You did not enter a valid coffee flavor.")
        exit()

# Check if user selected tea and asks for flavoring
if drinkType == "tea":
    flavorCheck = input("Please enter the type of flavoring you would like in your tea (lemon/mint/none):")
    flavorCheck = flavorCheck.lower()

    if flavorCheck == "l" or flavorCheck == "lemon":
        flavor = LEMON
        stringFlavor = "lemon"
    elif flavorCheck == "m" or flavorCheck == "mint":
        flavor = MINT
        stringFlavor = "mint"
    elif flavorCheck == "" or flavorCheck == "none":
        flavor = NOFLAVOR
        stringFlavor = "no"
    else:
        print("You did not enter a valid tea flavor.")
        exit()

# calculate the cost of the drink before taxes
initialCost = size + flavor
# calculate total cost of the drink after taxes
totalCost = initialCost * 1.11

# print the customer's name and drink with the cost
print("For {}, a {} {} with {} flavoring, ".format(name, stringSize, drinkType, stringFlavor), end="")
print("cost: $%.2f" % totalCost)



