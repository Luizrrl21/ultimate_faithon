import streamlit as st

usuarios = [{"usuario":"Luiz", "senha":"12345"}]

def login(usuario, senha):
    for i in usuarios:
        if i["login"] == usuario and i["senha"] == senha:
            st.write("Login efetuado")

st.write("Login")
user = st.text_input("Usuário")
password = st.text_input("senha")
bt_login = st.button("Login", on_click=login(user, password))
