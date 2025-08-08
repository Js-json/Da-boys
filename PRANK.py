import tkinter as tk
from tkinter import messagebox
import random

def generate_problems():
    global x_answer, y_answer
    x1, x2 = random.randint(10, 40), random.randint(2, 20)
    y1, y2 = random.randint(10, 40), random.randint(2, 20)
    x_answer = x1 * x2
    y_answer = y1 * y2
    problem1_label.config(text=f"Solve for X: {x1} × {x2}")
    problem2_label.config(text=f"Solve for Y: {y1} × {y2}")

def update_mouse_position(event):
    coords_label.config(text=f"Mouse: ({event.x}, {event.y})")

def on_click(event):
    click_x, click_y = event.x, event.y
    print(f"Clicked at: ({click_x}, {click_y})")
    margin = 10
    if abs(click_x - x_answer) <= margin and abs(click_y - y_answer) <= margin:
        messagebox.showinfo("✅ You Escaped!", "Correct! Closing app...")
        root.destroy()
    else:
        status_label.config(text="❌ Wrong spot. Try again.")

def disable_alt_f4():
    # ALT+F4 triggers window close event
    # Override the window close protocol
    pass  # Do nothing!

# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("Math Gate")
root.attributes("-fullscreen", True)
root.configure(bg="black")

# Disable ALT+F4 and window close
root.protocol("WM_DELETE_WINDOW", disable_alt_f4)

# Display math problems
problem1_label = tk.Label(root, text="", font=("Consolas", 28), fg="white", bg="black")
problem1_label.pack(pady=20)

problem2_label = tk.Label(root, text="", font=("Consolas", 28), fg="white", bg="black")
problem2_label.pack(pady=10)

instructions = tk.Label(root,
    text="🔐 Click the exact coordinate (X, Y) = your answers to escape.",
    font=("Arial", 18), fg="gray", bg="black"
)
instructions.pack(pady=20)

coords_label = tk.Label(root, text="Mouse: (0, 0)", font=("Arial", 16), fg="yellow", bg="black")
coords_label.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 16), fg="red", bg="black")
status_label.pack(pady=10)

generate_problems()

# Bind movement + click
root.bind("<Motion>", update_mouse_position)
root.bind("<Button-1>", on_click)

# Block ALT+F4: capture <Alt-F4> and do nothing
def block_alt_f4(event):
    return "break"  # Stop event from propagating

root.bind("<Alt-F4>", block_alt_f4)

# Optional: disable Escape key too
root.bind("<Escape>", lambda e: "break")

root.mainloop()
