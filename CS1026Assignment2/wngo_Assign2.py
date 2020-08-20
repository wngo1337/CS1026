# CS1026 "Volume Calculator" Assignment 2
# code written by William Ngo

# define volume functions for each shape
from math import pi
allCubeVols = []
allPyramidVols = []
allEllipsoidVols = []

def cubeVolume():
    side_length = input("Enter the side length of your cube: ")
    # since we are allowed to assume user enters positive integers, we only have to check if input is numeric
    while not side_length.isdigit():
        print("That is not a valid side length.")
        side_length = input("Enter the side length of your cube: ")
    else:
        side_length = int(side_length)
        cube_vol = side_length ** 3
        round_cube_vol = float(round(cube_vol, 1))
        print("The volume of a cube with a side length of {} is {} \n".format(side_length, round_cube_vol))
        allCubeVols.append(round_cube_vol)

def pyramidVolume():
    pyramid_base = input("Enter the base length of your pyramid: ")
    while not pyramid_base.isdigit():
        print("That is not a valid base length.")
        pyramid_base = input("Enter the base length of your pyramid: ")

    pyramid_base = int(pyramid_base)
    pyramid_height = input("Enter the height of your pyramid: ")

    while not pyramid_height.isdigit():
        print("That is not a valid height.")
        pyramid_height = input("Enter the height of your pyramid: ")

    pyramid_height = int(pyramid_height)
    pyramid_vol = (1/3) * pyramid_base ** 2 * pyramid_height
    round_pyramid_vol = float(round(pyramid_vol, 1))
    print("The volume of a pyramid with a base of {} and a height of {} is {} \n".format(pyramid_base, pyramid_height, round_pyramid_vol))
    allPyramidVols.append(round_pyramid_vol)

def ellipsoidVolume():
    radius1 = input("Enter the first radius of your ellipsoid: ")
    while not radius1.isdigit():
        print("That is not a valid radius.")
        radius1 = input("Enter the first radius of your ellipsoid: ")
    else:
        radius1 = int(radius1)

    radius2 = input("Enter the second radius of your ellipsoid: ")
    while not radius2.isdigit():
        print("That is not a valid radius.")
        radius2 = input("Enter the second radius of your ellipsoid: ")
    else:
        radius2 = int(radius2)

    radius3 = input("Enter the third radius of your ellipsoid: ")
    while not radius3.isdigit():
        print("That is not a valid radius.")
        radius3 = input("Enter the third radius of your ellipsoid: ")

    radius3 = int(radius3)
    ellipsoid_vol = (4/3) * pi * radius1 * radius2 * radius3
    round_ellipsoid_vol = float(round(ellipsoid_vol, 1))
    print("The volume of an ellipsoid with radii of lengths {}, {}, and {} is {} \n".format(radius1, radius2, radius3, round_ellipsoid_vol))
    allEllipsoidVols.append(round_ellipsoid_vol)

# function used to print the lists (if they contain elements) at the end of the program
def printList(shape_list):
    if not shape_list:
        print("No computations for this shape")
    else:
        for i in range(0, len(shape_list)):
            if i == (len(shape_list) - 1):
                print(shape_list[i])
            else:
                print(shape_list[i], end =", ")

# defining the main function
def main():
    # create a loop that runs until we hit quit
    while True:
        print("Which of the following would you like to calculate the volume of?")
        print("Cube")
        print("Pyramid")
        print("Ellipsoid")
        print("Or enter 'quit' to end the session")
        shape = input("Enter your choice here: ")

        # now check if the input (convert to lowercase for ease) is valid
        if shape.lower() == "cube":
            cubeVolume()
        elif shape.lower() == "pyramid":
            pyramidVolume()
        elif shape.lower() == "ellipsoid":
            ellipsoidVolume()
        elif shape.lower() == "quit":
            print("You have come to the end of the session.")
            if not allCubeVols and not allPyramidVols and not allEllipsoidVols:
                print("You did not perform any volume calculations.")
                exit()
            else:
                print("The volumes calculated for each shape are shown below.")
                break
        else:
            print("That is not a valid option")
            print()
    # print the stored volumes if there are values in the shape's list

    print("Cube: ", end="")
    printList(allCubeVols)

    print("Pyramid: ", end="")
    printList(allPyramidVols)

    print("Ellipsoid: ", end="")
    printList(allEllipsoidVols)

# call the main function
main()
