import streamlit as st
from views import View
from datetime import datetime
import time
class CreateAccountUI():
    def main():
        st.header("Criar conta")
        CreateAccountUI.create()
    def create():
        with st.form("create_user"):
            name = st.text_input("Nome:")
            email = st.text_input("E-mail:")
            password = st.text_input("Senha:", type="password")
            birth_date = st.date_input("Data de nascimento:")
            updated_at = datetime.now()
            if st.form_submit_button("Criar"):
                View.create_user(name, email, password, birth_date, updated_at)
                st.success("Conta criada com sucesso")
                time.sleep(2)
                st.rerun()