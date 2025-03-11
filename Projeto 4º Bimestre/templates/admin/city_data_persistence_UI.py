import streamlit as st
from datetime import datetime
from views import View
import time
class CityDataPersistenceUI():
    def main():
        with st.form("cities"):
            st.markdown("## Cadastrar cidades:")
            city_name = st.text_input("Cidade:")
            total_shows_by_city = st.number_input("Quantidade de apresentações:", step=1, format="%d")
            updated_at = datetime.now()
            if st.form_submit_button("Cadastrar cidade"):
                View.create_city(city_name, total_shows_by_city, updated_at)
                st.success(f"{city_name} foi cadastrada!")
                time.sleep(2)
                st.rerun()