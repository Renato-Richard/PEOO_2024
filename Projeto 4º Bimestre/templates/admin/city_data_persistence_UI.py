import streamlit as st
import pandas as pd
from datetime import datetime
from views import View
import time
class CityDataPersistenceUI():
    def main():
        st.markdown("## Cadastrar cidades:")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])
        with tab1: CityDataPersistenceUI.create()
        with tab2: CityDataPersistenceUI.read()
        with tab3: CityDataPersistenceUI.update()
        with tab4: CityDataPersistenceUI.delete()
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
    def update():
        cities = View.read_city()
        if len(cities) == 0: 
            st.info("Nenhuma cidade cadastrada")
        else:
            with st.form("update_city"):
                city_name = st.text_input("Informe o novo nome do cliente")
                total_shows_by_city = st.number_input("Quantidade de apresentações:", step=1, format="%d")
                updated_at = datetime.now()
                if st.form_submit_button("Atualizar"):
                    View.update_city(city_name, total_shows_by_city, updated_at)
                    st.success("Cliente atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
    def delete():
        pass