import streamlit as st
from datetime import datetime
from views import View
class BandDataPersistenceUI():
    def main():
        with st.form("bands"):
            st.markdown("## Cadastrar bandas:")
            band_name = st.text_input("Nome da banda:")
            music_genre = st.text_input("Gênero musical:")
            description = st.text_input("Descrição da banda:")
            formed_date = st.date_input("Data de formação:")
            members_count = st.number_input("Quantidade de membros:", min_value=1, step=1, format="%d")
            total_shows_by_band = st.number_input("Quantidade de apresentações:", min_value=0, step=1, format="%d")
            st.info("O valor que você inserir em quantidade de apresentações, será um valor inicial. Este valor será somado as apresentações seguintes, portanto, ele será atualizado automaticamente.")
            band_status = st.text_input("Estado atual da banda:")
            st.info("Ex.: Ativo, inativo, suspenso...")
            updated_at = datetime.now()
            if st.form_submit_button("Cadastrar banda"):
                View.create_band(band_name, music_genre, description, formed_date, members_count, total_shows_by_band, band_status, updated_at)