import streamlit as st
from views import View
from datetime import datetime
import pandas as pd
import time
class TicketDataPersistenceUI():
    @staticmethod
    def main():
        st.markdown("## Cadastrar ingressos:")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])
        with tab1: TicketDataPersistenceUI.create()
        with tab2: TicketDataPersistenceUI.read()
        with tab3: TicketDataPersistenceUI.update()
        with tab4: TicketDataPersistenceUI.delete()
    @staticmethod
    def create():
        shows = View.read_show()
        with st.form("create_ticket"):
            show = st.selectbox("De qual show?", shows, index = None)
            ticket_price = st.text_input("Preço do ingresso")
            updated_at = datetime.now()
            if st.form_submit_button("Cadastrar ingresso"):
                show_id = None
                if show != None: show_id = show.id
                View.create_ticket(show_id, ticket_price, updated_at)
                st.success("O ingresso foi inserido!")
                time.sleep(2)
                st.rerun()
    @staticmethod
    def read():
        tickets = View.read_show()
        if len(tickets) == 0:
            st.info("Nenhum ingresso cadastrado")
        else:  
            attribute_map = {
            'id': 'ID do Ingresso',
            '_Ticket__user_id': "ID do usuário",
            '_Ticket__show_id': "ID do show",
            '_Show__ticket_price': 'Preço dos ingressos',
            '_Show__updated_at': 'Última Atualização',
            }
            dic = []
            for obj in tickets:
                ticket_dict = obj.__dict__
                renamed_dict = {attribute_map.get(key, key): value for key, value in ticket_dict.items()}
                dic.append(renamed_dict)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    @staticmethod
    def update():
        shows = View.read_show()
        if len(shows) == 0: 
            st.info("Nenhum show cadastrado")
        else:
            with st.form("update_show"):
                opt = st.selectbox("Escolha o show", shows, key="show_selectbox")
                show_id = opt.id if opt else None
                ticket_price = st.text_input("Preço do ingresso", placeholder="R$00,00")
                updated_at = datetime.now()
                if st.form_submit_button("Atualizar"):
                    if show_id and ticket_price:
                        View.update_ticket(opt.id, show_id, ticket_price, updated_at)
                        st.success("Ingresso atualizado com sucesso")
                        time.sleep(2)
                        st.rerun()
    @staticmethod
    def delete():
        tickets = View.read_show()
        if len(tickets) == 0: 
            st.info("Nenhum ingresso cadastrado")
        else:
            with st.form("delete_show"):
                opt = st.selectbox("Exclusão de banda", tickets)
                if st.form_submit_button("Excluir"):
                    View.delete_ticket(opt.id)
                    st.success("Show excluído com sucesso")
                    time.sleep(2)
                    st.rerun()