import sqlite3
import streamlit as ar

def init_db():
    """Create database file and user table if it doesn't exist."""
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, password):
    """Add a new user to the database."""
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        # Username already exists
        return False

def verify_user(username, password):
    """Check if username and password match."""
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None


# Initialize database when app starts
init_db()

ar.set_page_config(page_title="Login and Signup App", page_icon="🔒", layout="centered")

# Custom CSS for dark theme UI (Completed and Fixed)
ar.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    div.stButton > button[kind="primary"] {
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 6px;
        border: none;
        height: 42px;
        font-weight: 600;
        width: 100%;
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #262933 !important;
        border-radius: 8px;
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

ar.markdown('<div class="main-title">Account Portal</div>', unsafe_allow_html=True)

# Tabs to separate Login and Registration forms
tab1, tab2 = ar.tabs(["🔑 Login", "📝 Sign Up"])

with tab1:
    ar.subheader("Sign In")
    login_user = ar.text_input("Username", key="login_username")
    login_pass = ar.text_input("Password", type="password", key="login_password")
    
    if ar.button("Log In", type="primary", key="login_btn"):
        if login_user and login_pass:
            if verify_user(login_user, login_pass):
                ar.success(f"Welcome back, {login_user}!")
            else:
                ar.error("Invalid username or password.")
        else:
            ar.warning("Please fill out all fields.")

with tab2:
    ar.subheader("Register Account")
    new_user = ar.text_input("Choose a Username", key="signup_username")
    new_pass = ar.text_input("Choose a Password", type="password", key="signup_password")
    confirm_pass = ar.text_input("Confirm Password", type="password", key="confirm_password")
    
    if ar.button("Register", type="primary", key="signup_btn"):
        if new_user and new_pass and confirm_pass:
            if new_pass != confirm_pass:
                ar.error("Passwords do not match.")
            elif add_user(new_user, new_pass):
                ar.success("Registration successful! You can now switch to the Log In tab.")
            else:
                ar.error("That username is already taken.")
        else:
            ar.warning("Please fill out all fields.")
