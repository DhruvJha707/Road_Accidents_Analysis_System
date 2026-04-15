import tkinter as tk
from tkinter import messagebox
from analysis import load_data, transform_data, clean_data, plot_yearly_trend, plot_top_states

# ---------------- ROOT ----------------
root = tk.Tk()
root.title("Road Accident Analysis System")
root.state("zoomed")
root.configure(bg="#1e1e2f")

# ---------------- LOAD DATA ----------------
df = clean_data(transform_data(load_data()))

# ---------------- FUNCTIONS ----------------
def show_trend():
    plot_yearly_trend(df)

def show_top_states():
    plot_top_states(df)

def show_info():
    messagebox.showinfo("About",
                        "Road Accident Analysis System\n\n"
                        "Built using:\nTkinter, Pandas, Matplotlib, NumPy")

def go_to_dashboard():
    start_frame.pack_forget()
    dashboard_frame.pack(fill="both", expand=True)

def go_to_home():
    dashboard_frame.pack_forget()
    start_frame.pack(fill="both", expand=True)

# ---------------- FRAMES ----------------
start_frame = tk.Frame(root, bg="#141422")
dashboard_frame = tk.Frame(root, bg="#1e1e2f")

# =========================================================
# 🔷 START PAGE (PROFESSIONAL)
# =========================================================
canvas = tk.Canvas(start_frame, bg="#141422", highlightthickness=0)
canvas.pack(fill="both", expand=True)

def draw_background(event=None):
    canvas.delete("all")

    w = canvas.winfo_width()
    h = canvas.winfo_height()

    # Background gradient effect
    for i in range(0, h, 2):
        canvas.create_line(0, i, w, i, fill="#1e1e2f")

    # Decorative shapes
    canvas.create_oval(-100, -100, 300, 300, fill="#2a2a40", outline="")
    canvas.create_oval(w-300, h-300, w+100, h+100, fill="#2a2a40", outline="")

    # Center card
    card_w, card_h = 500, 320
    x1 = (w - card_w) // 2
    y1 = (h - card_h) // 2
    x2, y2 = x1 + card_w, y1 + card_h

    canvas.create_rectangle(x1, y1, x2, y2, fill="#1e1e2f", outline="")

    # Title
    canvas.create_text(w//2, y1+70,
                       text="🚗 Road Accident Analysis",
                       fill="white",
                       font=("Helvetica", 22, "bold"))

    # Subtitle
    canvas.create_text(w//2, y1+120,
                       text="Data-driven insights for safer roads",
                       fill="lightgray",
                       font=("Arial", 12))

    # Button
    canvas.create_window(w//2, y1+200, window=enter_btn)

canvas.bind("<Configure>", draw_background)

# ENTER button
def on_enter(e):
    enter_btn.config(bg="#66bb6a")

def on_leave(e):
    enter_btn.config(bg="#4CAF50")

enter_btn = tk.Button(start_frame,
                      text="ENTER DASHBOARD",
                      command=go_to_dashboard,
                      font=("Arial", 14, "bold"),
                      bg="#4CAF50",
                      fg="white",
                      width=20,
                      height=2,
                      bd=0,
                      cursor="hand2")

enter_btn.bind("<Enter>", on_enter)
enter_btn.bind("<Leave>", on_leave)

start_frame.pack(fill="both", expand=True)

# =========================================================
# 🔷 DASHBOARD (CENTERED PROFESSIONAL UI)
# =========================================================

# Main container
main_container = tk.Frame(dashboard_frame, bg="#1e1e2f")
main_container.pack(expand=True)

# Card
card = tk.Frame(main_container, bg="#2c2c3e", padx=50, pady=50)
card.pack(padx=200)

# Title
title = tk.Label(card,
                 text="📊 Dashboard",
                 font=("Helvetica", 26, "bold"),
                 bg="#2c2c3e",
                 fg="white")
title.pack(pady=(0, 30))

# Button style
def create_button(text, command, color):
    return tk.Button(card,
                     text=text,
                     command=command,
                     font=("Arial", 14, "bold"),
                     bg=color,
                     fg="white",
                     width=30,
                     height=2,
                     bd=0,
                     activebackground="#555",
                     cursor="hand2")

# Buttons
create_button("📈 Show Yearly Trend", show_trend, "#4CAF50").pack(pady=10)
create_button("📊 Top Dangerous States", show_top_states, "#2196F3").pack(pady=10)
create_button("ℹ️ Project Info", show_info, "#9C27B0").pack(pady=10)
create_button("🏠 Back to Home", go_to_home, "#FF9800").pack(pady=10)
create_button("❌ Exit", root.quit, "#f44336").pack(pady=(20, 0))

# Footer
footer = tk.Label(dashboard_frame,
                  text="B.Tech Python Capstone Project",
                  font=("Arial", 10),
                  bg="#1e1e2f",
                  fg="lightgray")
footer.pack(pady=10)

# ---------------- RUN ----------------
root.mainloop()