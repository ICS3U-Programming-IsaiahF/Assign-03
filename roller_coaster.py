#!/usr/bin/env python3

# Created by: Isaiah Fernandez
# Date: January 11, 2023
# This program tells the user if they are tall enough for the ride with user input.

import math

def main():

    height_string_up = (input("What is your height in meters or centimeters? "))
    height_string = height_string_up.lower()
    # Try catch for invalid input
    if "c" in height_string:
        height_string = (height_string.replace("m","").replace("c",""))       
        
        try: 
            height = float(height_string)
            print("")

        except ValueError:
            print("")
            print("Please input valid a number")
            print("")
            return main()
        
        height = height/100
    else:
        try: 
            height = float(height_string.replace("m",""))
            print("")

        except ValueError:
            print("")
            print("Please input valid a number")
            print("")
            return main()
    if height < 0:
        print("Please input a positive number")
        print("")
        return main()

    else:
    
        if height >= 1.32:    
            print("You are tall enough to go on the roller coaster!")
            print("")
        else:  
            print("Sorry, you are not tall enough to go on the roller coaster.")
            print("")

if __name__ == "__main__":
    main()
