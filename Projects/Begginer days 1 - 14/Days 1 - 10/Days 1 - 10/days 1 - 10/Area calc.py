import math

height = float(input("Enter the height in m: "))
width = float(input("Enther the width in m: "))
coverage_per_can = float(input("How many meters does one can fill? "))

def area(height, width, coverage_per_can):
    area_to_cover = height * width
    number_of_cans = math.ceil(area_to_cover / coverage_per_can)
    # math.ceil rounds up

    print(f"The area to cover is {area_to_cover}m")
    print(f"You need {number_of_cans} cans to paint the entier area.")

area(height, width, coverage_per_can)