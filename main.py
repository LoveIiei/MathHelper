from functions import *

i = 0
while i == 0:
    choice = input("What can I help you today (Please enter the number for the function you want to use: \n"
                   "0. Quit the program\n"
                   "1. Quadratic Formula \n"
                   "2. Standard Deviation \n"
                   "3. Limit Definition \n"
                   "4. Newton method \n"
                   "5. Draw Graph \n")
    if choice == "0":
        print("Thank you for using MathHelper -- Owen Hua")
        i += 1
    elif choice == "1":
        a_value = input("What is your a value: ")
        b_value = input("What is your b value: ")
        c_value = input("What is your c value: ")
        print(quadratic_formula(a_value, b_value, c_value))
    elif choice == "2":
        print(standard_deviation())
    elif choice == "3":
        x = input("What is x approaching for you limit (Enter in for ∞, -in for -∞): ")
        l_v = input("What is your L value (What does the limit equal to, enter in for ∞, -in for -∞): ")
        print(limit_definition(x, l_v))
    elif choice == "4":
        f = input("What is the function (E.g x ** 2): ")
        fprime = input("What is the derivative function (E.g 2x): ")
        initial_guess = float(input("What is the initial Guess: "))
        newton_method(f, fprime, initial_guess)
    elif choice == "6":
        equ = input("What is the equation for the graph: ")
        left = int(input("What is the left point of the graph (starts from): "))
        right = int(input("What is the right side of the graph (ends at): "))
        draw_graph(equ, left, right)
    else:
        print(
            "Please re-enter a number that represents the function you want to use. E.g 3 for using limit definition.")
