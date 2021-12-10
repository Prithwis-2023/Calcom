def combo():
    print("*********************************************\nFactorial Calculations\n=============================================\nP & C\n=============================================\nAverage Value of Dice Throw\n=============================================")
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
        print("*********************************************\nPermutation\n=============================================\nCombination\n=============================================")
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



