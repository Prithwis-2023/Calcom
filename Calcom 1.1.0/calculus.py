import sympy as sp
from sympy import *
import scipy.integrate as integrate
import scipy.special as special
from scipy.integrate import quad
#exp = input("Enter the expression: ")
from numpy import sqrt, sin, cos, pi, exp
print("Instructions:")
print(f"1) Use brackets appropiately for correct results.")
print(f"2) Use exp() for e. Like e^x must be inputted as exp(x).")
print(f"3) Always represent the variables as instructed.")
#print("5) Use oo for infinity.")
def calculus():
  print("*********************************************\nDifferentiation\n=============================================\nIntegration\n=============================================")
  opt = input("Enter the option: ")
  f_list = ["Differentiation", "Integration"]
  while (opt not in f_list):
    print("Wrong Input! Please try again.")
    opt = input("Enter the option: ")
  if opt == "Differentiation": 
    type  = input(f"Enter the type of function (Single-Variable/Multi-Variable): ")
    f_list = ["Single-Variable", "Multi-Variable"]
    while (type not in f_list):
      print("Wrong Input! Please try again.")
      type = input(f"Enter the type of function (Single-Variable/Multi-Variable): ")
    if type == "Single-Variable":
      print("Use x as the variable.")
      print("*********************************************")
      x = sp.Symbol('x')
      exp = input(f"Enter the function: ")
      sol = sp.diff(exp)
      print("=====================Result====================")
      print(sol)
    elif type == "Multi-Variable":
      print("Use only lowercase alphabets as variables.")
      print("*********************************************")
      v = int(input("Please enter the number of variables: "))
      a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = sp.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
      exp = input("Enter the function: ")
      var = input("Enter the variable in whose respect you want to differentiate: ")
      sol = sp.diff(exp, var)
      print("====================Result=======================")
      print(sol)
  elif opt == "Integration":
    print("*********************************************\nSingle Integration\n=============================================\nDouble Integration\n=============================================\nTriple Integration\n=============================================")
    f_list = ["Single Integration", "Double Integration", "Triple Integration"]
    opt = input("Enter the option: ")
    while (opt not in f_list):
      print("Wrong Input! Please try again.")
      opt = input("Enter the option: ")
    if opt == "Single Integration":
      import sympy as sp
      from sympy import *
      from sympy import oo
      from sympy import sin, cos, tan, sec, sqrt, pi, exp, log, integrate
      init_printing(use_unicode=False, wrap_line=False)
      a = Symbol('a')
      b = Symbol('b')
      c = Symbol('c')
      d = Symbol('d')
      e = Symbol('e')
      f = Symbol('f')
      g = Symbol('g')
      h = Symbol('h')
      i = Symbol('i')
      j = Symbol('j')
      k = Symbol('k')
      l = Symbol('l')
      m = Symbol('m')
      n = Symbol('n')
      o = Symbol('o')
      p = Symbol('p')
      q = Symbol('q')
      r = Symbol('r')
      s = Symbol('s')
      t = Symbol('t')
      u = Symbol('u')
      v = Symbol('v')
      w = Symbol('w')
      x = Symbol('x')
      y = Symbol('y')
      z = Symbol('z')

      print("Use x as the variable of integration.")
      print("============================================")
      exp = input("Enter the function: ")
      exp_list = [char for char in exp]
      for i in range(len(exp_list)):
        if exp_list[i] == "^":
          exp_list[i] == "**" 
      lb = input("Enter the lower bound: ")
      ub = input("Enter the upper bound: ")
      print("=================Result====================")
      print(integrate(exp, (x, lb, ub)))
    
    elif opt == "Double Integration":  
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
  
    elif opt == "Triple Integration":
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

    
while True:
  calculus()
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




