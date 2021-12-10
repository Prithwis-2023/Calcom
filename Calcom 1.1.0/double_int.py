import sympy as sp
from sympy import *
init_printing(use_unicode=False, wrap_line=False)
x,y=symbols('x y')
y,z=symbols('y z')
x,z=symbols('x z')
print("Currently, you can only perform indefinite integration. Use only x and y as the variables of integration.")
print("**************************************************************")
exp=input("Enter the expression: ")
exp_list = [char for char in exp]
for i in range(len(exp_list)):
  if exp_list[i] == "^":
    exp_list[i] == "**"    
print("======================Result========================")
print(integrate(exp, x, y))
