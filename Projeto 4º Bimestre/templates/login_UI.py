import streamlit as st
from views import View
import time
class LoginUI():
    def main():
        st.write("DEBUG: LoginUI.main() foi chamado")
        st.header("Entrar:")
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            a = View.authenticate_admin(email, password)
            if a != None:
                st.session_state["id"] = a["id"]
                st.session_state["user_name"] = a["user_name"]
                st.session_state["type"] = "admin"
                st.session_state["page"] = "admin_menu"
                st.success(f"Bem-vindo, Administrador {a['user_name']}!")
                st.rerun()
            u = View.authenticate_user(email, password)
            if u == None and a == None: 
                st.write("E-mail ou senha inválidos")
            elif u != None:    
                st.session_state["id"] = u["id"]
                st.session_state["user_name"] = u["user_name"]
                st.session_state["type"] = "user"
                st.session_state["page"] = "user_menu"
                st.write(f"DEBUG: Redirecionando para {st.session_state['page']}")
                st.success(f"Bem-vindo, {u['user_name']}!")
                st.rerun()