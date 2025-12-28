''' One foot is equal to 12 inches. Write a function that accepts a length written in feet 
    as an arguement and returns the equivalent length in inches.
    
    write a second function that asks the user for a number of feet and returns its value. 
    
    Write a third function that accepts a number of inches and displays this to the screen 
    
    use these three functions to write a program that converts feet to inches.'''


def feet_to_inches(feet):
        inches = feet * 12
        return inches
def get_feet_from_user():
        feet = float(input("Enter length in feet: "))
        return feet
def display_inches(inches):
        print(f"Length in inches: {inches}")
    
feet = get_feet_from_user()
inches = feet_to_inches(feet)
display_inches(inches)  