import streamlit as st

produtos = []

def add(nome, qtd, preco):
    produto = {
        "nome" : nome,
        "quantidade" : qtd,
        "preco" : preco
    }
    produtos.append(produto)


with st.form("Formulário"):
    st.write("Login")

    nome = st.text_input("Nome")
    qtd = st.text_input("Quantidade")
    preco = st.text_input("Preço")

    submit = st.form_submit_button("Enviar", on_click=add(nome, qtd, preco))

tabela = st.dataframe()