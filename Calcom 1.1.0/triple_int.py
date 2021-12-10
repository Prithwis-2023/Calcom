import sympy as sp
from sympy import *
init_printing(use_unicode=False, wrap_line=False)
x,y,z=symbols('x y z')
print("Currently, you can only perform indefinite integration. Use only x, y and z as the variables of integration.")
print("====================================================")
exp=input("Enter the expression: ")
exp_list = [char for char in exp]
for i in range(len(exp_list)):
  if exp_list[i] == "^":
    exp_list[i] == "**"    
print("======================Result========================")
print(integrate(exp, x, y, z))
