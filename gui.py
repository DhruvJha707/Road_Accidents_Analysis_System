import tkinter as tk
from tkinter import messagebox
from analysis import load_data, transform_data, clean_data, plot_yearly_trend, plot_top_states

# Load data
df = load_data()
df = transform_data(df)
df = clean_data(df)


# ---------------- FUNCTIONS ----------------
def show_trend():
    plot_yearly_trend(df)

def show_top_states():
    plot_top_states(df)

def show_info():
    messagebox.showinfo("About",
                        "Road Accident Analysis System\n\n"
                        "Built using:\nTkinter, Pandas, Matplotlib, NumPy")


# ---------------- GUI WINDOW ----------------
root = tk.Tk()
root.title("Road Accident Analysis System")
root.geometry("600x450")
root.configure(bg="#1e1e2f")  # Dark background


# ---------------- TITLE ----------------
title = tk.Label(root,
                 text="🚗 Road Accident Analysis System",
                 font=("Helvetica", 18, "bold"),
                 bg="#1e1e2f",
                 fg="white")
title.pack(pady=20)


# ---------------- FRAME ----------------
frame = tk.Frame(root, bg="#2c2c3e", bd=2, relief="ridge")
frame.pack(pady=20, padx=20, fill="both", expand=True)


# ---------------- BUTTON STYLE FUNCTION ----------------
def create_button(text, command, color):
    return tk.Button(frame,
                     text=text,
                     command=command,
                     font=("Arial", 12, "bold"),
                     bg=color,
                     fg="white",
                     width=25,
                     height=2,
                     bd=0,
                     activebackground="#444",
                     cursor="hand2")


# ---------------- BUTTONS ----------------
btn1 = create_button("📈 Show Yearly Trend", show_trend, "#4CAF50")
btn1.pack(pady=10)

btn2 = create_button("📊 Top Dangerous States", show_top_states, "#2196F3")
btn2.pack(pady=10)

btn3 = create_button("ℹ️ Project Info", show_info, "#9C27B0")
btn3.pack(pady=10)

btn4 = create_button("❌ Exit", root.quit, "#f44336")
btn4.pack(pady=20)


# ---------------- FOOTER ----------------
footer = tk.Label(root,
                  text="B.Tech Python Capstone Project",
                  font=("Arial", 10),
                  bg="#1e1e2f",
                  fg="lightgray")
footer.pack(pady=10)


# ---------------- RUN ----------------
root.mainloop()