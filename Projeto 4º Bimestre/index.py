import streamlit as st
import time
from views import View
from templates.create_account_UI import CreateAccountUI
from templates.login_UI import LoginUI
from templates.settings_UI import SettingsUI
from templates.admin.band_data_persistence_UI import BandDataPersistenceUI
from templates.admin.city_data_persistence_UI import CityDataPersistenceUI
from templates.admin.show_data_persistence_UI import ShowDataPersistenceUI
from templates.user.explore_bands_UI import ExploreBandsUI
from templates.user.explore_cities_UI import ExploreCitiesUI
from templates.user.my_tickets_UI import MyTickets
class IndexUI():
    def main():
        IndexUI.page_style()
        if "page" in st.session_state:
            if st.session_state["page"] == "user_menu": IndexUI.user_menu()
            elif st.session_state["page"] == "admin_menu": IndexUI.admin_menu()
        else: IndexUI.visitor_menu()
    def sidebar():
        if "id" not in st.session_state:
            IndexUI.visitor_menu()   
        else:
            admin = st.session_state["type"] == "admin"
            st.sidebar.write(f"Bem-vindo(a), {st.session_state['user_name']}")
            if st.session_state["type"] == "user":
                IndexUI.user_menu() 
            elif admin:
                IndexUI.admin_menu()
            IndexUI.sair_do_sistema()
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            st.session_state.clear()
            st.rerun()
    def page_style():
        st.sidebar.markdown("# Agenda Musical")
        st.markdown("<style>.e1c29vlm8{background-color: #f20c8b; color: white;} .e1d5ycv52:hover{border: 1px solid #f20c8b; color: #f20c8b;}</style>", unsafe_allow_html=True)
    def visitor_menu():
        opt = st.sidebar.selectbox("", ["Criar conta", "Fazer login"], key="login")
        if opt == "Criar conta": CreateAccountUI.main()
        if opt == "Fazer login": LoginUI.main()
    def user_menu():
        opt = st.sidebar.selectbox("", ["Explorar Bandas", "Explorar cidades", "Meus Ingressos", "Configurações"], key="user_menu")
        if opt == "Explorar Bandas": ExploreBandsUI.main()
        if opt == "Explorar cidades": ExploreCitiesUI.main()
        if opt == "Meus Ingressos": MyTickets.main()
        if opt == "Configurações": SettingsUI.main()
        st.write(f"Página atual: {st.session_state.get('page')}")
    def admin_menu():          
        opt = st.sidebar.selectbox("Painel do administrador:", ["Cadastro de Bandas", "Cadastro de Cidades", "Cadastro de Shows"], key="admin_menu")
        if opt == "Cadastro de Bandas": BandDataPersistenceUI.main()
        if opt == "Cadastro de Cidades": CityDataPersistenceUI.main()
        if opt == "Cadastro de Shows": ShowDataPersistenceUI.main()
IndexUI.main()