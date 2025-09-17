import tkinter as tk

root = tk.Tk()
root.title("TextBox Input")
root.geometry('400x200')

# Function to display input
def show_input():
    lbl.config(text=f"Input: {txt.get('1.0', 'end-1c')}")

# TextBox for input
txt = tk.Text(root, height=5, width=40)
txt.pack()

# Button to print input
btn = tk.Button(root, text="Print", command=show_input)
btn.pack()

# Label to display input
lbl = tk.Label(root, text="")
lbl.pack()

root.mainloop()