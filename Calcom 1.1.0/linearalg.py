import tkinter as tk
import numpy as np
from numpy import linalg
import numpy.linalg as la
verySmallNumber = 1e-14 # That's 1×10⁻¹⁴ = 0.00000000000001
def gsBasis(A) :
      B = np.array(A, dtype=np.float_) # Make B as a copy of A, since we're going to alter it's values.
      # Loop over all vectors, starting with zero, label them with i
      for i in range(B.shape[1]) :
          # Inside that loop, loop over all previous vectors, j, to subtract.
          for j in range(i) :
            # Complete the code to subtract the overlap with previous vectors.
            # you'll need the current vector B[:, i] and a previous vector B[:, j]
            B[:, i] = B[:, i] - B[:, i] @ B[:, j]*B[:, j] 
        # Next insert code to do the normalisation test for B[:, i]
          if la.norm(B[:, i]) > verySmallNumber:
              B[:, i] = B[:, i] / la.norm(B[:, i])
          else:
              B[:, i] = np.zeros_like(B[:, i])
                
    # Finally, we return the result:
      return B
def dimensions(A) :
      return np.sum(la.norm(gsBasis(A), axis=0))      
def linalg():
  print("*********************************************\nAddition\n=============================================\nSubtraction\n=============================================\nMultiplication\n=============================================\nSingularity Check\n=============================================\nBasis\n=============================================\nCalculate Dimension\n=============================================")
  f_list = ["Addition", "Subtraction", "Multiplication", "Singularity Check", "Basis", "Calculate Dimension"]
  opt = input("Enter the option: ")
  while (opt not in f_list):
    print("Wrong Input! Please try again.")
    opt = input("Enter the option: ")
  if opt == "Addition" or opt == "Substraction":
    cont = True
    rowxcol = input('How many rows and columns should be in this matrix? Input your answer in the form rowxcol e.g. 2x3: ')
    rc = rowxcol.split('x')
    try:
        rc[0] = int(rc[0])
        rc[1] = int(rc[1])
    except:
        print('Invalid Input.')
        cont = False
    else:
        if rc[0] <= 0 or rc[1] <= 0:
            print('Invalid Input.')
            cont = False
    if cont == True:
        win = tk.Tk()
        win.title("Matrix Addition/Subtraction")

        matrix1 = []
        matrix2 = []

        def calculate():
            for i in range(len(matrix1)):
                for j in range(len(matrix1[i])):
                    try:
                        matrix1[i][j] = int(matrix1[i][j])
                    except:
                        matrix1[i][j] = int(matrix1[i][j].get())
            for i in range(len(matrix2)):
                for j in range(len(matrix2[i])):
                    try:
                        matrix2[i][j] = int(matrix2[i][j])
                    except:
                        matrix2[i][j] = int(matrix2[i][j].get())
            mtrx1 = np.array(matrix1)
            mtrx2 = np.array(matrix2)
            if sign['text'] == "+":
                print("Addition:")
                print("===================")
                print(np.add(mtrx1, mtrx2))
            elif sign['text'] == "-":
                print("Subtraction:")
                print("===================")
                print(np.subtract(mtrx1, mtrx2))
                '''
            elif sign['text'] == "x":
                print("Multiplication:")    
                print("===================")
                print(np.dot(mtrx1,mtrx2))
                '''
        def change_sign():
            if sign['text'] == "+":
                sign['text'] = "-"
            else:
                sign['text'] = "+"

        for r in range(1, rc[0] + 1):
            row1 = []
            for c in range(1, rc[1] + 1):
                entry = tk.Entry(win, width=5)
                entry.grid(row=r, column=c, pady=3, padx=3)
                row1.append(entry)
            matrix1.append(row1)

        sign = tk.Button(win, text="+", command=change_sign)
        sign.grid(row=rc[0] + 1, column=rc[1] + 1, pady=3, padx=3)
    
        for r in range(rc[0] + 2, 2 * (rc[0]) + 2):
            row2 = []
            for c in range(rc[1] + 2, 2 * (rc[1]) + 2):
                entry = tk.Entry(win, width=5)
                entry.grid(row=r, column=c, pady=3, padx=3)
                row2.append(entry)
            matrix2.append(row2)
    
        submit = tk.Button(win, text="Calculate", command=calculate)
        submit.grid(row=2 * rc[0] + 3, column=2 * rc[1] + 3, pady=3, padx=3)

        win.mainloop()
  elif opt == "Multiplication":
    print("Here you can only multiply two matrices at a time.")
    list = []
    for i in range (2):
      R = int(input("Enter the number of rows of matrix {}: ".format(i+1)))
      C = int(input("Enter the number of columns of matrix {}: ".format(i+1)))
  
# Initialize matrix
      matrix = []
      result = []
      print("Enter the entries rowwise: ")
  
# For user input
      for i in range(R):          # A for loop for row entries
        a =[]
        for j in range(C):      # A for loop for column entries
            a.append(float(input()))
        matrix.append(a)
        result.append(0)
      print("================Matrix Data=================")  
      A = np.array(matrix)
      print(np.array(matrix))
      list.append(matrix)

    result = np.dot(list[0], list[1])
    print("==================Result=====================")
    print(np.array(result))

  elif opt == "Singularity Check":
    print("Here you can check whether your inputted matrix is singular or not.") 
    R = int(input("Enter the number of rows: "))
    C = int(input("Enter the number of columns: "))
    matrix = []
    print("Enter the entries rowwise: ")
    for i in range(R):
      a = []
      for j in range(C):
        a.append(float(input()))
      matrix.append(a)
    A = np.array(matrix)
    print("================Matrix Data=================")  
    print(A)
    print("============================================")
    det = np.linalg.det(A)
    if det == 0:
      print("The matrix is Singular.")
    else:    
      print("The matrix is non-Singular.")


  elif opt == "Basis":
    R = int(input("Enter the number of rows: "))
    C = int(input("Enter the number of columns: "))
  
# Initialize matrix
    matrix = []
    print("Enter the entries rowwise: ")
  
# For user input
    for i in range(R):          # A for loop for row entries
      a =[]
      for j in range(C):      # A for loop for column entries
         a.append(float(input()))
      matrix.append(a)
    A = np.array(matrix, dtype=np.float_)
    print("====================Result=====================")
    print(gsBasis(A))
  
  elif opt == "Calculate Dimension" :
    R = int(input("Enter the number of rows: "))
    C = int(input("Enter the number of columns: "))
  
# Initialize matrix
    matrix = []
    print("Enter the entries rowwise: ")
  
# For user input
    for i in range(R):          # A for loop for row entries
      a =[]
      for j in range(C):      # A for loop for column entries
         a.append(float(input()))
      matrix.append(a)
    A = np.array(matrix, dtype=np.float_)
    print("==================Result====================")
    print(dimensions(A))
    

while(True):
  linalg()
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


