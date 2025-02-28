from views import View
import time
import streamlit as st
class Create_account_UI():
    def main():
        st.header("Criar conta")
        Create_account_UI.create()
    def create():
        name = st.text_input("Nome:")
        email = st.text_input("E-mail:")
        password = st.text_input("Senha:", type="password")
        birth_date = st.date_input("Data de nascimento:")
        if st.button("Criar"):
            View.create_user(name, email, password, birth_date)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()