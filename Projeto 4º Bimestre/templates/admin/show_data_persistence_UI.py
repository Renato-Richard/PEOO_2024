import streamlit as st
from datetime import datetime
from views import View
import time
class ShowDataPersistenceUI():
    @staticmethod
    def main():
        with st.form("shows"):
            st.markdown("## Cadastrar shows:")
            description_of_show = st.text_input("Descrição do show:")
            show_date = st.date_input("Data:")
            show_time = st.time_input("Hora:")
            is_virtual = st.radio("Modalidade", ["Presencial", "Virtual"])
            is_virtual = is_virtual == "Virtual"
            available_tickets = st.number_input("Ingressos disponíveis:", min_value=0, step=1, format="%d")
            ticket_price = st.text_input("Valor do ingresso:", placeholder="R$00,00")
            sold_tickets = st.number_input("Ingressos vendidos:", step=1, format="%d")
            show_status = st.radio("Estado atual da show:", ["Ativo", "Cancelado", "Suspenso"])
            updated_at = datetime.now()
            if st.form_submit_button("Cadastrar show"):
                    View.create_show(description_of_show, show_date, show_time, is_virtual, available_tickets, ticket_price, sold_tickets, show_status, updated_at)
                    st.success("O show foi cadastrado!")
                    time.sleep(2)
                    st.rerun()