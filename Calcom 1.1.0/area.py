def area():
    print(
        "*********************************************\nSquare\n=============================================\nRectangle\n=============================================\nTriangle\n=============================================\nParallelogram\n=============================================\nRhombus\n=============================================\nSphere\n=============================================\nTrapezium\n=============================================\nCircle\n=============================================\nRight Circular Cylinder\n=============================================\nRight Circular Cone\n============================================="
    )
    a_t = input(f"Enter the shape name: ")
    f_list = [
        "Square", "Rectangle", "Triangle", "Parallelogram", "Rhombus",
        "Sphere", "Trapezium", "Circle", "Right Circular Cylinder",
        "Right Circular Cone"
    ]
    while (a_t not in f_list):
        print("Wrong Input! Please try again.")
        a_t = input("Enter the shape name: ")

    if a_t == "Square":
        D_E = float(input(f"Enter the side length: "))
        area = (D_E)**2
        print(area)

    elif a_t == "Rectangle":
        D_E = float(input(f"Enter the length: "))
        breadth = float(input(f"Enter the breadth: "))
        area = D_E * breadth
        print(area)

    elif a_t == "Triangle":
        D_E = float(input(f"Enter the base: "))
        BASE = float(input(f"Enter the height: "))
        area = (1 / 2) * (BASE) * (D_E)
        print(area)

    elif a_t == "Parallelogram":
        D_E = float(input("Enter the length of one side: "))
        HEIGHT = float(input("Enter the height: "))
        area = D_E * HEIGHT
        print(area)

    elif a_t == "Rhombus":
        D_E = float(input("Enter the first diagonal: "))
        diagonal = float(input("Enter the second diagonal: "))
        area = 1 / 2 * (D_E * diagonal)
        print(area)

    elif a_t == "Trapezium":
        D_E = float(input("Enter the first base: "))
        base = float(input("Enter the second base: "))
        h_t = float(input("Enter the height: "))
        area = ((D_E + base) / 2) * h_t
        print(area)

    elif a_t == "Circle":
        D_E = float(input("Enter the radius: "))
        area = 3.414 * (D_E)**2
        print(area)

    elif a_t == "Right Circular Cylinder":
        A = float(input("Enter the radius of the base: "))
        ht = float(input("Enter the height: "))
        AREA_a = 2 * 3.414 * A * ht
        print("Curved Surface Area: " + str(AREA_a))
        AREA_b = 2 * 3.414 * A * ht
        print("Total Surface Area: " + str(AREA_b))

    elif a_t == "Sphere":
        R = float(input("Enter the radius: "))
        AREA = 4 * 3.414 * R**2
        print("Area of sphere is: " + str(AREA))

    elif a_t == "Right Circular Cone":
        R = float(input("Enter the radius of the base: "))
        h = float(input("Enter the height: "))
        CSA = 3.414 * R * (R**2 + h**2)**(1 / 2)
        TSA = 3.414 * R * (R + (R**2 + h**2)**(1 / 2))
        print("Curved Surface Area: " + str(CSA))
        print("Total Surface Area: " + str(TSA))


while True:
    area()
    contin = ""
    if contin not in ["no", "n", "yes", "y"]:
        contin = input(f"Do you wish to enter another calculation? (Yes/No): ")
        wish = ["Yes", "No"]
        while (contin not in wish):
            print("Wrong Input! Please try again.")
            contin = input(
                f"Do you wish to enter another calculation? (Yes/No): ")
        if contin.lower() in ["no", "n"]:
            break
        elif contin.lower() in ["yes", "y"]:
            area()
