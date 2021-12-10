import math
def nt_i():
  print("Calcom has the following features for Number Theory:")
  print("*********************************************\nPrime Identification\n=============================================\nDivisibility Test\n=============================================\nDiophantine Equations\n=============================================\nPartitions\n=============================================\nG.C.D\n=============================================\nL.C.M\n=============================================")
  f_list = ["Prime Identification", "Divisibility Test", "Diophantine Equations", "Partitions", "G.C.D", "L.C.M"]
  g = input("Enter the option: ")
  while (g not in f_list):
    print("Wrong Input! Please try again.")
    g = input("Enter the option: ")
  if g == "Prime Identification":
    # Program to check if a number is prime or not

    num = int(input("Enter the number: "))

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
    flag = False

# prime numbers are greater than 1
    if num > 1:
    # check for factors
      for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
    if flag:
      print(num, "is not a prime number") 
    else:
      print(num, "is a prime number")

  elif g == "Diophantine Equations":
    from sympy.solvers.diophantine import diophantine
    from sympy import symbols
    x, y, z = symbols("x, y, z", integer=True)
    a = int(input("Enter the coefficient of x: "))
    b = int(input("Enter the coefficient of y: "))
    c = int(input("Enter the constant: "))
    print(diophantine(a*x+b*y-c))
  elif g == "Divisibility Test":
    k = int(input("Enter the Dividend: "))
    m = int(input("Enter the divisor: "))
    if k%m == 0:
      print("{} is divisible by {}".format(k,m))
    elif k%m != 0:
      print("{} is not divisible by {}".format(k,m))
      print("Suggestions:\n============================================")
      for i in range(1, k-1):
        if k%i == 0:
          #print("SUGGESTIONS:")
          print("{} is divisible by {}".format(k,i))
          print("============================================")
        i+=1
  elif g == "Partitions":
    s=int(input("Enter the number: "))
    X=1/((4*s*3**(1/2))*(2.718)**(3.414*((2*s)/3)**(1/2)))
    print("~" , str(X))

  elif g == "G.C.D":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(math.gcd(a,b))

  elif g == "L.C.M":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))  
    gcd = math.gcd(a,b)
    lcm = (a*b)/gcd
    print(lcm)
while True:
  nt_i()
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
