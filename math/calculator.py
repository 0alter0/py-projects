import tkinter as tk
import math

def press(value):
    current = display.get()

    if current == "Error":
        display.set("")

    display.set(display.get() + value)

def clear():
    display.set("")

def backspace():
    display.set(display.get()[:-1])

def calculate():
    expression = display.get()

    try:
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")
        expression = expression.replace("^", "**")

        allowed = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "abs": abs,
            "round": round
        }

        result = eval(expression, {"__builtins__": {}}, allowed)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        display.set(str(result))

    except:
        display.set("Error")

root = tk.Tk()
root.title("Python Calculator")
root.geometry("400x600")
root.resizable(False, False)

display = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=display,
    font=("Arial", 30),
    justify="right",
    bd=10,
    relief="sunken"
)

entry.pack(
    fill="both",
    padx=10,
    pady=10,
    ipady=15
)

button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both", padx=10, pady=10)

buttons = [
    ["C", "⌫", "(", ")"],
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "^", "+"],
    ["sqrt(", "sin(", "cos(", "="],
]

def button_click(value):
    if value == "C":
        clear()
    elif value == "⌫":
        backspace()
    elif value == "=":
        calculate()
    else:
        press(value)

for row, button_row in enumerate(buttons):
    for col, value in enumerate(button_row):
        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18),
            command=lambda v=value: button_click(v)
        )

        button.grid(
            row=row,
            column=col,
            sticky="nsew",
            padx=3,
            pady=3
        )

for i in range(6):
    button_frame.rowconfigure(i, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)

def keyboard(event):
    key = event.keysym

    if key == "Return":
        calculate()
    elif key == "Escape":
        clear()
    elif key == "BackSpace":
        backspace()

root.bind("<Key>", keyboard)
entry.focus()
root.mainloop()
