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