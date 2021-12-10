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
#var_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
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



