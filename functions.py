import math
import numpy as np
import matplotlib.pyplot as plt


def quadratic_formula(a: str, b: str, c: str):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return "Invalid input. Please enter numeric values for a, b, and c.\n"

    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        ans1 = round(((b * -1) + math.sqrt(discriminant)) / (2 * a), 4)
        ans2 = round(((b * -1) - math.sqrt(discriminant)) / (2 * a), 4)
        return "ans1: " + str(ans1) + " ans2: " + str(ans2)
    else:
        return "No real solutions.\n"


def standard_deviation():
    try:
        data = input("What is your dataset: ")
        numbers = [float(num) for num in data.split(",")]
    except ValueError:
        return "Invalid input. Please enter a comma-separated list of numeric values.\n"

    if len(numbers) < 2:
        return "At least two numbers are required for standard deviation calculation.\n"

    mean = math.fsum(numbers) / len(numbers)
    total = 0
    for number in numbers:
        squared = (number - mean) ** 2
        total += squared
    variance = total / (len(numbers) - 1)
    if variance >= 0:
        sd = round(math.sqrt(variance), 4)
        return "Mean: " + str(round(mean, 4)) + " Standard Deviation: " + str(sd)
    else:
        return "There is a problem with your dataset. Please try again.\n"


def limit_definition(x_approach: str, l_value: str):
    if x_approach == 'in':
        x_symbol = "N"
        x_range = "(N, ∞)"
        x_algebra = "(x > N)"
    elif x_approach == '-in':
        x_symbol = "N"
        x_range = "(-∞, -N)"
        x_algebra = "(x < -N)"
    else:
        side = input("Is your x approaching from one side (l for left, r for right, n for not): ")
        x_symbol = "𝛿"
        x = float(x_approach)
        if side == "l" or side == "L":
            x_range = f"({x} - 𝛿, {x})"
            x_algebra = f"(0 < |-x - {x}| < 𝛿)"
        elif side == "r" or side == "R":
            x_range = f"({x}, {x} + 𝛿)"
            x_algebra = f"(0 < |x - {x}| < 𝛿)"
        else:
            x_range = f"({x} - 𝛿, {x}) U ({x}, {x} + 𝛿)"
            x_algebra = f"(0 < |x - {x}| < 𝛿)"

    if l_value == 'in':
        y_symbol = "M"
        y_range = "(M, ∞)"
        y_algebra = "(f(x) > M)"
    elif l_value == '-in':
        y_symbol = "M"
        y_range = "(-∞, -M)"
        y_algebra = "(f(x) < -M)"
    else:
        y_symbol = "ε"
        y = float(l_value)
        y_range = f"({y} - ε, {y} + ε)"
        y_algebra = f"(|f(x) - {y}| < ε)"

    limit = (f'Limit Definition: ∀ {y_symbol} > 0 ∃ {x_symbol} > 0 st x in {x_range}'
             f' => f(x) in {y_range}')
    limit_algebra = f'Algebraic Limit: ∀ {y_symbol} > 0 ∃ {x_symbol} > 0 st {x_algebra} => {y_algebra}'
    return limit + "\n" + limit_algebra + "\n"


def newton_method(f, fprime, initial_guess, tolerance=1e-6, max_iterations=100):
    x = initial_guess

    for _ in range(max_iterations):
        f = x**2 - 2
        f_prime = 2 * x

        x = x - f / f_prime
        print(x)

        if abs(f) < tolerance:
            break
    return x


def draw_graph(equation, left_point, right_point):
    x = np.linspace(left_point, right_point, 400)
    y = eval("lambda x: " + equation)(x)

    plt.plot(x, y)
    plt.title("Graph of {}".format(equation))     # set the title for the plot
    plt.xlabel('X-axis')              # set the label for the x-axis
    plt.ylabel('Y-axis')              # set the label for the y-axis
    plt.show()

