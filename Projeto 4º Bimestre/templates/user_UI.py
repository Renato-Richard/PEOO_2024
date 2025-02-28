from templates.view_shows_UI import view_shows_UI
from templates.buy_ticket_UI import buy_ticket_UI
from templates.my_data_UI import my_data_UI
import streamlit as st
class User_UI():
    def main():
        User_UI.user_menu()
    def user_menu():
        opt = st.sidebar.selectbox("Menu", ["Ver shows", "Meus Dados"])
        if opt == "Ver shows": view_shows_UI.main()
        if opt == "Comprar ingressos": buy_ticket_UI.main()
        if opt == "Meus Dados": my_data_UI.main()