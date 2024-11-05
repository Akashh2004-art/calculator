import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("3D Calculator")
        
        self.result_var = tk.StringVar()
        
        # Create result display
        self.result_display = tk.Entry(master, textvariable=self.result_var, font=("Helvetica", 24), bd=5, relief="ridge", justify="right")
        self.result_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button configuration with colors
        buttons = [
            ('C', 1, 0, '#FF6347', 'white'),  # Dark Red
            ('/', 1, 1, '#FF7F50', 'black'),  # Light Coral
            ('*', 1, 2, '#FF8C69', 'black'),  # Light Salmon
            ('-', 1, 3, '#FFD700', 'black'),  # Light Goldenrod
            ('7', 2, 0, '#87CEFA', 'black'),   # Light Sky Blue
            ('8', 2, 1, '#87CEFA', 'black'),   # Light Sky Blue
            ('9', 2, 2, '#87CEFA', 'black'),   # Light Sky Blue
            ('+', 2, 3, '#3CB371', 'white'),    # Medium Sea Green
            ('4', 3, 0, '#B0E0E6', 'black'),   # Light Steel Blue
            ('5', 3, 1, '#B0E0E6', 'black'),   # Light Steel Blue
            ('6', 3, 2, '#B0E0E6', 'black'),   # Light Steel Blue
            ('=', 3, 3, '#C71585', 'white'),   # Medium Violet Red
            ('1', 4, 0, '#FFB6C1', 'black'),   # Light Pink
            ('2', 4, 1, '#FFB6C1', 'black'),   # Light Pink
            ('3', 4, 2, '#FFB6C1', 'black'),   # Light Pink
            ('0', 4, 3, '#E6E6FA', 'black'),   # Lavender
            ('.', 5, 0, '#EEE8AA', 'black')    # Pale Goldenrod
        ]

        for (text, row, col, bg, fg) in buttons:
            self.create_button(text, row, col, bg, fg)

    def create_button(self, text, row, col, bg, fg):
        button = tk.Button(self.master, text=text, font=("Helvetica", 18), command=lambda: self.on_button_click(text), bd=5, relief="raised", bg=bg, fg=fg)
        button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # Configure grid weights for better sizing
        self.master.grid_rowconfigure(row, weight=1)
        self.master.grid_columnconfigure(col, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set("")
        elif char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.geometry("400x600")  # Set size of the window
    root.mainloop()