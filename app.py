import streamlit as ar
ar.set_page_config(page_title="Login Page", layout="centered")
with ar.container():
    ar.title("Login Page")
username = ar.text_input("Username")
password = ar.text_input("Password", type="password")
if ar.button("Login"):
    if username == "ASHWIN" and password == "Achu@2008":
        ar.success("login successful! and welcome to Ashwin's world.")
    else:
        ar.error("user name and password check pannu pa thambi.")
