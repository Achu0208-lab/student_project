import streamlit as ar
ar.set_page_config(page_title="Login Page", layout="centered")
with ar.container():
    ar.title("Login Page")
username = ar.text_input("Username")
password = ar.text_input("Password", type="password")
if ar.button("Login"):
    if username == "admin" and password == "password":
        ar.success("Login successful!")
    else:
        ar.error("Invalid username or password.")
