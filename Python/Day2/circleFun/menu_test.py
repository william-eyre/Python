from circleFun import Circle, getRectangle

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():


    choice = 0
    while choice != QUIT_CHOICE:
        display_menu ()
        choice = int (input ("Enter your choice: " ))
        if choice == AREA_CIRCLE_CHOICE:
            radius = float ( input("Enter the circle's radius "))
            print ('The area is', Circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float (input ("Enter the circle's radius"))
            print("The circumference is", Circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float ( input ("Enter the rectangle's width"))
            length = float ( input("Enter the rectangles's length"))
            print ("The area is", getRectangle)
        elif choice == QUIT_CHOICE:
            print ('Exiting the program')
        else:
            print ('Error: invalid selection')


def display_menu():
    print( "Menu")
    print('1) Area of the circle')
    print('2) Circumference of the circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')


main()
