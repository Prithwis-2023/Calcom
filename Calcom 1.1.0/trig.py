import math
def trig_op():
  print("=============================================\nTrigonometric Operations\n=============================================\nInverse Trigonometric Operations\n=============================================\nHyperbolic Trigonometric Operations\n=============================================")
  f_list = ["Trigonometric Operations", "Inverse Trigonometric Operations", "Hyperbolic Trigonometric Operations"]
  op = input("Choose the type of operation: ")
  while (op not in f_list):
    print("Wrong Input! Please try again.")
    op = input("Choose the type of operation: ")
  if op == "Trigonometric Operations":
    print("You have the options to evaluate the following functions for x in radians.")
    print("==========================================================================")
    print("sin(x)\n=============================================\ncos(x)\n=============================================\ntan(x)\n=============================================\nsec(x)\n=============================================\ncosec(x)\n=============================================\ncot(x)\n=============================================")
    f_list = ["sin(x)", "cos(x)", "tan(x)", "sec(x)", "cosec(x)", "cot(x)"]
    d=input("Enter the function: ")
    while (d not in f_list):
      print("Wrong Input! Please try again.")
      d=input("Enter the function: ")
    if d == "sin(x)":
      x=float(input("Enter the value of x: "))
      print(math.sin(x))
    elif d == "cos(x)":
      x=float(input("Enter the value of x: "))
      print(math.cos(x))
    elif d == "tan(x)":
      x=float(input("Enter the value of x: "))
      print(math.tan(x))
    elif d == "sec(x)":
      x=float(input("Enter the value of x: "))
      a = (math.cos(x))
      print(1/a)
    elif d == "cosec(x)":
      x=float(input("Enter the value of x: "))
      a = (math.sin(x))
      print(1/a)
    elif d == "cot(x)":
      x=float(input("Enter the value of x: "))
      a = (math.tan(x))
      print(1/a)
    else:
      print("Invalid Input!")
  elif op == "Inverse Trigonometric Operations":
    print("You have the option to evaluate the following functions.")
    print("==========================================================================")
    print("arcsin(x)\n=============================================\narccos(x)\n=============================================\narctan(x)\n=============================================")
    f_list = ["arcsin(x)", "arccos(x)", "arctan(x)"]
    d = input("Enter the function: ")
    while (d not in f_list):
      print("Wrong Input! Please try again.")
      d = input("Enter the function: ")
    if d == "arcsin(x)":
      e=float(input("Enter the value of x: "))
      while(e > 1 or e < -1):
        print("Domain Error. Please try again!")
        e=float(input("Enter the value of x: "))
      print(str(math.asin(e)))
    elif d == "arccos(x)":
      e=float(input("Enter the value of x: "))
      while(e > 1 or e < -1):
        print("Domain Error. Please try again!")
        e=float(input("Enter the value of x: "))
      print(str(math.acos(e)))
    elif d == "arctan(x)":
      e=float(input("Enter the value of x: "))
      while(e > 1 or e < -1):
        print("Domain Error. Please try again!")
        e=float(input("Enter the value of x: "))
      print(str(math.atan(e))) 
  elif op == "Hyperbolic Trigonometric Operations":
    print("=============================================\nsinh(x)\n=============================================\ncosh(x)\n=============================================\ntanh(x)\n=============================================")
    f_list = ["sinh(x)", "cosh(x)", "tanh(x)"]
    opt = input("Enter the option: ")
    while (opt not in f_list):             
      print("Wrong Input! Please try again.")
      opt = input("Enter the option: ")
    if opt == "sinh(x)":
      x = float(input("Enter the value of x: "))
      print(math.sinh(x))
    elif opt == "cosh(x)":
      x = float(input("Enter the value of x: "))
      print(math.cosh(x))
    elif opt == "tanh(x)":
      x = float(input("Enter the value of x: "))
      print(math.tanh(x))             
while True:
  trig_op()
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
