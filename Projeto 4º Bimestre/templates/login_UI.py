from views import View
import time
import streamlit as st 
from templates.user_UI import User_UI
class Login_UI():
    def main():
        st.header("Entrar:")
        if "page" not in st.session_state:
            st.session_state["page"] = "login"  # Página inicial é o login

        if st.session_state["page"] == "login":
            Login_UI.create()  # Exibe a página de login
        elif st.session_state["page"] == "user":
            User_UI.main()  # Exibe o menu do usuário
        elif st.session_state["page"] == "admin":
            User_UI.main()  # Exibe o menu do administrador
    def create():
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            u = View.authenticate_user(email, password)
            a = View.authenticate_admin(email, password)
            if u == None and a == None: 
                st.write("E-mail ou senha inválidos")
            elif u != None:    
                st.session_state["id"] = u["id"]
                st.session_state["user_name"] = u["user_name"]
                st.session_state["type"] = "user"
                st.session_state["page"] = "user"
                st.success("Bem-vindo")
            elif a != None:    
                st.session_state["id"] = a["id"]
                st.session_state["user_name"] = a["user_name"]
                st.session_state["type"] = "admin"
                st.session_state["page"] = "admin"
                st.success("Bem-vindo")
            st.rerun()