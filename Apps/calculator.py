import tkinter as tk
from tkinter import ttk

# Simple Tkinter Calculator
# Run: python calculator.py

ALLOWED_CHARS = set("0123456789+-*/(). %")  # Allowed characters for input

class Calculator(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=12)
        self.master = master
        self.master.title("Calculator")  # Set window title
        self.master.resizable(True, True)  # Allow window resizing
        self.expression = tk.StringVar(value="")  # Stores the current expression

        # Styles
        style = ttk.Style()
        try:
            style.theme_use('xpnative') # Set theme (fallback if not available) classic, alt, clam, default, winnative, xpnative, vista, aqua
        except Exception:
            pass
        style.configure('TButton', padding=8, font=('bold'))  # Button style
        style.configure('Display.TEntry', padding=8, font=('Segoe UI', 12))  # Display style

        # Display (Entry widget for showing the expression/result)
        self.display = ttk.Entry(self, textvariable=self.expression, justify='right', width=22, font=('Segoe UI', 18))
        self.display.grid(row=0, column=0, columnspan=4, sticky='ew', pady=(0, 8))
        self.display.focus_set()  # Focus on display at start

        # Button layout: (text, row, column, command)
        buttons = [
            ('C', 1, 0, self.clear),  # Clear button
            ('(', 1, 1, lambda: self.add_char('(')),  # Open parenthesis
            (')', 1, 2, lambda: self.add_char(')')),  # Close parenthesis
            ('←', 1, 3, self.backspace),  # Backspace button
            ('/', 2, 3, lambda: self.add_char('/')),  # Division
            ('*', 3, 3, lambda: self.add_char('*')),  # Multiplication
            ('-', 4, 3, lambda: self.add_char('-')),  # Subtraction
            ('.', 5, 1, lambda: self.add_char('.')),  # Decimal point
            ('=', 5, 2, self.calculate),  # Equals button
            ('+', 5, 3, lambda: self.add_char('+')),  # Addition
            ('0', 5, 0, lambda: self.add_char('0')),  # Number buttons
            ('1', 4, 0, lambda: self.add_char('1')),
            ('2', 4, 1, lambda: self.add_char('2')),
            ('3', 4, 2, lambda: self.add_char('3')),
            ('4', 3, 0, lambda: self.add_char('4')),
            ('5', 3, 1, lambda: self.add_char('5')),
            ('6', 3, 2, lambda: self.add_char('6')),
            ('7', 2, 0, lambda: self.add_char('7')),  
            ('8', 2, 1, lambda: self.add_char('8')),
            ('9', 2, 2, lambda: self.add_char('9')),
        ]

        # Create and place buttons on the grid
        for (text, r, c, cmd) in buttons:
            btn = ttk.Button(self, text=text, command=cmd)
            btn.grid(row=r, column=c, padx=4, pady=4, sticky='nsew')

        # Make columns and rows expandable
        for i in range(4):
            self.columnconfigure(i, weight=1)
        for i in range(6):
            self.rowconfigure(i, weight=1)

        # Keyboard bindings for calculator actions
        self.master.bind('<Key>', self.on_key)  # Handle keypresses
        self.master.bind('<Return>', lambda e: self.calculate())  # Enter key
        self.master.bind('<KP_Enter>', lambda e: self.calculate())  # Numpad Enter
        self.master.bind('<BackSpace>', lambda e: self.backspace())  # Backspace key
        self.master.bind('<Escape>', lambda e: self.clear())  # Escape key

        self.pack(fill='both', expand=True)  # Fill window

    def add_char(self, ch: str):
        """Add a character to the expression."""
        self.expression.set(self.expression.get() + ch)

    def clear(self):
        """Clear the expression."""
        self.expression.set("")

    def backspace(self):
        """Remove the last character from the expression."""
        self.expression.set(self.expression.get()[:-1])

    def sanitize(self, expr: str) -> str:
        """Allow only safe characters in the expression."""
        filtered = ''.join(ch for ch in expr if ch in ALLOWED_CHARS)
        return filtered

    def calculate(self):
        """Evaluate the expression and display the result."""
        expr = self.expression.get()
        expr = self.sanitize(expr)
        if not expr:
            return
        try:
            # Evaluate in a restricted namespace for safety
            result = eval(expr, {"__builtins__": None}, {})
            self.expression.set(str(result))
        except Exception:
            self.flash_error()  # Show error if evaluation fails

    def flash_error(self):
        """Flash the display red to indicate an error."""
        self.display.cget('foreground') if hasattr(self.display, 'cget') else None
        try:
            self.display.configure(foreground='red')
            self.master.after(250, lambda: self.display.configure(foreground='black'))
        except Exception:
            pass

    def on_key(self, event):
        """Handle keypress events for input validation."""
        ch = event.char
        if ch and ch in ALLOWED_CHARS:
            # Let normal keypress type into the entry
            return
        # Block anything else (including letters)
        if event.keysym in ('Return', 'KP_Enter', 'BackSpace', 'Escape', 'Left', 'Right', 'Delete', 'Home', 'End'):
            return
        return 'break'  # Prevent unwanted key input


def main():
    """Main function to run the calculator app."""
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


if __name__ == '__main__':
    main()