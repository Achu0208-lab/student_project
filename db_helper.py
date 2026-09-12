import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login and Signup App")
root.configure(bg="#121212")
root.geometry("400x400")

# Functions
def show_login():
    signup_frame.pack_forget()
    login_frame.pack(pady=20)

def show_signup():
    login_frame.pack_forget()
    signup_frame.pack(pady=20)

def toggle_password(entry, btn):
    if entry.cget("show") == "":
        entry.config(show="*")
        btn.config(text="👁️")
    else:
        entry.config(show="")
        btn.config(text="🙈")

def login():
    user = login_user.get()
    pwd = login_pass.get()
    messagebox.showinfo("Login", f"Logging in with Username: {user}, Password: {pwd}")

def signup():
    user = signup_user.get()
    pwd = signup_pass.get()
    messagebox.showinfo("Signup", f"Signing up with Username: {user}, Password: {pwd}")

# Title
title = tk.Label(root, text="🔒 Login and Signup App", fg="white", bg="#121212", font=("Arial", 16))
title.pack(pady=10)

# Buttons
btn_login = tk.Button(root, text="🔑 Go to Login", bg="#e53935", fg="white", command=show_login)
btn_login.pack(pady=5)

btn_signup = tk.Button(root, text="📄 Go to Sign Up", bg="#333", fg="white", command=show_signup)
btn_signup.pack(pady=5)

# Login Frame
login_frame = tk.Frame(root, bg="#1e1e1e")
tk.Label(login_frame, text="Login Section", fg="#e53935", bg="#1e1e1e", font=("Arial", 14)).pack(pady=10)

login_user = tk.Entry(login_frame, width=30)
login_user.insert(0, "👤 Username")
login_user.pack(pady=5)

login_pass = tk.Entry(login_frame, width=25, show="*")
login_pass.pack(side="left", padx=5, pady=5)
login_toggle = tk.Button(login_frame, text="👁️", command=lambda: toggle_password(login_pass, login_toggle))
login_toggle.pack(side="left")

tk.Button(login_frame, text="Login", bg="#333", fg="white", command=login).pack(pady=10)

# Signup Frame
signup_frame = tk.Frame(root, bg="#1e1e1e")
tk.Label(signup_frame, text="Signup Section", fg="#e53935", bg="#1e1e1e", font=("Arial", 14)).pack(pady=10)

signup_user = tk.Entry(signup_frame, width=30)
signup_user.insert(0, "👤 Username")
signup_user.pack(pady=5)

signup_pass = tk.Entry(signup_frame, width=25, show="*")
signup_pass.pack(side="left", padx=5, pady=5)
signup_toggle = tk.Button(signup_frame, text="👁️", command=lambda: toggle_password(signup_pass, signup_toggle))
signup_toggle.pack(side="left")

tk.Button(signup_frame, text="Sign Up", bg="#333", fg="white", command=signup).pack(pady=10)

root.mainloop()
