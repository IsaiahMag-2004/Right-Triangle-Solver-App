#Taking two legs of the right triangle returns the Hypotonuse, and area
#author (Isaiah Magana)
#
#Main.py

print("Welcome to the Right Triangle Solver App")

#Get Legs
first_leg = float(input("What is the first leg on the triangle: "))
second_leg = float(input("What is the second leg on the triangle: "))

#Calculate and round
hypotonuse = round(first_leg**2 + second_leg**2 , 2)
area = round((first_leg * second_leg) / 2 , 2)

#output
print(f"For a trinagle with legs of {str(first_leg)} and {str(second_leg)} the hypotenuse is {str(hypotonuse)}")
print(f"For a triangle with legs of {str(first_leg)} and {str(second_leg)} the area is {str(area)}")


