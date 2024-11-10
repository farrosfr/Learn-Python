"""
This program is a Pig Latin Translator.
It takes a word input from the user, converts it to Pig Latin,
and prints the translated word.
"""
print "Starting the calculator..."

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == 'C':
    radius = float(raw_input("Enter radius: "))
    area = 3.14159 * radius**2
    print "Area: %f" % area
elif option == 'T':
    base = float(raw_input("Enter base: "))
    height = float(raw_input("Enter height: "))
    area = 0.5 * base * height
    print "Area: %f" % area
else:
    print "Error! Invalid shape."

print "Exiting..."


