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
        users = View.read_user()
        shows = View.read_show()
        with st.form("create_ticket"):
            user = st.selectbox("De qual usuário?", users, index = None)
            show = st.selectbox("De qual show?", shows, index = None)
            ticket_price = st.text_input("Preço do ingresso")
            updated_at = datetime.now()
            if st.form_submit_button("Cadastrar ingresso"):
                user_id = None
                show_id = None
                if user != None: user_id = user.id
                if show != None: show_id = show.id
                View.create_ticket(user_id, show_id, ticket_price, updated_at)
                st.success("O show foi cadastrado!")
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
                users = View.read_user()
                shows = View.read_show()
                opt = st.selectbox("Escolha o show", shows)
                opt = st.selectbox("Escolha o show", shows)
                band_id = None if opt._Show__band_id in [0, None] else opt._Show__band_id
                city_id = None if opt._Show__city_id in [0, None] else opt._Show__city_id
                band = st.selectbox("Escolha a banda", bands, next((i for i, c in enumerate(bands) if c.id == band_id), None))
                city = st.selectbox("Escolha a cidade", cities, next((i for i, s in enumerate(cities) if s.id == city_id), None))
                description_of_show = st.text_input("Descrição do show:")
                show_date = st.date_input("Data:")
                show_time = st.time_input("Hora:")
                is_virtual = st.radio("Modalidade", ["Presencial", "Virtual"])
                is_virtual = is_virtual == "Virtual"
                available_tickets = st.number_input("Ingressos disponíveis:", min_value=0, step=1, format="%d")
                ticket_price = st.text_input("Valor do ingresso:", placeholder="R$00,00")
                sold_tickets = st.number_input("Ingressos vendidos:", step=1, format="%d")
                show_status = st.radio("Estado atual do show:", ["Ativo", "Cancelado", "Suspenso"])
                updated_at = datetime.now()
                if st.form_submit_button("Atualizar"):
                    band_id = None
                    city_id = None
                    if band != None: band_id = band.id
                    if city != None: city_id = city.id
                    View.update_show(opt.id, band_id, city_id, description_of_show, show_date, show_time, is_virtual, available_tickets, ticket_price, sold_tickets, show_status, updated_at)
                    st.success("Show atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
    @staticmethod
    def delete():
        shows = View.read_show()
        if len(shows) == 0: 
            st.info("Nenhum show cadastrada")
        else:
            with st.form("delete_show"):
                opt = st.selectbox("Exclusão de banda", shows)
                if st.form_submit_button("Excluir"):
                    View.delete_show(opt.id)
                    st.success("Show excluído com sucesso")
                    time.sleep(2)
                    st.rerun()