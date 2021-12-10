
# means code

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
  mean_list = ['*********************************************', 'Arithmetic Mean', '=============================================', 'Geometric Mean', '=============================================', 'Harmonic Mean', '=============================================', 'Weighted Arithmetic Mean', '=============================================', 'Weighted Geometric Mean', '=============================================', 'Weighted Harmonic Mean', '=============================================']
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
