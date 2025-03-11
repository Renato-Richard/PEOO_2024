import streamlit as st
from datetime import datetime
from views import View
import time
import pandas as pd
class ShowDataPersistenceUI():
    @staticmethod
    def main():
        st.markdown("## Cadastrar shows:")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])
        with tab1: ShowDataPersistenceUI.create()
        with tab2: ShowDataPersistenceUI.read()
        with tab3: ShowDataPersistenceUI.update()
        with tab4: ShowDataPersistenceUI.delete()
    @staticmethod
    def create():
        bands = View.read_band()
        cities = View.read_city()
        with st.form("create_show"):
            band = st.selectbox("De qual banda?", bands, index = None)
            city = st.selectbox("Em qual cidade?", cities, index = None)
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
                band_id = None
                city_id = None
                if band != None: band_id = band.id
                if city != None: city_id = city.id
                View.create_show(band_id, city_id, description_of_show, show_date, show_time, is_virtual, available_tickets, ticket_price, sold_tickets, show_status, updated_at)
                st.success("O show foi cadastrado!")
                time.sleep(2)
                st.rerun()
    @staticmethod
    def read():
        shows = View.read_show()
        if len(shows) == 0:
            st.info("Nenhum show cadastrada")
        else:  
            attribute_map = {
            'id': 'ID do Show',
            '_Show__band_id': "ID da banda",
            '_Show__city_id': "ID da cidade",
            '_Show__description_of_show': 'Descrição do show',
            '_Show__show_date': 'Data',
            '_Show__show_time': 'Hora',
            '_Show__formed_date': 'Data de formação',
            '_Show__is_virtual': 'Modalidade',
            '_Show__available_tickets': 'Ingressos disponíveis',
            '_Show__ticket_price': 'Preço dos ingressos',
            '_Show__sold_tickets': 'Ingressos vendidos',
            '_Show__show_status': 'Estado atual do show',
            '_Show__updated_at': 'Última Atualização',
            }
            dic = []
            for obj in shows:
                show_dict = obj.__dict__
                renamed_dict = {attribute_map.get(key, key): value for key, value in show_dict.items()}
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
                bands = View.read_band()
                cities = View.read_city()
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