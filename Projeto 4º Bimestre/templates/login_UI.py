from views import View
from templates.create_account_UI import Create_account_UI
import streamlit as st 
class Login_UI():
    def main():
        Create_account_UI.main()
        st.header("Entrar:")
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            u = View.authenticate_user(email, password)
            a = View.authenticate_admin(email, password)
            if u == None and a == None: 
                st.write("E-mail ou senha inválidos")
                Create_account_UI.main()
            if u != None:    
                st.session_state["cliente_id"] = u["id"]
                st.session_state["cliente_nome"] = u["nome"]
                st.session_state["tipo"] = "cliente"
                st.rerun()
            if a != None:    
                st.session_state["cliente_id"] = u["id"]
                st.session_state["cliente_nome"] = u["nome"]
                st.session_state["tipo"] = "profissional"
                st.rerun()                