import streamlit as ar
from db_helper import init_db, add_user,verify_user

def main():
    init_db()
    ar.title("login page")
    choice = ar.selectbox("Choose an option", ["Login", "Create Account"])
    if choice == "Create Account":
        ar.subheader("Create New Account")
        new_username = ar.text_input("New Username")
        new_password = ar.text_input("New Password", type="password")
        if ar.button("Create Account"):
            if new_username and new_password:
                add_user(new_username, new_password)
                ar.success(f"Account created for {new_username}!")
            elif not new_username or not new_password:
                ar.error("Please enter both username and password.")
            else:
                ar.error("Account creation failed. Please try again.")
    elif choice == "Login":
        ar.subheader("Login")
        username = ar.text_input("Username")
        password = ar.text_input("Password", type="password")
        if ar.button("Login"):
            if verify_user(username, password):
                ar.success(f"Logged in as {username}!")
            else:
                ar.error("Invalid username or password.")
            # Here you would add logic to authenticate the user

if __name__ == "__main__":
    main()  