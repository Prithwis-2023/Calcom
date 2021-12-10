# still have to copy paste
import numpy as np
from sympy import symbols, Eq, solve
x, y = symbols('x y')
print("*********************************************\nEquations with 2 unknowns\n=============================================\nEquations with 3 unknowns\n=============================================")
f_list = [2, 3]
opt = input("Enter the number of unknowns: ")
while (opt not in f_list):
  print("Wrong Input! Please try again.")
  opt = input("Enter the number of unknowns: ")
if opt == 2:
  print("Instructions:")
  print("1) Enter the equations in the form ax + by = c. Write each coefficient of the variables even if it's 1.\n2) Use letters x and y for equations with 2 unknowns and x, y, z for that of 3.\n===========================================================================")
  exp1 = int(input("Enter the first equation: "))
  list1 = []
  exp1.split()
  for ele in exp1:
    list1.append(ele)
  list1_new = []
  for i in range(len(list1)):
    if list1[i] not in [' ', '=', '+', '-', 'x', 'y', 'z']:
      list1_new.append(list1[i])
  list1_new[2:4] = [''.join(list1_new[2:4])]  
  elements1 = [int(char) for char in list1_new]
  #eq1 = Eq((elements1[0])*x - (elements[1])*y - elements[2])

  exp2 = input("Enter the second equation: ")
  list2 = []
  exp2.split()
  for ele in exp2:
    list2.append(ele)
  list2_new = []
  for i in range(len(list2)):
    if list2[i] not in [' ', '=', '+', '-', 'x', 'y', 'z']:
      list2_new.append(list2[i])
  list2_new[2:4] = [''.join(list2_new[2:4])]    
  elements2 = [int(char) for char in list2_new]
  #eq2 = Eq((elements[0])*x - (elements[1])*y - elements[2])
  
  m_list = [[elements1[0], elements1[1]], [elements2[0], elements2[1]]]
  A = np.array(m_list)
  B = np.array([elements1[2], elements2[2]])
  X = np.linalg.inv(A).dot(B)
  print("=========================Result==========================")
  print("x = {}".format(X[0]))
  print("y = {}".format(X[1]))
if opt == 3:
  print("1) Enter the equations in the form ax + by + cz = d. Write each coefficient of the variables even if it's 1.\n2) Use letters x and y for equations with 2 unknowns and x, y, z for that of 3.\n======================================================================================")
  exp1 = input("Enter the first equation: ")
  exp2 = input("Enter the second equation: ")
  exp3 = input("Enter the third equation: ")
  list1 = []
  list2 = []
  list3 = []
  exp1.split()
  for ele in exp1:
    list1.append(ele)
  list1_new = []
  for i in range(len(list1)):
    if list1[i] not in [' ', '=', '+', '-', 'x', 'y', 'z']:
      list1_new.append(list1[i])
  list1_new[2:4] = [''.join(list1_new[2:4])]  
  elements1 = [int(char) for char in list1_new]
  
  exp2 = input("Enter the second equation: ")
  exp2.split()
  for ele in exp2:
    list2.append(ele)
  list2_new = []
  for i in range(len(list2)):
    if list2[i] not in [' ', '=', '+', '-', 'x', 'y', 'z']:
      list2_new.append(list2[i])
  list2_new[2:4] = [''.join(list2_new[2:4])]    
  elements2 = [int(char) for char in list2_new]
  
  exp3 = input("Enter the third equation: ")
  exp3.split()
  for ele in exp2:
    list3.append(ele)
  list3_new = []
  for i in range(len(list3)):
    if list3[i] not in [' ', '=', '+', '-', 'x', 'y', 'z']:
      list3_new.append(list3[i])
  list3_new[2:4] = [''.join(list3_new[2:4])]    
  elements3 = [int(char) for char in list3_new]  

  m_list = [[elements1[0], elements1[1], elements1[]], [elements2[0], elements2[1]]]
  A = np.array(m_list)
  B = np.array([elements1[2], elements2[2]])
  X = np.linalg.inv(A).dot(B)
  print("=========================Result==========================")
  print("x = {}".format(X[0]))
  print("y = {}".format(X[1]))
