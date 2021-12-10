import sympy as sp
import numpy as np
from numpy import linalg
from itertools import islice
def eqns():
    unknowns = int(input("Enter the number of unknowns: "))
    print("Enter the equation in the following form. If the equation is x + 2y = 3, enter the first coefficient as 1, 2nd coefficient as 2 and the constant as 3.")
    numbers = []
    const = []
    length_to_split = []
    for i in range(unknowns):
      length_to_split.append(unknowns)
    n=1
    while (n<=unknowns):
      for i in range(unknowns):
        coeff = float(input("Enter coefficient {} of equation {}: ".format(i+1, n)))
        print('=============================================')
        numbers.append(coeff)
      constant = float(input("Enter the constant of equation {}: ".format(n)))
      print('=============================================')
      const.append(constant) 
      n = n + 1 

    inputt = iter(numbers)
    output = [list(islice(inputt, elem))
              for elem in length_to_split]  
    output = np.array(output)
    const = np.array(const)

    x = np.linalg.solve(output,const)
    print('====================Result=====================')
    print(x)

while True:
    eqns()
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
            eqns()

