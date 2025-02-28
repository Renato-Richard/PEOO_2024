from templates.band_data_persistence_UI import band_data_persistence_UI
from templates.city_data_persistence_UI import city_data_persistence_UI
from templates.show_data_persistence_UI import show_data_persistence_UI
from templates.user_data_persistence_UI import user_data_persistence_UI

from templates.view_shows_UI import view_shows_UI
from templates.buy_ticket_UI import buy_ticket_UI
from templates.my_data_UI import my_data_UI
from templates.login_UI import Login_UI

import streamlit as st
class IndexUI:
    def login():
        Login_UI.main()

    def admin_menu():            
        opt = st.sidebar.selectbox("Menu", ["Cadastro de Bandas", "Cadastro de Cidades", "Cadastro de Shows", "Cadastro de Usuários"])
        if opt == "Cadastro de Bandas": band_data_persistence_UI.main()
        if opt == "Cadastro de Cidades": city_data_persistence_UI.main()
        if opt == "Cadastro de Shows": show_data_persistence_UI.main()
        if opt == "Cadastro de Usuários": user_data_persistence_UI.main()
    def user_menu():
        opt = st.sidebar.selectbox("Menu", ["Ver shows", "Meus Dados"])
        if opt == "Ver shows": view_shows_UI.main()
        if opt == "Comprar ingressos": buy_ticket_UI.main()
        if opt == "Meus Dados": my_data_UI.main()
    def main():
        IndexUI.login()
IndexUI.main()