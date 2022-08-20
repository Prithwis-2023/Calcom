from base64 import b64decode,b64encode
import time
import webbrowser
insertRow = []
print("""
░█████╗░░█████╗░██╗░░░░░░█████╗░░█████╗░███╗░░░███╗  ░██╗░░░░░░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗████╗░████║  ░██║░░██╗░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║  ░╚██╗████╗██╔╝█████╗░░██████╦╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║  ░░████╔═████║░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║  ░░╚██╔╝░╚██╔╝░███████╗██████╦╝
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░""")
#name = input("Please enter your name [Discord usernames are also valid]: ")
#insertRow.append(name)
print("<------------------------------------------------------------------------------------------------->")
#print("Welcome to Calcom! Here you can perform basic arithmetic operations and many more. You will receive instructions (if necessary) for every feature you would use. Remember, if you feel any feature is missing, always use the MiniCalc to complete your calculation. But, remember! Once you close MiniCalc after performing all operations, you will not be able to open it again in a session. So it's recommended to use it at the end, when you are done with all calculations.")

def main():
#Start of code and action
  #print("<------------------------------------------------------------------------------------------------->")
  print(f"Please select from the following operations:")
  print("<------------------------------------------->")
  print(f"Basic Operations\n=============================================\nRoots of Polynomials\n=============================================\nLogarithmic Operations\n=============================================\nNumber Theory\n=============================================\nTrigonometric Operations\n=============================================\nGraphs\n=============================================\nCalculus\n=============================================\nCombinatorial Calculations\n=============================================\nSystem of Equations\n=============================================\nArea Calculations\n=============================================\nVolume Calculations\n=============================================\nBase Conversion\n=============================================\nMeans\n=============================================\nMiniCalc\n=============================================\nFun Zone\n=============================================\nLinear Algebra\n=============================================")
  E = input(f"Enter the operation: ")
  feature_list = ["Basic Operations", "Roots of Polynomials", "Logarithmic Operations", "Number Theory", "Trigonometric Operations", "Graphs", "Calculus", "Combinatorial Calculations", "Area Calculations", "Volume Calculations", "Base Conversion", "MiniCalc", "Fun Zone", "Linear Algebra", "Means", "System of Equations"]
  while (E not in feature_list):
      print("Wrong Input! Please try again.")
      E = input("Enter the operation: ")

  if E == "Basic Operations":
    def basic_calc():
        exp = input("Enter the expression: ")
        exp_list = [char for char in exp]
        # fixes math notation
        for i in range(len(exp_list)):
            # fixes parentheses
            if i < len(exp_list) - 1:
                if exp_list[i].isdigit() and exp_list[i + 1] == '(':
                    exp_list[i + 1] = '*('
                elif exp_list[i] == ')' and exp_list[i + 1].isdigit():
                    exp_list[i] = ')*'
                elif exp_list[i] == ')' and exp_list[i + 1] == '(':
                    exp_list[i] = ')*'
          # fixes powers
            if exp_list[i] == '^':
                exp_list[i] = '**'
            # takes out spaces
            if exp_list[i] == ' ':
                exp_list[i] = ''
        exp = ''.join(exp_list)
        # checks if exp is a valid expression, and evaluates exp if it is
        for char in exp:
            if '()' in exp:
                print("Your input isn't a valid expression.")
                break
            elif char.isdigit() == False and char not in ['+', '-', '*', '.', '/', '(', ')']:
                print("Your input isn't a valid expression.")
                break
        else:
            try:
                print("Answer:", round(eval(exp), 6))
            except:
                print("Your input isn't a valid expression.")

    while True:
        basic_calc()
        contin = ""
        if contin not in ["no", "n", "yes", "y"]:
            contin = input(f"Do you wish to enter another calculation in Basic Operations? (Yes/No): ")
            wish = ["Yes", "No"]
            while (contin not in wish):
              print("Wrong Input! Please try again.")
              contin = input(f"Do you wish to enter another calculation? (Yes/No): ")
            if contin.lower() in ["no", "n"]:
                break
            elif contin.lower() in ["yes", "y"]:
                continue
       
  elif E == "Roots of Polynomials":
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

  elif E == "Logarithmic Operations":
    import math
    def log():
      arg = float(input("Enter the argument: "))
      base = float(input("Enter the base: "))
      while (base < 0):
       print("Please enter a valid base.")
       base = float(input("Enter the base: ")) 
      print(math.log(base, arg))
    while True:
      log()
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
    
  elif E == "Trigonometric Operations":
    import math
    def trig_op():
      print("=============================================\nPlane Trigonometric Operations\n=============================================\nInverse Trigonometric Operations\n=============================================\nHyperbolic Trigonometric Operations\n=============================================")
      f_list = ["Plane Trigonometric Operations", "Inverse Trigonometric Operations", "Hyperbolic Trigonometric Operations"]
      op = input("Choose the type of operation: ")
      while (op not in f_list):
        print("Wrong Input! Please try again.")
        op = input("Choose the type of operation: ")
      if op == "Plane Trigonometric Operations":
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


  elif E == "Graphs":
    def graphs():  
      import numpy as np
      import tkinter as tk
      from tkinter import Tk, BOTTOM, BOTH
      print("<------------------------------------------->\nPlane Trigonometric\n=============================================\nExponential\n=============================================\nLogarithmic\n=============================================\nPolynomial\n=============================================\nJulia Sets\n=============================================\nCustom Data Points\n=============================================\nLissajous Figures\n=============================================")
      d=input("Please enter the type of the function: ")
      f_list = ["Plane Trigonometric", "Exponential", "Logarithmic", "Polynomial", "Julia Sets", "Custom Data Points", "Lissajous Figures"]
      while (d not in f_list):
        print("Wrong Input! Please try again.")
        d = input("Please enter the option: ")
      if d == "Plane Trigonometric":
        b=input("Enter the Trigonometric function (sin(x)/cos(x)/tan(x)): ")
        f_list = ["sin(x)", "cos(x)", "tan(x)"]
        while (b not in f_list):
          print("Wrong Input! Please try again.")
          b=input("Enter the Trigonometric function (sin(x)/cos(x)/tan(x)): ")
        #c=int(input("Enter the number which will be the coeficient of theta (Like enter 2 if the graph is sin(2*theta)...: "))
        if b == "sin(x)":
          import matplotlib.pyplot as plt
          from matplotlib.figure import Figure
          from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
          class Root(Tk):
            def __init__(self):
              super(Root, self).__init__()
              self.title("Graph Window")
              self.minsize(640, 400)
              self.matplotCanvas()
            def matplotCanvas(self):
              f = Figure(figsize=(5,5), dpi=100)
              plt = f.add_subplot(111)
              c=float(input("Enter the number which will be the coeficient of theta (Like enter 2 if the graph is sin(2*theta)...: "))
              x=np.arange(0, c*(np.pi), 0.1)
              y=np.sin(x)
              plt.plot(x,y)
              canvas = FigureCanvasTkAgg(f, self)
              canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
          if __name__ == '__main__':
            root = Root()
            root.mainloop()
        elif b == "cos(x)":
          from matplotlib.figure import Figure
          from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
          class Root(Tk):
            def __init__(self):
              super(Root, self).__init__()
              self.title("Graph Window")
              self.minsize(640, 400)
              self.matplotCanvas()
            def matplotCanvas(self):
              f = Figure(figsize=(5,5), dpi=100)
              plt = f.add_subplot(111)
              c=float(input("Enter the number which will be the coeficient of theta (Like enter 2 if the graph is sin(2*theta)...: "))
              x=np.arange(0, c*(np.pi), 0.1)
              y=np.cos(x)
              plt.plot(x,y)
              canvas = FigureCanvasTkAgg(f, self)
              canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
          if __name__ == '__main__':
            root = Root()
            root.mainloop()
        elif b == "tan(x)":
          from matplotlib.figure import Figure
          from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
          class Root(Tk):
            def __init__(self):
              super(Root, self).__init__()
              self.title("Graph Window")
              self.minsize(640, 400)
              self.matplotCanvas()
            def matplotCanvas(self):
              f = Figure(figsize=(5,5), dpi=100)
              plt = f.add_subplot(111)
              c=float(input("Enter the number which will be the coeficient of theta (Like enter 2 if the graph is sin(2*theta)...: "))
              x=np.arange(0, c*(np.pi), 0.1)
              y=np.tan(x)
              plt.plot(x,y)
              canvas = FigureCanvasTkAgg(f, self)
              canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
          if __name__ == '__main__':
            root = Root()
            root.mainloop()         
              

      elif d == "Exponential":
        from matplotlib.figure import Figure
        from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
        class Root(Tk):
          def __init__(self):
            super(Root, self).__init__()
            self.title("Graph Window")
            self.minsize(640, 400)
            self.matplotCanvas()

          def matplotCanvas(self):
            f = Figure(figsize=(5,5), dpi=100)
            plt = f.add_subplot(111)
            import numpy as np
            c=float(input("Enter the lower bound: "))
            d=float(input("Enter the upper bound: "))
            x=np.arange(c,d,0.1)
            e=2.718281828
            y=np.e**x
            plt.plot(x,y)
            canvas = FigureCanvasTkAgg(f, self)
            canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
        if __name__ == '__main__':
          root = Root()
          root.mainloop()
  
      elif d == "Logarithmic":
        from matplotlib.figure import Figure
        from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
        class Root(Tk):
          def __init__(self):
            super(Root, self).__init__()
            self.title("Graph Window")
            self.minsize(640, 400)
            self.matplotCanvas()

          def matplotCanvas(self):
            f = Figure(figsize=(5,5), dpi=100)
            plt = f.add_subplot(111)
            import numpy as np
            c=float(input("Enter the lower bound: "))
            d=float(input("Enter the upper bound: "))
            x=np.arange(c,d,0.1)
            y=np.log(x)
            plt.plot(x,y)
            canvas = FigureCanvasTkAgg(f, self)
            canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
        if __name__ == '__main__':
          root = Root()
          root.mainloop()
 
      elif d == "Polynomial":
        a_y = input("Enter the type of polynomial graph (Linear/Quadratic/Cubic/Biquadratic): ")
        f_list = ["Linear", "Quadratic", "Biquadratic", "Cubic"]
        while (a_y not in f_list):
          print("Wrong Input! Please try again.")
          a_y = input("Enter the type of polynomial graph (Linear/Quadratic/Cubic/Biquadratic): ")
        if a_y == "Linear":
          from matplotlib.figure import Figure
          from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
          class Root(Tk):
            def __init__(self):
              super(Root, self).__init__()
              self.title("Graph Window")
              self.minsize(640, 400)
              self.matplotCanvas()

            def matplotCanvas(self):
              f = Figure(figsize=(5,5), dpi=100)
              plt = f.add_subplot(111)
              import numpy as np
              a_e = float(input("Enter the coefficient of x: "))
              a_f = float(input("Enter the constant: "))
              a_g=float(input("Enter the lower bound: "))
              a_h=float(input("Enter the uper bound: "))
              x=np.linspace(a_g,a_h,256, endpoint=True)
              y=a_e*(x)+a_f
              plt.plot(x,y)
              canvas = FigureCanvasTkAgg(f, self)
              canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
          if __name__ == '__main__':
            root = Root()
            root.mainloop()
        elif a_y == "Quadratic":
          from matplotlib.figure import Figure
          from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
          class Root(Tk):
            def __init__(self):
              super(Root, self).__init__()
              self.title("Graph Window")
              self.minsize(640, 400)
              self.matplotCanvas()
            def matplotCanvas(self):
              f = Figure(figsize=(5,5), dpi=100)
              plt = f.add_subplot(111)
              a_s=float(input("Enter the coefficient of x^2: "))
              a_d=float(input("Enter the coefficient of x: "))
              a_f=float(input("Enter the constant: "))
              a_g=float(input("Enter the lower bound: "))
              a_h=float(input("Enter the upper bound: "))
              x=np.linspace(a_g,a_h,256, endpoint = True)
              y=(a_s*(x*x))+(a_d*x)+a_f
              plt.plot(x,y)
              canvas = FigureCanvasTkAgg(f, self)
              canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
          if __name__ == '__main__':
            root = Root()
            root.mainloop()

        elif a_y == "Cubic":
          from matplotlib.figure import Figure
          from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
          class Root(Tk):
            def __init__(self):
              super(Root, self).__init__()
              self.title("Graph Window")
              self.minsize(640, 400)
              self.matplotCanvas()

            def matplotCanvas(self):
              f = Figure(figsize=(5,5), dpi=100)
              plt = f.add_subplot(111)
              a_q=float(input("Enter the coefficient of x^3: "))
              a_s=float(input("Enter the coefficient of x^2: "))
              a_d=float(input("Enter the coefficient of x: "))
              a_f=float(input("Enter the constant: "))
              a_g=float(input("Enter the lower bound: "))
              a_h=float(input("Enter the upper bound: "))
              x=np.linspace(a_g,a_h,256, endpoint = True)
              y=(a_q*(x*x*x))+(a_s*(x*x))+(a_d*x)+a_f
              plt.plot(x,y)
              canvas = FigureCanvasTkAgg(f, self)
              canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
          if __name__ == '__main__':
            root = Root()
            root.mainloop()

        elif a_y == "Biquadratic":
          from matplotlib.figure import Figure
          from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
          class Root(Tk):
            def __init__(self):
              super(Root, self).__init__()
              self.title("Graph Window")
              self.minsize(640, 400)
              self.matplotCanvas()

            def matplotCanvas(self):
              f = Figure(figsize=(5,5), dpi=100)
              plt = f.add_subplot(111)
              a_r=float(input("Enter the coefficient of x^4: "))
              a_q=float(input("Enter the coefficient of x^3: "))
              a_s=float(input("Enter the coefficient of x^2: "))
              a_d=float(input("Enter the coefficient of x: "))
              a_f=float(input("Enter the constant: "))
              a_g=float(input("Enter the lower bound: "))
              a_h=float(input("Enter the upper bound: "))
              x=np.linspace(a_g,a_h,256, endpoint = True)
              y=(a_r*(x*x*x*x))+(a_q*(x*x*x))+(a_s*(x*x))+(a_d*x)+a_f
              plt.plot(x,y)
              canvas = FigureCanvasTkAgg(f, self)
              canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
          if __name__ == '__main__':
              root = Root()
              root.mainloop()
      
      elif d == "Julia Sets":
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm
        # Resolution and plot size
        x_res, y_res = 200, 200
        xmin, xmax = -1.5, 1.5
        width = xmax - xmin
        ymin, ymax = -1.5, 1.5
        height = ymax - ymin

        # The mathematical parameters.
        z_abs_max = 10
        max_iter = int(input("Enter the maximum number of iterations (Recommended 1000): "))
        def julia_set(c):
           # Initialise an empty array (corresponding to pixels)
           julia = np.zeros((x_res, y_res))
           for ix in range(x_res):
            for iy in range(y_res):
                # Map pixel position to a point in the complex plane
                z = complex(ix / x_res * width + xmin,
                            iy / y_res * height + ymin)
                iteration = 0
                while abs(z) <= z_abs_max and iteration < max_iter:
                  z = z**2 + c
                  iteration += 1
                iteration_ratio = iteration / max_iter    
                # Set the pixel value to be equal to the iteration_ratio
                julia[ix, iy] = iteration_ratio
             # Plot the array using matplotlib's imshow
           fig, ax = plt.subplots()
           ax.imshow(julia, interpolation='nearest', cmap=cm.gnuplot2)
           plt.axis('off')
           plt.show()
           #fig.savefig('julia_set.png', dpi=500)   
        c = complex(input("Enter the complex number c (Eg. 1+2j): ")) 
        julia_set(c)

      elif d == "Custom Data Points":
        import matplotlib.pyplot as plt
        number = int(input("How many set of data points you want to plot, i.e. how many graphs do you want to have in one plot for comparison: "))
        for i in range(number):
          print("<-------------Enter details for Graph {}------------->".format(i+1))
          points = int(input("Enter the number of data points that you want to plot: "))
          x = []
          y = []
          for k in range(points):
            c = input("Enter the coordinates of the {} point of graph {} in the form of (x,y): ".format(k+1, i+1))
            x.append(c[1])
            y.append(c[3])
          label_s = input("Enter Label for the graph: ")
          plt.plot(x, y, label = label_s)
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        title_s = input("Enter title for the entire plot: ")
        plt.title(title_s)
        plt.legend()
        plt.show()
      
      elif d == "Lissajous Figures":
        import matplotlib.pyplot as plt
        from matplotlib import animation
        import numpy as np

        fig = plt.figure()
        ax = plt.subplot()
        plt.plot(0,0)
        t = np.linspace(-2*np.pi, 2*np.pi, 1000)
        print("""Parametric equation of Lissajous Curves:\n
        x = A * sin(at + d)\n
        y = B * sin(bt)\n
        =================================================\n
        Enter the values of A, B, a, b and d. 
        """)
        A = float(input("Enter the value of A: "))
        B = float(input("Enter the value of B: "))
        a = float(input("Enter the value of a: "))
        d = float(input("Enter the value of d: "))
        b = float(input("Enter the value of b: "))

        def animate(i):
          if i < 500:
            a = b * (0.01 * i)
          else:
            a = b * (0.01 * (1000-i))  
                  
          x = A * np.sin(a*t + d)
          y = B * np.sin(b*t)
          ax.clear()      
          plt.plot(x, y, c = "#E02050", lw = '5')
          return fig,
          
        ani = animation.FuncAnimation(fig, animate, frames = 1000, interval=20, blit=False)
        plt.show()

    while True:
      graphs()
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

    
  elif E == "Calculus":
    print("Instructions:")
    print("-------------------------------------------")
    print(f"1) Use brackets appropiately for correct results.")
    print(f"2) Use exp() for e. Like e^x must be inputted as exp(x).")
    print(f"3) Always represent the variables as instructed.")
    print(f"4) Use +infty or -infty for representing +infinity and -infinity.")
    print(f"5) Use pi for representing the constant pi.")
    #print("5) Use oo for infinity.")
    def calculus():
      import sympy as sp
      from sympy import Symbol
      import scipy.integrate as integrate
      import scipy.special as special
      from scipy.integrate import quad
      #exp = input("Enter the expression: ")
      from numpy import sqrt, sin, cos, pi, exp
      print("<------------------------------------------->\nDifferentiation\n=============================================\nIntegration\n=============================================\nFind Jacobian\n=============================================")
      opt = input("Enter the option: ")
      f_list = ["Differentiation", "Integration", "Find Hessian", "Find Jacobian"]
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
          print("<------------------------------------------->")
          x = sp.Symbol('x')
          exp = input(f"Enter the function: ")
          sol = sp.diff(exp)
          print("=====================Result====================")
          print(sol)
        elif type == "Multi-Variable":
          print("Use only lowercase alphabets as variables.")
          print("<------------------------------------------->")
          v = int(input("Please enter the number of variables: "))
          a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = sp.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
          exp = input("Enter the function: ")
          var = input("Enter the variable in whose respect you want to differentiate: ")
          sol = sp.diff(exp, var)
          print("====================Result=======================")
          print(sol)
      elif opt == "Integration":
        print("<------------------------------------------->\nSingle Integration\n=============================================\nDouble Integration\n=============================================\nTriple Integration\n=============================================")
        f_list = ["Single Integration", "Double Integration", "Triple Integration"]
        opt = input("Enter the option: ")
        while (opt not in f_list):
          print("Wrong Input! Please try again.")
          opt = input("Enter the option: ")
        if opt == "Single Integration":
          import sympy as sp
          from sympy import Symbol, init_printing
          from sympy import oo
          from sympy import sin, cos, tan, sec, sqrt, pi, exp, log, integrate
          init_printing(use_unicode=False, wrap_line=False)
          x = Symbol('x')
          print("Use x as the variable of integration. Use of other alphabets will be treated as constants")
          print("============================================")
          exp = input("Enter the function: ")
          exp_list = [char for char in exp]
          for i in range(len(exp_list)):
            if exp_list[i] == "^":
              exp_list[i] == "**" 
          lb = input("Enter the lower bound: ")
          ub = input("Enter the upper bound: ")
          print("==================Result====================")
          print(integrate(exp, (x, lb, ub)))
        
        elif opt == "Double Integration":  
              import sympy as sp
              from sympy import integrate
              from sympy import symbols, init_printing
              init_printing(use_unicode=False, wrap_line=False)
              x,y=symbols('x y')
              print("Currently, you can only perform indefinite integration. Use only x, y as the variables of integration. Use of other alphabets shall be treated as constants.")
              print("<------------------------------------------->")
              exp=input("Enter the expression: ")
              exp_list = [char for char in exp]
              for i in range(len(exp_list)):
                if exp_list[i] == "^":
                  exp_list[i] == "**"    
              print("======================Result========================")
              print(integrate(exp, x, y))
      
        elif opt == "Triple Integration":
              import sympy as sp
              from sympy import symbols, init_printing, integrate
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

      elif opt == "Find Jacobian":
        import sympy as sym
        import numpy as np
        def Jacobian(v_str, f_list):
          vars = sym.symbols(v_str)
          f = sym.sympify(f_list)
          J = sym.zeros(len(f),len(vars))
          for i, fi in enumerate(f):
            for j, s in enumerate(vars):
              J[i,j] = sym.diff(fi, s)
          return J
        var = int(input("Enter the number of variables: "))
        ls = []
        for i in range(var):
          v = input("Enter the variable {}: ".format(i+1))
          ls.append(v)
          ls.append(' ')
        str1 = "" 
        for ele in ls: 
          str1 += ele
        #print(str1)
        exp = input("Enter the multivariable function: ")
        change = [char for char in exp]
        for i in range(len(change)):
          if change[i] == "^":
            change[i] == "**"
        ex = []
        ex.append(exp)
        res = Jacobian(str1, ex)
        print("================================Result=================================")
        print(res)
        print("=======================================================================")
        print("In the result a**b means a^b. Remember this for future results as well!")
  
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
          

  elif E == "Combinatorial Calculations":
    def combo():
        print("<------------------------------------------->\nFactorial Calculations\n=============================================\nP & C\n=============================================\nAverage Value of Dice Throw\n=============================================")
        f_list = ["Factorial Calculations", "P & C", "Average Value of Dice Throw"]
        q_s = input("Enter the operation: ")
        while (q_s not in f_list):
          print("Wrong Input! Please try again.")
          q_s = input("Enter the operation: ")
        if q_s == "Factorial Calculations":
            W_E = int(input("Enter the number: "))
            fact = 1
            for a in range(1,W_E+1):
              fact = fact*a
            print(fact)
        elif q_s == "P & C":
            print("<------------------------------------------->\nPermutation\n=============================================\nCombination\n=============================================")
            f_list = ["Permutation", "Combination"]
            a=input("Enter the operation: ")
            while (a not in f_list):
              print("Wrong Input! Please try again.")
              a=input("Enter the operation: ")
            if a == "Permutation":
                q_r = int(input("In nPr, enter the value of n: "))
                r_q = int(input("In nPr, enter the value of r: "))
                if q_r < r_q:
                  print("0")
                else:  
                  p_r = q_r-r_q
                  fact = 1
                  for i in range(1,q_r+1):
                      fact=fact*i
                  fact_b = 1
                  for n in range(1,p_r+1):
                      fact_b=fact_b*n
                  print(fact/fact_b)
            elif a == "Combination":
                q_r = int(input("In nCr, please enter the value of n: "))
                r_q = int(input("IN nCr, please enter the value of r: "))
                if q_r < r_q:
                  print("0")
                else:  
                  p_r = q_r-r_q
                  fact = 1
                  for i in range(1,q_r+1):
                      fact=fact*i
                  fact_b = 1
                  for n in range(1,p_r+1):
                      fact_b=fact_b*n
                  fact_c=1
                  for c in range(1,r_q+1):
                      fact_c=fact_c*c
                  print((fact)/(fact_b*fact_c))
        
        elif q_s == "Average Value of Dice Throw":
          from random import randint, seed
          from datetime import datetime

          seed(datetime.now())

          num_rounds = int(input("Enter a really large number as the number of rounds: "))
          sum_of_values = 0

          for _ in range(num_rounds):
            sum_of_values += randint(1, 6)
        
          print("The average is {}".format(sum_of_values/(num_rounds*1.0)))


    while True:
      combo()
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


  elif E == "Area Calculations":
    def area():
        print("<------------------------------------------->\nSquare\n=============================================\nRectangle\n=============================================\nTriangle\n=============================================\nParallelogram\n=============================================\nRhombus\n=============================================\nSphere\n=============================================\nTrapezium\n=============================================\nCircle\n=============================================\nRight Circular Cylinder\n=============================================\nRight Circular Cone\n=============================================")
        a_t = input(f"Enter the shape name: ")
        f_list = ["Square", "Rectangle", "Triangle", "Parallelogram", "Rhombus","Sphere", "Trapezium", "Circle", "Right Circular Cylinder","Right Circular Cone"]
        while (a_t not in f_list):
            print("Wrong Input! Please try again.")
            a_t = input("Enter the shape name: ")

        if a_t == "Square":
            D_E = float(input(f"Enter the side length: "))
            area = (D_E)**2
            print(area)

        elif a_t == "Rectangle":
            D_E = float(input(f"Enter the length: "))
            breadth = float(input(f"Enter the breadth: "))
            area = D_E * breadth
            print(area)

        elif a_t == "Triangle":
            D_E = float(input(f"Enter the base: "))
            BASE = float(input(f"Enter the height: "))
            area = (1 / 2) * (BASE) * (D_E)
            print(area)

        elif a_t == "Parallelogram":
            D_E = float(input("Enter the length of one side: "))
            HEIGHT = float(input("Enter the height: "))
            area = D_E * HEIGHT
            print(area)

        elif a_t == "Rhombus":
            D_E = float(input("Enter the first diagonal: "))
            diagonal = float(input("Enter the second diagonal: "))
            area = 1 / 2 * (D_E * diagonal)
            print(area)

        elif a_t == "Trapezium":
            D_E = float(input("Enter the first base: "))
            base = float(input("Enter the second base: "))
            h_t = float(input("Enter the height: "))
            area = ((D_E + base) / 2) * h_t
            print(area)

        elif a_t == "Circle":
            D_E = float(input("Enter the radius: "))
            area = 3.414 * (D_E)**2
            print(area)

        elif a_t == "Right Circular Cylinder":
            A = float(input("Enter the radius of the base: "))
            ht = float(input("Enter the height: "))
            AREA_a = 2 * 3.414 * A * ht
            print("Curved Surface Area: " + str(AREA_a))
            AREA_b = 2 * 3.414 * A * ht
            print("Total Surface Area: " + str(AREA_b))

        elif a_t == "Sphere":
            R = float(input("Enter the radius: "))
            AREA = 4 * 3.414 * R**2
            print("Area of sphere is: " + str(AREA))

        elif a_t == "Right Circular Cone":
            R = float(input("Enter the radius of the base: "))
            h = float(input("Enter the height: "))
            CSA = 3.414 * R * (R**2 + h**2)**(1 / 2)
            TSA = 3.414 * R * (R + (R**2 + h**2)**(1 / 2))
            print("Curved Surface Area: " + str(CSA))
            print("Total Surface Area: " + str(TSA))


    while True:
        area()
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

    
  elif E == "Volume Calculations":
    def volume():
          print("<------------------------------------------->\nCube\n=============================================\nCuboid\n=============================================\nSphere\n=============================================\nRight Circular Cone\n=============================================\nRight Circular Cylinder\n=============================================\nPrism\n=============================================\nRight Rectangular/Square Pyramidal\n=============================================\nEllipsoid\n=============================================\nTetrahedron\n=============================================")
          f_list = ["Cube", "Cuboid", "Sphere", "Right Circular Cone", "Right Circular Cylinder", "Prism", "Right Rectangular/Square Pyramidal", "Ellipsoid", "Tetrahedron"]
          o = input("Enter the shape: ") 
          while (o not in f_list):
            print("Wrong Input! Please try again.")
            o = input("Enter the shape: ") 
            
          if o == "Cube":
                l = float(input("Enter the length of one side: "))
                print("The volume is: " + str(l**3))

          elif o == "Cuboid":
                l = float(input("Enter the length: "))
                b = float(input("Enter the breadth: "))
                h = float(input("Enter the height: "))
                V = l*b*h
                print("The volume is: " + str(V))

          elif o == "Sphere":
                r = float(input("Enter the radius: "))
                V = (4/3)*3.141592653589793238*(r)**3
                print("The volume is: " + str(V))

          elif o == "Right Circular Cone":
                r = float(input("Enter the radius: "))
                h_l = input("Do you want to enter Slant Height or the Altitude [Type S-H for Slant Height & H for Altitude]: ")
                if h_l == "SH":
                    s_h = float(input("Enter the Slant Height: "))
                    h = (((s_h)**2)-(r**2))**(1/2)
                    V = (1/3)*3.141592653589793238*(r**2)*h
                    print("The Volume is: " + str(V))
                elif h_l == "H":
                    h_o = float(input("Enter the Height: "))
                    V = (1/3)*3.141592653589793238*(r**2)*h_o
                    print("The Volume is: " + str(V))

          elif o == "Right Circluar Cylinder":
                r = float(input("Enter the radius of the base: "))
                h = float(input("Enter the height: "))
                V = 3.141592653589793238*(r**2)*h
                print("The volume is: " + str(V))

          elif o == "Prism":
                print("As you know it... For a square prism, both the length and breadth are the same!")
                print("<----------------------------------------------------------------------------->")
                l = float(input("Enter the length of the base: "))
                b = float(input("Enter the breadth of the base: "))
                h = float(input("Enter the height of the prism: "))
                V = (l*b)*h
                print("The Volume is: " + str(V))

          elif o == "Right-Rectangular/Square-Pyramidal":
                print("For Square Pyramid, both the length and breadth are the same.")
                print("<----------------------------------------------------------->")
                l = float(input("Enter the base length: "))
                b = float(input("Enter the base width: "))
                h = float(input("Enter the height: "))
                V = (l*b)*h
                print("The volume is: " + str(V))

          elif o == "Ellipsoid":
                a = float(input("Enter the first semi axis: "))
                b = float(input("Enter the second semi axis: "))
                c = float(input("Enter the third semi axis: "))
                V = (4/3)*3.141592653589793238*a*b*c
                print("The volume is: " + str(V))

          elif o == "Tetrahedron":
                l = float(input("Enter the length of the edge: "))
                V = (l**3)/(6*(2)**(1/2))
                print("The volume is: " + str(V))
    while True:
      volume()
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


  elif E == "System of Equations":
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


  elif E == "Base Conversion":
    def take_inputs():
        while True:
            # input for initial base
            init_base = input("Initial Base (Between 2 and 36): ")
            if init_base.isdigit() == True:
                init_base = int(init_base)
                if init_base >= 2 and init_base <= 36:
                    break
            print("Invalid Input!")
        while True:
            #input for initial number
            init_num = input("Number: ")
            if init_num.isalnum() == True:
                init_numl = [char for char in init_num]
                # checking if the number in that base is valid
                error = 0
                for i in range(len(init_numl)):
                    if init_numl[i].isalpha() == True:
                        init_numl[i] = ord(init_numl[i].upper()) - 55
                    else:
                        init_numl[i] = int(init_numl[i])
                    if init_numl[i] >= init_base:
                        error += 1
                if error == 0:
                    break
            print("Invalid Input!")
        while True:
            conv_base = input("Convert to Base (Between 2 and 36): ")
            if conv_base.isdigit() == True:
                conv_base = int(conv_base)
                if conv_base >= 2 and conv_base <= 36:
                    input_error = 0
                    return_t = init_base, init_numl, conv_base
                    return return_t
            print("Invalid Input!")

    # converting bases

    def conv_base(ibase, inuml, cbase):
        # first conv to base10
        inuml.reverse()
        base10 = 0
        for i in range(len(inuml)):
            base10 += inuml[i] * ibase ** i
        # next conv base10 to cbase
        cnuml = []
        while base10 != 0:
            cnuml.append(base10 % cbase)
            base10 = base10 // cbase
        cnuml.reverse()
        for i in range(len(cnuml)):
            if cnuml[i] > 9:
                cnuml[i] = chr(cnuml[i] + 55)
            else:
                cnuml[i] = str(cnuml[i])
        conv_num = "".join(cnuml)
        if sum(inuml) == 0:
            conv_num = 0
        print(f"Converted to: {conv_num}")
    def base():
      ti = take_inputs()
      conv_base(ti[0], ti[1], ti[2])
    while True:
      base()
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


  elif E == "MiniCalc":
    import wolframalpha
    print("<----------------------------------------------------->")
    def wolfram():
        input_wolfram = input("Enter your expression/question: ")
        app_id = "UY8J28-REUQGGRJRT"
        client = wolframalpha.Client(app_id)
        result = client.query(input_wolfram)
        try:
          answer = next(result.results).text
          print("<----------------------------------------------------->")
          print(answer)
        except StopIteration:
          print("Invalid Question.")  
    while True:
      wolfram()
      contin = ""
      if contin not in ["no", "n", "yes", "y"]:
        contin = input(f"Do you wish to enter another calculation in MiniCalc? (Yes/No): ")
        wish = ["Yes", "No"]
        while (contin not in wish):
          print("Wrong Input! Please try again.")
          contin = input(f"Do you wish to enter another calculation? (Yes/No): ")
        if contin.lower() in ["no", "n"]:
            break
        elif contin.lower() in ["yes", "y"]:
            continue
    """          
  elif E == "Time Converter(Ext.)":
    import webbrowser
    print("<---------------Powered by CS50---------------->")
    time.sleep(3)
    webbrowser.open('https://time.cs50.io')
    """        
  elif E == "Linear Algebra":
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
      print("<------------------------------------------->\nAddition\n=============================================\nSubtraction\n=============================================\nMultiplication\n=============================================\nSingularity Check\n=============================================\nBasis\n=============================================\nCalculate Dimension\n=============================================")
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

  elif E == "Means":
    def valid_nums(num_list):
        for num in num_list:
            try:
                float(eval(num))
            except:
                return False
        return True

    def arithmetic_mean(num_list):
        return sum(num_list) / len(num_list)

    def geometric_mean(num_list):
        product = 1
        for term in num_list:
            product *= term
        return product ** (1 / len(num_list))

    def harmonic_mean(num_list):
        recip_sum = 0
        for term in num_list:
            recip_sum += 1 / term
        return 1 / (recip_sum / len(num_list))

    def weighted_arithmetic_mean(num_list):
        weight_list = weight_check(num_list)
        if weight_list != False:
            weight_sum = sum(weight_list)
            for i in range(len(num_list)):
                num_list[i] = weight_list[i] * num_list[i]
            return sum(num_list) / weight_sum
        else:
            return False
        
    def weighted_geometric_mean(num_list):
        weight_list = weight_check(num_list)
        if weight_list != False:
            product = 1
            weight_sum = sum(weight_list)
            for i in range(len(num_list)):
                product *= weight_list[i] * num_list[i]
            return product ** (1 / weight_sum)
        else:
            return False

    def weighted_harmonic_mean(num_list):
        weight_list = weight_check(num_list)
        if weight_list != False:
            weight_sum = sum(weight_list)
            recip_sum = 0
            for i in range(len(num_list)):
                recip_sum += weight_list[i] / num_list[i]
            return weight_sum / recip_sum
        else:
            return False

    def weight_check(num_list):
        weight_list = []
        for i in range(len(num_list)):
            try:
                weight = float(eval(input(f"Enter the weight for {num_list[i]}: ")))
            except:
                return False
            weight_list.append(weight)
        return weight_list
        
    def means():
      mean_list = ['<------------------------------------------->', 'Arithmetic Mean', '=============================================', 'Geometric Mean', '=============================================', 'Harmonic Mean', '=============================================', 'Weighted Arithmetic Mean', '=============================================', 'Weighted Geometric Mean', '=============================================', 'Weighted Harmonic Mean', '=============================================']
      for mean_type in mean_list:
          print(mean_type)

      mean_type = input("Enter the type of mean: ")
      while (mean_type not in mean_list):
        print("Wrong Input! Please try again.")
        mean_type = input("Enter the type of mean: ")
      if mean_type in mean_list:
          print('Separate the numbers with a space after a comma (e.g. 3, 4, 0.9)')
          numbers = input("Enter Numbers: ")
          num_list = numbers.split(', ')
          if valid_nums(num_list):
              for i in range(len(num_list)):
                  num_list[i] = eval(num_list[i])
              if mean_type == 'Arithmetic Mean':
                  print(f"The {mean_type} of the numbers is: {round(arithmetic_mean(num_list), 5)}")
              elif mean_type == 'Geometric Mean':
                  print(f"The {mean_type} of the numbers is: {round(geometric_mean(num_list), 5)}")
              elif mean_type == 'Harmonic Mean':
                  print(f"The {mean_type} of the numbers is: {round(harmonic_mean(num_list), 5)}")
              elif mean_type == 'Weighted Arithmetic Mean':
                  wam = weighted_arithmetic_mean(num_list)
                  if wam != False:
                      print(f"The {mean_type} of the numbers is: {round(wam, 5)}")
              elif mean_type == 'Weighted Geometric Mean':
                  wgm = weighted_geometric_mean(num_list)
                  if wgm != False:
                      print(f"The {mean_type} of the numbers is: {round(wgm, 5)}")
              elif mean_type == 'Weighted Harmonic Mean':
                  whm = weighted_harmonic_mean(num_list)
                  if whm != False:
                      print(f"The {mean_type} of the numbers is: {round(whm, 5)}")
              else:
                  print("Invalid Weights.")
          else:
              print("Invalid list of numbers.")
      else:
          print("Your input is not one of options.")

    while True:
      means()
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


  elif E == "Fun Zone":
    print("Welcome to the Calcom Fun-Zone. We have the following features:")
    def fun():
      print("<------------------------------------------->\nDrawing\n=============================================\nPig (Dice Game)\n=============================================\nPlay Connect4\n=============================================")
      f_list = ["Drawing", "Pig (Dice Game)", "Play Connect4"]
      option = input("Enter the option of your choice: ")
      while (option not in f_list):
        print("Wrong Input! Please try again.")
        option = input("Enter the option of your choice: ")
      if option == "Drawing": 
        import turtle
        from turtle import color, begin_fill, pendown, forward, right, end_fill
        print('This part can draw polygons. Describe your shape...')
        sides = int(input('Enter the number of sides: '))
        size = int(input('Size of shape (Number from 10 - 125 for best results): '))
        colour = input('Color of Shape: ')
        def polygon(sides, size, colour):
            pendown()
            color('black', colour)
            begin_fill()
            for i in range(sides):
                forward(size)
                right(360-((sides-2 * 180)/sides)+ 1)
            end_fill()
        polygon(sides, size, colour)

      elif option == "Play Connect4":
        print("""
░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗░█████╗░████████╗  ░░██╗██╗
██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗╚══██╔══╝  ░██╔╝██║
██║░░╚═╝██║░░██║██╔██╗██║██╔██╗██║█████╗░░██║░░╚═╝░░░██║░░░  ██╔╝░██║
██║░░██╗██║░░██║██║╚████║██║╚████║██╔══╝░░██║░░██╗░░░██║░░░  ███████║
╚█████╔╝╚█████╔╝██║░╚███║██║░╚███║███████╗╚█████╔╝░░░██║░░░  ╚════██║
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝░╚════╝░░░░╚═╝░░░  ░░░░░╚═╝
""")
        # connect 4 game :D

        red = "X"
        yellow = "O"
        empty = "-"
        col_num = "1 2 3 4 5 6 7"

        c4_board = [
        ["-", "-", "-", "-", "-", "-", "-"], 
        ["-", "-", "-", "-", "-", "-", "-"], 
        ["-", "-", "-", "-", "-", "-", "-"], 
        ["-", "-", "-", "-", "-", "-", "-"], 
        ["-", "-", "-", "-", "-", "-", "-"], 
        ["-", "-", "-", "-", "-", "-", "-"]]

        # printing c4_board to screen
        def print_board(): 
            print(col_num)
            for row in c4_board:
                for checker in row:
                    print(checker, end = " ")
                print()

        player1 = input("Name of player one (X): ")
        player2 = input("Name of player two (O): ")

        print_board()

        turn = 0
        while True:
            if turn % 2 == 0:
                print(f"{player1}'s turn")
                person = player1
                symbol = red
            else:
                print(f"{player2}'s turn")
                person = player2
                symbol = yellow

            # check if column number is valid:
            while True:
                col = input("Column number (between 1 and 7): ")
                col = str(col)
                if col.isdigit() == True:
                    col = int(col)
                    rcol = col - 1
                    if col >= 1 and col <= 7:
                        if c4_board[0][rcol] == empty:
                            break
                print_board()
                print("Invalid input")
            rrow = 5
            while c4_board[rrow][rcol] != empty:
                rrow -= 1

            c4_board[rrow][rcol] = symbol
            print_board()

            win_mess = False
            # check row
            for i in range(4):
                if c4_board[rrow][i] == c4_board[rrow][i + 1] == c4_board[rrow][i + 2] == c4_board[rrow][i + 3] == symbol:
                    win_mess = True
            # check column
            for i in range(3):
                if c4_board[i][rcol] == c4_board[i + 1][rcol] == c4_board[i + 2][rcol] == c4_board[i + 3][rcol] == symbol:
                    win_mess = True
            # check diagonal slant forward
            drow = rrow - min(rrow, rcol)
            dcol = rcol - min(rrow, rcol)
            if max(drow, dcol) == drow and drow <= 3:
                times = 3 - drow
            elif max(drow, dcol) == dcol and dcol <= 4:
                times = 4 - dcol
            else:
                times = 0
            for i in range(times):
                if c4_board[drow + i][dcol + i] == c4_board[drow + 1 + i][dcol + 1 + i] == c4_board[drow + 2 + i][dcol + 2 + i] == c4_board[drow + 3 + i][dcol + 3 + i] == symbol:
                    win_mess = True
            # check diagonal slant backward
            if rrow + rcol > 6:
                drow = rrow + rcol - 6
                dcol = 6
            else:
                drow = 0
                dcol = rrow + rcol
            i = 0
            while drow + 3 + i <= 5 and dcol - 3 - i >= 0:
                if c4_board[drow + i][dcol - i] == c4_board[drow + 1 + i][dcol - 1 - i] == c4_board[drow + 2 + i][dcol - 2 - i] == c4_board[drow + 3 + i][dcol - 3 - i] == symbol:
                    win_mess = True
                i += 1
            if win_mess == True:
                print(f"Congratulations {person}!! You are the winner!")
                break
            turn += 1

      elif option == "Pig (Dice Game)":
        print("""
██████╗░██╗░██████╗░
██╔══██╗██║██╔════╝░
██████╔╝██║██║░░██╗░
██╔═══╝░██║██║░░╚██╗
██║░░░░░██║╚██████╔╝
╚═╝░░░░░╚═╝░╚═════╝░ 
""")
        import random
        score_p1, score_p2 = 0, 0
        winnum = int(input("Enter the winning number: "))
        while (winnum < 2):
          print("Should be greater than 2. Please try again!")
          winnum = int(input("Enter the winning number: "))
        print(f'This is the dice game called "Pig"\nThe number you roll is added to your score, and you can keep rolling as long as you like, \nbut if you roll a 1 then 0 pts are added to your score. \nFirst to {winnum} wins!')
        player1 = input('Name of player 1: ')
        player2 = input('Name of player 2: ')
        turn = 1

        def play(player, n, score_p1, score_p2):
            num_list = [0]
            move = -1
            while move != 'hold':
                move = input('roll or hold?: ')
                if move == 'roll':
                    num = random.randint(1, 6)
                    print(f'You have rolled a {num}')
                    num_list.append(num)
                    if n == 1:
                        score_p1 += num
                    elif n == 2:
                        score_p2 += num
                    if num == 1:
                        print('Oh... bad luck! you rolled a 1')
                        if n == 1:
                            score_p1 -= sum(num_list)
                        elif n == 2:
                            score_p2 -= sum(num_list)
                        pts = 0
                        break
                if move == 'hold':
                    pts = sum(num_list)
                    print(f'Nice, you earned {pts} points!')
                if n == 1:
                    if score_p1 >= winnum:
                        print("=============================================")
                        print('Hurray! You win :)')
                        return score_p1, score_p2
                        break
                if n == 2:
                    if score_p2 >= winnum:
                        print("=============================================")
                        print('Hurray! You win :)')
                        return score_p1, score_p2
                        break
            return score_p1, score_p2

        while max(score_p1, score_p2) < winnum:
            if turn == 1:
                print('Now it\'s player 1\'s turn!')
                score_p1, score_p2 = play(player1, 1, score_p1, score_p2)
                turn = 2
            elif turn == 2:
                print('Now it\'s player 2\'s turn!')
                score_p1, score_p2 = play(player2, 2, score_p1, score_p2)
                turn = 1
            current_score = f'\n    {player1}\'s score: {score_p1}\n    {player2}\'s score: {score_p2}\n'
            print(current_score)
        
    while True:
      fun()
      contin = ""
      if contin not in ["no", "n", "yes", "y"]:
        contin = input(f"Do you wish to use again? (Yes/No): ")
        wish = ["Yes", "No"]
        while (contin not in wish):
              print("Wrong Input! Please try again.")
              contin = input(f"Do you wish to use again? (Yes/No): ")
        if contin.lower() in ["no", "n"]:
          break
        elif contin.lower() in ["yes", "y"]:
          continue

  elif E == "Number Theory":
    import math
    def nt_i():
      print("Calcom has the following features for Number Theory:")
      print("<------------------------------------------->\nPrime Identification\n=============================================\nPrime Factorization\n=============================================\nDivisibility Test\n=============================================\nSum of Factors\n=============================================\nNumber of Factors\n=============================================\nExponent of a Prime in Prime Factorization\n=============================================\nDiophantine Equations\n=============================================\nPartitions\n=============================================\nG.C.D\n=============================================\nL.C.M\n=============================================")
      f_list = ["Prime Identification", "Divisibility Test", "Diophantine Equations", "Partitions", "G.C.D", "L.C.M", "Prime Factorization", "Sum of Factors", "Number of Factors", "Exponent of a Prime in Prime Factorization"]
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
        import math
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(math.gcd(a,b))

      elif g == "L.C.M":
        import math
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))  
        gcd = math.gcd(a,b)
        lcm = (a*b)/gcd
        print(lcm)

      elif g == "Prime Factorization":
        import math
        n = int(input("Enter the number: "))
        ls = []
        while n%2 == 0:
          ls.append('2')
          ls.append("*")
          n = n/2   
        for i in range(3,int(math.sqrt(n))+1,2):
          while n%i == 0:
            ls.append(str(i))
            ls.append("*")
            n = n/i
        if n>2:
          ls.append(str(int(n)))
          ls.append("*")
        ls.append('1') 
        st1 = " "
        print("Prime Factorization:", st1.join(ls))
      
      elif g == "Sum of Factors":
        import math
        n = int(input("Enter the number: "))
        if (n == 1):
          return 1
        result = 0
        for i in range(2,(int(math.sqrt(n)))+1):
          if (n % i == 0):
            if (i == (n/i)):
                result = result + i
            else:
                result = result + (i + n//i)  
        print("Sum of Factors: ", result+n+1)     
      
      elif g == "Number of Factors":
        n = int(input("Enter the number: "))
        l = []
        for i in range(1, n+1):
          if n % i == 0:
            l.append(i)
        print("Number of Factors:", len(l))   

      elif g == "Exponent of a Prime in Prime Factorization":
        import math
        n = int(input("Enter the number: "))
        prime = int(input("Enter the prime factor of {}: ".format(n)))
        ls = []
        while n%2 == 0:
          ls.append(2)
          n = n/2   
        for i in range(3,int(math.sqrt(n))+1,2):
          while n%i == 0:
            ls.append(i)
            n = n/i
        if n>2:
          ls.append(int(n))
        ls.append(1) 
        cnt = ls.count(prime)
        print("Exponent of {}:".format(prime), cnt) 
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

while True:
  main()
  contin = ""
  if contin not in ["no", "n", "yes", "y"]:
    contin = input(f"Do you wish to return to main menu? (Yes/No): ")
    if contin.lower() in ["no", "n"]:
      break
    elif contin.lower() in ["yes", "y"]:
      continue
      
f_l = input("Are you using Calcom for the first time?(y/n): ")
er = input("Did you face any problem?(Yes/No):")
if er == "Yes":
   print("For providing you the required support, please email us at support@pycalc.com")
elif er == "No":
  print("Great! Consider using me again!")

if f_l == "y":
  webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLScm-4xrSwI4FbetEitzBF2kd2tQgiNOlEhkfiC_lrVRQ4cVdQ/viewform?usp=sf_link')

elif f_l == "n":
   print("To keep you updated, please enter your information. Also join the PyCalc X Discord Server, Invite link: https://discord.gg/uhK3ptyuXZ. Ignore if already joined! ")

time.sleep(10)

