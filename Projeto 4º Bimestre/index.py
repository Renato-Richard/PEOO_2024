from templates.band_data_persistence_UI import band_data_persistence_UI
from templates.city_data_persistence_UI import city_data_persistence_UI
from templates.show_data_persistence_UI import show_data_persistence_UI
from templates.user_data_persistence_UI import user_data_persistence_UI

from templates.view_shows_UI import view_shows_UI
from templates.buy_ticket_UI import buy_ticket_UI
from templates.my_data_UI import my_data_UI
from templates.create_account_UI import Create_account_UI
from templates.login_UI import Login_UI
from views import View
import time
import streamlit as st
class IndexUI():
    def admin_menu():
        st.header("alguma coisa")            
        opt = st.sidebar.selectbox("Menu", ["Cadastro de Bandas", "Cadastro de Cidades", "Cadastro de Shows", "Cadastro de Usuários"])
        if opt == "Cadastro de Bandas": band_data_persistence_UI.main()
        if opt == "Cadastro de Cidades": city_data_persistence_UI.main()
        if opt == "Cadastro de Shows": show_data_persistence_UI.main()
        if opt == "Cadastro de Usuários": user_data_persistence_UI.main()
    def visitor_menu():
        opt = st.sidebar.selectbox("Entrar", ["Criar conta", "Fazer login"])
        if opt == "Criar conta": Create_account_UI.main()
        if opt == "Fazer login": Login_UI.main()
        st.rerun()
    def main():
       if "type" in st.session_state:
        if st.session_state["type"] == "admin":
            IndexUI.admin_menu()
        elif st.session_state["type"] == "user":
            IndexUI.user_menu()
    def create_account():
        st.header("Criar conta")
        name = st.text_input("Nome:")
        email = st.text_input("E-mail:")
        password = st.text_input("Senha:", type="password")
        birth_date = st.date_input("Data de nascimento:")
        if st.button("Criar"):
            View.create_user(name, email, password, birth_date)
            st.success("Conta criada com sucesso")
            time.sleep(2)
IndexUI.visitor_menu()