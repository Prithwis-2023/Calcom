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

