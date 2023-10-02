import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.current_input = ""
        self.has_error = False
        self.valid_characters = set("123456789+-*/.=")  # Define valid input characters excluding '0'
        self.create_ui()

    def create_ui(self):
        self.create_entry()
        self.create_buttons()

    def create_entry(self):
        self.entry = tk.Entry(self.root, textvariable=self.result_var, font=("Helvetica", 20), bd=10, insertwidth=4, width=14,
                              justify='right', state="readonly")
        self.entry.grid(row=0, column=0, columnspan=5)
        self.entry.bind("<KeyPress>", self.on_entry_key_press)  # Bind keypress event to the entry field

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        button_width = 4  # Uniform button width
        button_height = 2  # Uniform button height
        row, col = 2, 0
        for button in buttons:
            tk.Button(self.root, text=button, padx=10, pady=10, font=("Helvetica", 20),
                      command=lambda b=button: self.on_button_click(b), width=button_width, height=button_height).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        clear_button = tk.Button(self.root, text="C", padx=10, pady=10, font=("Helvetica", 20),
                                 command=lambda b="C": self.on_button_click(b), width=button_width, height=button_height)
        clear_button.grid(row=1, column=0, columnspan=1, sticky='w')

        # Add a Backspace button to the right of the "C" button in the 4th row
        backspace_button = tk.Button(self.root, text="?", padx=10, pady=10, font=("Helvetica", 20),
                                     command=lambda b="?": self.on_button_click(b), width=button_width, height=button_height)
        backspace_button.grid(row=1, column=3, columnspan=1, sticky='w')  # Positioned in the 4th column, 4th row

    def update_display(self):
        if len(self.current_input) > 14:
            self.result_var.set(self.current_input[-14:])
        else:
            self.result_var.set(self.current_input)

    def on_button_click(self, button):
        if button == 'C':
            self.current_input = ""
            self.has_error = False
        elif button == '?':  # Handle backspace button
            if self.current_input and not self.has_error:
                self.current_input = self.current_input[:-1]  # Remove the last character
        elif self.has_error:
            return
        elif button == '=':
            try:
                result = eval(self.current_input)
                # Check if the result is an integer and format accordingly
                if result == int(result):
                    self.current_input = str(int(result))
                else:
                    self.current_input = str(result)
            except Exception:
                self.current_input = "Error"
                self.has_error = True
        else:
            # Check if the input is a valid character
            if (button in self.valid_characters) or (button == '0' and self.current_input != ""):
                self.current_input += button

        self.update_display()

    def on_entry_key_press(self, event):
        key = event.char
        if key:
            if key == '\r':
                key = '='  # Treat Enter/Return key as '='
            if key in self.valid_characters:
                self.on_button_click(key)
        return "break"

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
