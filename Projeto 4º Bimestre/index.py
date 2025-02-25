from templates.band_data_persistence import band_data_persistence
from templates.city_data_persistence import city_data_persistence
from templates.show_data_persistence import show_data_persistence
from templates.user_data_persistence import user_data_persistence

import streamlit as st
class IndexUI:
    def admin_menu():            
        opt = st.sidebar.selectbox("Menu", ["Cadastro de Bandas", "Cadastro de Cidades", "Cadastro de Shows", "Cadastro de Usuários"])
        if opt == "Cadastro de Bandas": band_data_persistence.main()
        if opt == "Cadastro de Cidades": city_data_persistence.main()
        if opt == "Cadastro de Shows": show_data_persistence.main()
        if opt == "Cadastro de Usuários": user_data_persistence.main()
    # def user_menu():
    #     opt = st.sidebar.selectbox("Menu", ["Horários Disponíveis", "Meus Dados"])
    #     if opt == "Horários Disponíveis": ListarHorarioUI.main()
    #     if opt == "Meus Dados": MeusDadosUI.main()
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()
    def sidebar():
        if "cliente_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["cliente_nome"] == "admin"
            # mensagen de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            # menu do usuário
            if st.session_state["tipo"] == "cliente":
                if admin: IndexUI.menu_admin()
                else: IndexUI.menu_cliente()
            else:
                IndexUI.menu_profissional()    
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 
    
    # def main():
    #     # verifica a existe o usuário admin
    #     View.cliente_admin()
    #     # monta o sidebar
    #     IndexUI.sidebar()
IndexUI.main()