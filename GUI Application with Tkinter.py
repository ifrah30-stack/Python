# Simple calculator GUI application
import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("300x400")
        
        self.current_input = ""
        self.create_widgets()
    
    def create_widgets(self):
        # Display widget
        self.display = tk.Entry(self.root, font=('Arial', 20), justify='right', bd=10)
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('⌫', 5, 3)
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            btn = tk.Button(
                self.root, text=text, font=('Arial', 15),
                command=lambda t=text: self.on_button_click(t),
                height=2, width=5
            )
            btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
        
        # Configure grid weights
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.current_input)
                self.current_input = str(result)
                self.display.delete(0, tk.END)
                self.display.insert(0, self.current_input)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid expression: {e}")
                self.current_input = ""
                self.display.delete(0, tk.END)
        
        elif char == 'C':
            self.current_input = ""
            self.display.delete(0, tk.END)
        
        elif char == '⌫':
            self.current_input = self.current_input[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_input)
        
        else:
            self.current_input += char
            self.display.insert(tk.END, char)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
