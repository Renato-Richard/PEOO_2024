import streamlit as st
import pandas as pd
from datetime import datetime
from views import View
import time
class CityDataPersistenceUI():
    @staticmethod
    def main():
        st.markdown("## Cadastrar cidades:")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])
        with tab1: CityDataPersistenceUI.create()
        with tab2: CityDataPersistenceUI.read()
        with tab3: CityDataPersistenceUI.update()
        with tab4: CityDataPersistenceUI.delete()
    @staticmethod
    def create():
        with st.form("create_city"):
            city_name = st.text_input("Cidade:")
            total_shows_by_city = st.number_input("Quantidade de apresentações:", step=1, format="%d")
            updated_at = datetime.now()
            if st.form_submit_button("Cadastrar cidade"):
                View.create_city(city_name, total_shows_by_city, updated_at)
                st.success(f"{city_name} foi cadastrada!")
                time.sleep(2)
                st.rerun()
    @staticmethod
    def read():
        cities = View.read_city()
        if len(cities) == 0: 
            st.info("Nenhuma cidade cadastrada")
        else:  
            attribute_map = {
            'id': 'ID da Cidade',
            '_City__city_name': 'Nome da Cidade',
            '_City__total_shows_by_city': 'Total de Apresentações',
            '_City__updated_at': 'Última Atualização'
            }
            dic = []
            for obj in cities:
                city_dict = obj.__dict__
                renamed_dict = {attribute_map.get(key, key): value for key, value in city_dict.items()}
                dic.append(renamed_dict)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    @staticmethod
    def update():
        cities = View.read_city()
        if len(cities) == 0: 
            st.info("Nenhuma cidade cadastrada")
        else:
            with st.form("update_city"):
                opt = st.selectbox("Atualização de cidade", cities)
                city_name = st.text_input("Nome da cidade")
                total_shows_by_city = st.number_input("Quantidade de apresentações:", step=1, format="%d")
                updated_at = datetime.now()
                if st.form_submit_button("Atualizar"):
                    View.update_city(opt.id, city_name, total_shows_by_city, updated_at)
                    st.success("Cidade atualizada com sucesso")
                    time.sleep(2)
                    st.rerun()
    @staticmethod
    def delete():
        cities = View.read_city()
        if len(cities) == 0: 
            st.info("Nenhuma cidade cadastrada")
        else:
            with st.form("delete_city"):
                op = st.selectbox("Exclusão de cidade", cities)
                if st.form_submit_button("Excluir"):
                    View.delete_city(op.id)
                    st.success("Cidade excluída com sucesso")
                    time.sleep(2)
                    st.rerun()