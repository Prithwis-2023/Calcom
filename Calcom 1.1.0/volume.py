def volume():
      print("*********************************************\nCube\n=============================================\nCuboid\n=============================================\nSphere\n=============================================\nRight Circular Cone\n=============================================\nRight Circular Cylinder\n=============================================\nPrism\n=============================================\nRight Rectangular/Square Pyramidal\n=============================================\nEllipsoid\n=============================================\nTetrahedron\n=============================================")
      f_list = ["Cube", "Cuboid", "Sphere", "Right Circular Cone", "Right Circular Cylinder", "Prism", "Right Rectangular/Square Pyramidal", "Ellipsoid", "Tetrahedron"]
      o = input("Enter the shape: ") 
      while (o not in f_list):
        print("Wrong Input! Please try again.")
        o = input("Enter the shape: ") 
        
      if o == "Cube":
            l = float(input("Enter the length of one side: "))
            print("The volume is: " + str(l**3))

      elif o == "Cuboid":
            l = float(input("Enter the length: "))
            b = float(input("Enter the breadth: "))
            h = float(input("Enter the height: "))
            V = l*b*h
            print("The volume is: " + str(V))

      elif o == "Sphere":
            r = float(input("Enter the radius: "))
            V = (4/3)*3.141592653589793238*(r)**3
            print("The volume is: " + str(V))

      elif o == "Right Circular Cone":
            r = float(input("Enter the radius: "))
            h_l = input("Do you want to enter Slant Height or the Altitude [Type S-H for Slant Height & H for Altitude]: ")
            if h_l == "SH":
                s_h = float(input("Enter the Slant Height: "))
                h = (((s_h)**2)-(r**2))**(1/2)
                V = (1/3)*3.141592653589793238*(r**2)*h
                print("The Volume is: " + str(V))
            elif h_l == "H":
                h_o = float(input("Enter the Height: "))
                V = (1/3)*3.141592653589793238*(r**2)*h_o
                print("The Volume is: " + str(V))

      elif o == "Right Circluar Cylinder":
            r = float(input("Enter the radius of the base: "))
            h = float(input("Enter the height: "))
            V = 3.141592653589793238*(r**2)*h
            print("The volume is: " + str(V))

      elif o == "Prism":
            print("As you know it... For a square prism, both the length and breadth are the same!")
            print("*******************************************************************************")
            l = float(input("Enter the length of the base: "))
            b = float(input("Enter the breadth of the base: "))
            h = float(input("Enter the height of the prism: "))
            V = (l*b)*h
            print("The Volume is: " + str(V))

      elif o == "Right-Rectangular/Square-Pyramidal":
            print("For Square Pyramid, both the length and breadth are the same.")
            print("*************************************************************")
            l = float(input("Enter the base length: "))
            b = float(input("Enter the base width: "))
            h = float(input("Enter the height: "))
            V = (l*b)*h
            print("The volume is: " + str(V))

      elif o == "Ellipsoid":
            a = float(input("Enter the first semi axis: "))
            b = float(input("Enter the second semi axis: "))
            c = float(input("Enter the third semi axis: "))
            V = (4/3)*3.141592653589793238*a*b*c
            print("The volume is: " + str(V))

      elif o == "Tetrahedron":
            l = float(input("Enter the length of the edge: "))
            V = (l**3)/(6*(2)**(1/2))
            print("The volume is: " + str(V))
while True:
  volume()
  contin = ""
  if contin not in ["no", "n", "yes", "y"]:
    contin = input(f"Do you wish to enter another calculation? (Yes/No): ")
    wish = ["Yes", "No"]
    while (contin not in wish):
          print("Wrong Input! Please try again.")
          contin = input(f"Do you wish to enter another calculation? (Yes/No): ")
    if contin.lower() in ["no", "n"]:
      break
    elif contin.lower() in ["yes", "y"]:
      continue
