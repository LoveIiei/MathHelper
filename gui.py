import tkinter as tk
from tkinter import messagebox
import math
import numpy as np
import matplotlib.pyplot as plt

class Calculator:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for quadratic formula function
        input_frame = tk.Frame(self.root)
        input_frame.pack(padx=10, pady=10)

         # Create labels and entry fields for quadratic formula function
        self.a_label    = tk.Label(input_frame, text="a:")
        self.a_label.grid(row=0, column=0)
        self.a_entry   = tk.Entry(input_frame)
        self.a_entry.grid(row=0, column=1)

        self.b_label   = tk.Label(input_frame, text="b:")
        self.b_label.grid(row=1, column=0)
        self.b_entry   = tk.Entry(input_frame)
        self.b_entry.grid(row=1, column=1)

        self.c_label   = tk.Label(input_frame, text="c:")
        self.c_label.grid(row=2, column=0)
        self.c_entry   = tk.Entry(input_frame)
        self.c_entry.grid(row=2, column=1)  

         # Create buttons for quadratic formula function
        self.quadratic_button  = tk.Button(input_frame, text="Quadratic Formula", command=self.quadratic_formula)
        self.quadratic_button.grid(row=3, column=0, columnspan=2)

         # Create a frame for the inputs and buttons for standard deviation function
        std_dev_frame  = tk.Frame(self.root)
        std_dev_frame.pack(padx=10, pady=10)

         # Create label and entry field for standard deviation function
        self.std_dev_label   = tk.Label(std_dev_frame, text="Enter your dataset (comma-separated numbers):")
        self.std_dev_label.pack()
        self.std_dev_entry  = tk.Entry(std_dev_frame)
        self.std_dev_entry.pack()

         # Create button for standard deviation function
        self.std_dev_button  = tk.Button(std_dev_frame, text="Standard Deviation", command=self.standard_deviation)
        self.std_dev_button.pack()

         # Create a frame for the inputs and buttons for limit definition function
        limit_def_frame  = tk.Frame(self.root)
        limit_def_frame.pack(padx=10, pady=10)

         # Create labels and entry fields for limit definition function
        self.limit_def_a_label    = tk.Label(limit_def_frame, text="a:")
        self.limit_def_a_label.pack()
        self.limit_def_a_entry   = tk.Entry(limit_def_frame)
        self.limit_def_a_entry.pack()

        self.limit_def_b_label    = tk.Label(limit_def_frame, text="b:")
        self.limit_def_b_label.pack()
        self.limit_def_b_entry   = tk.Entry(limit_def_frame)
        self.limit_def_b_entry.pack()

        self.limit_def_c_label    = tk.Label(limit_def_frame, text="c:")
        self.limit_def_c_label.pack()
        self.limit_def_c_entry   = tk.Entry(limit_def_frame)
        self.limit_def_c_entry.pack()  

         # Create button for limit definition function
        self.limit_def_button  = tk.Button(limit_def_frame, text="Limit Definition", command=self.limit_definition)
        self.limit_def_button.pack()

        graph_frame = tk.Frame(self.root)
        graph_frame.pack(padx=10, pady=10)

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
        self.graph_button = tk.Button(graph_frame, text="Draw Graph", command=self.draw_graph)
        self.graph_button.pack()


    def quadratic_formula(self):
        a  = float(self.a_entry.get())
        b  = float(self.b_entry.get())
        c  = float(self.c_entry.get())
        deter = b**2 - 4*a*c
        if deter < 0:
            ans1 = (-b + math.sqrt(-deter)*1j) / (2*a), 4
            ans2 = (-b - math.sqrt(-deter)*1j) / (2*a), 4
            messagebox.showinfo("Solution", f"The solutions are {ans1} and {ans2}")
        else:
            ans1 = round((-b + math.sqrt(deter)) / (2*a), 4)
            ans2 = round((-b - math.sqrt(deter)) / (2*a), 4)
            messagebox.showinfo("Solution", f"The solutions are {ans1} and {ans2}")
        self.root.focus_force()


    def standard_deviation(self):
        dataset  = self.std_dev_entry.get().split(",")
        mean      = np.mean([float(i) for i in dataset])
        variance  = np.var([float(i) for i in dataset], ddof=1)
        if variance > 0:
            std_dev   = math.sqrt(variance)
            messagebox.showinfo("Standard Deviation", f"The standard deviation is {round(std_dev, 4)}, mean is {round(mean, 4)}")
        else:
            messagebox.showerror("Standard Deviation", "The dataset has no variation")
        # self.root.focus_force()


    def limit_definition(self):
        a     = float(self.limit_def_a_entry.get())
        b     = float(self.limit_def_b_entry.get())
        c     = float(self.limit_def_c_entry.get())
        epsilon  = 0   # Assuming epsilon is 0, you can replace this with the actual value if needed

        if a > epsilon and b > epsilon and c > epsilon:
            messagebox.showinfo("Limit Definition", "The limit exists")
        else:
            messagebox.showerror("Limit Definition", "The limit does not exist")


    def draw_graph(self):
        left = float(self.graph_left_entry.get())
        right = float(self.graph_right_entry.get())
        x = np.linspace(left, right, 400)
        y = eval("lambda x: " + self.graph_equ_entry.get())(x)

        plt.plot(x, y)
        plt.title(f"Graph for {self.graph_equ_entry.get()}")
        plt.xlable = "X-axis"
        plt.ylable = "Y-axis"
        plt.show(block=False)
        self.root.focus_force()

if __name__ == "__main__":
    root = tk.Tk()  # Create an instance of Tk()
    root.title("Math Helper")
    app = Calculator(root)
    root.mainloop()
