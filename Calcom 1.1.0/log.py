import math
def log():
  a=float(input("Enter the number: "))
        #import math
  print(math.log(a))
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