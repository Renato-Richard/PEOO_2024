from views import View
import streamlit as st
class band_data_persistence_UI():
    def main():
        with st.form("bands"):
            st.title("Cadastrar bandas:")
            band_name = st.text_input("Nome da banda:")
            music_genre = st.text_input("Gênero musical:")
            description = st.text_input("Descrição da banda:")
            # formed_date = st.date_input("Data de formação:")
            members_count = st.number_input("Quantidade de membros:", min_value=1, step=1, format="%d")
            total_shows_by_band = st.number_input("Quantidade de apresentações:", min_value=0, step=1, format="%d")
            st.write("Este é um valor inicial, ele será atualizado automaticamente.")
            band_status = st.text_input("Estado atual da banda:")
            st.write("Aqui vem a última aualização")
            if st.form_submit_button("Cadastrar bandas"):
                View.create_band(band_name, music_genre, description, "", members_count, total_shows_by_band, band_status)