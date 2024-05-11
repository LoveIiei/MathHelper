import tkinter as tk
from tkinter import TRUE, messagebox
import math
import numpy as np
import matplotlib.pyplot as plt
import ast
import webbrowser


class Calculator:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for quadratic formula function
        input_frame = tk.Frame(self.root)
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        # Create labels and entry fields for quadratic formula function
        self.a_label = tk.Label(input_frame, text="a:")
        self.a_label.grid(row=0, column=0)
        self.a_entry = tk.Entry(input_frame)
        self.a_entry.grid(row=0, column=1)

        self.b_label = tk.Label(input_frame, text="b:")
        self.b_label.grid(row=1, column=0)
        self.b_entry = tk.Entry(input_frame)
        self.b_entry.grid(row=1, column=1)

        self.c_label = tk.Label(input_frame, text="c:")
        self.c_label.grid(row=2, column=0)
        self.c_entry = tk.Entry(input_frame)
        self.c_entry.grid(row=2, column=1)

        # Create buttons for quadratic formula function
        self.quadratic_button = tk.Button(
            input_frame, text="Quadratic Formula", command=self.quadratic_formula
        )
        self.quadratic_button.grid(row=3, column=0, columnspan=2)

        # Create a frame for the inputs and buttons for standard deviation function
        std_dev_frame = tk.Frame(self.root)
        std_dev_frame.grid(row=1, column=0, padx=10, pady=10)

        # Create label and entry field for standard deviation function
        self.std_dev_label = tk.Label(
            std_dev_frame, text="Enter your dataset (comma-separated numbers):"
        )
        self.std_dev_label.pack()
        self.std_dev_entry = tk.Entry(std_dev_frame)
        self.std_dev_entry.pack()

        # Create button for standard deviation function
        self.std_dev_button = tk.Button(
            std_dev_frame, text="Standard Deviation", command=self.standard_deviation
        )
        self.std_dev_button.pack()

        # Create a frame for the inputs and buttons for limit definition function
        limit_def_frame = tk.Frame(self.root)
        limit_def_frame.grid(row=2, column=0, padx=10, pady=10)

        # Create labels and entry fields for limit definition function
        self.limit_def_a_label = tk.Label(limit_def_frame, text="a:")
        self.limit_def_a_label.grid(row=0, column=0)
        self.limit_def_a_entry = tk.Entry(limit_def_frame)
        self.limit_def_a_entry.grid(row=0, column=1)

        self.limit_def_b_label = tk.Label(limit_def_frame, text="b:")
        self.limit_def_b_label.grid(row=1, column=0)
        self.limit_def_b_entry = tk.Entry(limit_def_frame)
        self.limit_def_b_entry.grid(row=1, column=1)

        self.limit_def_c_label = tk.Label(limit_def_frame, text="c:")
        self.limit_def_c_label.grid(row=2, column=0)
        self.limit_def_c_entry = tk.Entry(limit_def_frame)
        self.limit_def_c_entry.grid(row=2, column=1)

        # Create button for limit definition function
        self.limit_def_button = tk.Button(
            limit_def_frame, text="Limit Definition", command=self.limit_definition
        )
        self.limit_def_button.grid(row=3, column=0, columnspan=2)

        graph_frame = tk.Frame(self.root)
        graph_frame.grid(row=3, column=0, padx=10, pady=10)

        # labels for draw_graph
        self.graph_equ = tk.Label(graph_frame, text="Equation: ")
        self.graph_equ.pack()
        self.graph_equ_entry = tk.Entry(graph_frame)
        self.graph_equ_entry.pack()

        self.graph_left_label = tk.Label(graph_frame, text="Left side: ")
        self.graph_left_label.pack()
        self.graph_left_entry = tk.Entry(graph_frame)
        self.graph_left_entry.pack()

        self.graph_right_label = tk.Label(graph_frame, text="Right side: ")
        self.graph_right_label.pack()
        self.graph_right_entry = tk.Entry(graph_frame)
        self.graph_right_entry.pack()

        # buttons for draw_graph
        self.graph_button = tk.Button(
            graph_frame, text="Draw Graph", command=self.draw_graph
        )
        self.graph_button.pack()

        # Creating second col for matrix_frame
        matrix_frame = tk.Frame(self.root)
        matrix_frame.grid(row=0, column=1, padx=10, pady=10)
        self.matrix_info = tk.Label(
            matrix_frame, text="Enter matrix like [[1, 2], [3, 4]]"
        )
        self.matrix_info.grid(row=0, column=0)
        self.matrix_1 = tk.Label(matrix_frame, text="Matrix 1: ")
        self.matrix_1.grid(row=1, column=0)
        self.matrix_1_entry = tk.Entry(matrix_frame)
        self.matrix_1_entry.grid(row=1, column=1)
        self.matrix_2 = tk.Label(matrix_frame, text="Matrix 2: ")
        self.matrix_2.grid(row=2, column=0)
        self.matrix_2_entry = tk.Entry(matrix_frame)
        self.matrix_2_entry.grid(row=2, column=1)

        # buttons for matrix operations
        self.matrix_add_button = tk.Button(
            matrix_frame, text="Matrix Operations", command=self.matrix_operation
        )
        self.matrix_add_button.grid(row=3, column=0, columnspan=2)

        link_frame = tk.Frame(self.root)
        link_frame.grid(row=1, column=1, padx=10, pady=10)

        self.derivative_button = tk.Button(
            link_frame,
            text="Derivative Calculator",
            command=lambda: self.open_link(1),
        )
        self.derivative_button.grid(row=0, column=0)

        self.integral_button = tk.Button(
            link_frame,
            text="Integral Calculator",
            command=lambda: self.open_link(2),
        )
        self.integral_button.grid(row=1, column=0)

        self.trig_button = tk.Button(
            link_frame,
            text="Trig Formula",
            command=lambda: self.open_link(3),
        )
        self.trig_button.grid(row=2, column=0)

    def quadratic_formula(self):
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        c = float(self.c_entry.get())
        deter = b**2 - 4 * a * c
        if deter < 0:
            ans1 = (-b + math.sqrt(-deter) * 1j) / (2 * a), 4
            ans2 = (-b - math.sqrt(-deter) * 1j) / (2 * a), 4
            messagebox.showinfo("Solution", f"The solutions are {ans1} and {ans2}")
        else:
            ans1 = round((-b + math.sqrt(deter)) / (2 * a), 4)
            ans2 = round((-b - math.sqrt(deter)) / (2 * a), 4)
            messagebox.showinfo("Solution", f"The solutions are {ans1} and {ans2}")
        self.root.focus_force()

    def standard_deviation(self):
        dataset = self.std_dev_entry.get().split(",")
        mean = np.mean([float(i) for i in dataset])
        variance = np.var([float(i) for i in dataset], ddof=1)
        if variance > 0:
            std_dev = math.sqrt(variance)
            messagebox.showinfo(
                "Standard Deviation",
                f"The standard deviation is {round(std_dev, 4)}, mean is {round(mean, 4)}",
            )
        else:
            messagebox.showerror("Standard Deviation", "The dataset has no variation")
        # self.root.focus_force()

    def limit_definition(self):
        x_approach = self.limit_def_a_entry.get()
        l_value = self.limit_def_b_entry.get()
        if x_approach == "in":
            x_symbol = "N"
            x_range = "(N, ∞)"
            x_algebra = "(x > N)"
        elif x_approach == "-in":
            x_symbol = "N"
            x_range = "(-∞, -N)"
            x_algebra = "(x < -N)"
        else:
            side = self.limit_def_c_entry.get()
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

        if l_value == "in":
            y_symbol = "M"
            y_range = "(M, ∞)"
            y_algebra = "(f(x) > M)"
        elif l_value == "-in":
            y_symbol = "M"
            y_range = "(-∞, -M)"
            y_algebra = "(f(x) < -M)"
        else:
            y_symbol = "ε"
            y = float(l_value)
            y_range = f"({y} - ε, {y} + ε)"
            y_algebra = f"(|f(x) - {y}| < ε)"

        limit = (
            f"Limit Definition: ∀ {y_symbol} > 0 ∃ {x_symbol} > 0 st x in {x_range}"
            f" => f(x) in {y_range}"
        )
        limit_algebra = f"Algebraic Limit: ∀ {y_symbol} > 0 ∃ {x_symbol} > 0 st {x_algebra} => {y_algebra}"
        messagebox.showinfo(limit + "\n" + limit_algebra)

    def draw_graph(self):
        left = float(self.graph_left_entry.get())
        right = float(self.graph_right_entry.get())
        x = np.linspace(left, right, 400)
        y = eval("lambda x: " + self.graph_equ_entry.get())(x)

        plt.plot(x, y)
        plt.title(f"Graph for {self.graph_equ_entry.get()}")
        plt.xlabel = "X-axis"
        plt.ylabel = "Y-axis"
        plt.show(block=False)
        self.root.focus_force()

    def matrix_operation(self):
        matrix1 = self.matrix_1_entry.get()
        matrix2 = self.matrix_2_entry.get()  # Convert the strings to lists of numbers
        matrix1 = ast.literal_eval(matrix1)
        matrix2 = ast.literal_eval(matrix2)
        matrix1 = np.array(matrix1)
        matrix2 = np.array(matrix2)
        addition = matrix1 + matrix2
        result_subtraction = matrix1 - matrix2
        result_multiplication = np.dot(matrix1, matrix2)
        matrix3 = np.transpose(matrix1)
        matrix4 = np.transpose(matrix2)
        determinant_matrix1 = np.linalg.det(matrix1)
        determinant_matrix2 = np.linalg.det(matrix2)
        inverse_matrix1 = np.linalg.inv(matrix1)
        inverse_matrix2 = np.linalg.inv(matrix2)
        eigen_values, eigen_vectors = np.linalg.eig(matrix1)
        messagebox.showinfo(
            "Addition",
            f"Addtion: {addition},\n Subtraction: {result_subtraction},\n "
            + f"Multiplication: {result_multiplication},\n TranposeM1: {matrix3},\n DeterM1: {determinant_matrix1},\n "
            + f"InverseM1: {inverse_matrix1},\n TranposeM2: {matrix4},\n DeterM2: {determinant_matrix2},\n InverseM2: {inverse_matrix2},\n "
            + f"EigenValues: {eigen_values},\n EigenVectors: {eigen_vectors}",
        )
        self.root.focus_force()

    def open_link(self, name: int):
        if name == 1:
            webbrowser.open("https://www.derivative-calculator.net/")
        elif name == 2:
            webbrowser.open("https://www.integral-calculator.com/")
        elif name == 3:
            webbrowser.open("https://tutorial.math.lamar.edu/pdf/trig_cheat_sheet.pdf")


if __name__ == "__main__":
    root = tk.Tk()  # Create an instance of Tk()
    root.title("Math Helper")
    app = Calculator(root)
    root.mainloop()
