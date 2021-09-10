import math

height = int(input("enter the height of the wall"))
width = int(input("enter the width of the wall"))
coverage_per_can = int(input("enter the coverage"))


def paint_area_calculator(height, width, coverage_per_can):
    cans = math.ceil((height*width)/coverage_per_can)
    return cans


cans_needed = paint_area_calculator(height,width,coverage_per_can)
print(f"You'll need {cans_needed} cans.")