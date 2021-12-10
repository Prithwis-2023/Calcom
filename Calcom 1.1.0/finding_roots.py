def finding_roots():
  import numpy as np
  list = []
  n = int(input("Enter the degree of the polynomial: "))
  while (n<1):
    print("Must be greate than or equal to 1! Please try again.")
    n = int(input("Enter the degree of the polynomial: "))
  print(f"Enter the coefficients from left to right. For example, if your polynomial is x^2+2x+1, then first enter 1, then 2 and finally 1.")
  for i in range(n+1):
    print("=======================================================================")
    c = float(input("Enter coefficient {}: ".format(i+1)))
    list.append(c)
  i+=1  
  sol = np.roots(list)
  print("==============================SOLUTION===================================")
  print(sol)  

while True:
  finding_roots()
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
      
