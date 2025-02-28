from views import View
import time
import streamlit as st 
class Login_UI():
    def main():
        st.header("Entrar:")
        Login_UI.create()
    def create():
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            u = View.authenticate_user(email, password)
            a = View.authenticate_admin(email, password)
            st.success("Bem-vindo")
            time.sleep(2)
            st.rerun()
            if u == None and a == None: 
                st.write("E-mail ou senha inválidos")
            if u != None:    
                st.session_state["id"] = u["id"]
                st.session_state["user_name"] = u["user_name"]
                st.session_state["type"] = "user"
                IndexUI.admin_menu()
            if a != None:    
                st.session_state["id"] = a["id"]
                st.session_state["user_name"] = a["user_name"]
                st.session_state["type"] = "admin"
            st.experimental_rerun()