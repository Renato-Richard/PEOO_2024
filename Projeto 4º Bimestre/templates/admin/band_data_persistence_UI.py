import streamlit as st
from datetime import datetime
from views import View
import pandas as pd
import time
from models.band import Band, Bands
class BandDataPersistenceUI():
    @staticmethod
    def main():
        BandDataPersistenceUI.search()
        st.markdown("## Cadastrar bandas:")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])
        with tab1: BandDataPersistenceUI.create()
        with tab2: BandDataPersistenceUI.read()
        with tab3: BandDataPersistenceUI.update()
        with tab4: BandDataPersistenceUI.delete()
    @staticmethod
    def create():
        with st.form("create_band"):
            band_name = st.text_input("Nome da banda:")
            music_genre = st.text_input("Gênero musical:")
            description = st.text_area("Descrição da banda")
            formed_date = st.date_input("Data de formação:")
            members_count = st.number_input("Quantidade de membros:", min_value=1, step=1, format="%d")
            total_shows_by_band = st.number_input("Quantidade de apresentações:", min_value=0, step=1, format="%d")
            st.info("O valor que você inserir em quantidade de apresentações, será um valor inicial. Este valor será somado as apresentações seguintes, portanto, ele será atualizado automaticamente.")
            band_status = st.radio("Estado atual da banda:", ["Ativa", "Inativa", "Suspensa"])
            updated_at = datetime.now()
            if st.form_submit_button("Cadastrar banda"):
                View.create_band(band_name, music_genre, description, formed_date, members_count, total_shows_by_band, band_status, updated_at)
                st.success(f"{band_name} foi cadastrada!")
                time.sleep(2)
                st.rerun()
    @staticmethod
    def read():
        bands = View.read_band()
        if len(bands) == 0: 
            st.info("Nenhuma banda cadastrada")
        else:  
            attribute_map = {
            'id': 'ID da Cidade',
            '_Band__band_name': 'Nome da Cidade',
            '_Band__music_genre': 'Gênero da banda',
            '_Band__description': 'Descrição da banda',
            '_Band__formed_date': 'Data de formação',
            '_Band__members_count': 'Quantidade de membros',
            '_Band__total_shows_by_band': 'Quantidade de shows',
            '_Band__band_status': 'Estado atual da banda',
            '_Band__updated_at': 'Última Atualização',
            }
            dic = []
            for obj in bands:
                band_dict = obj.__dict__
                renamed_dict = {attribute_map.get(key, key): value for key, value in band_dict.items()}
                dic.append(renamed_dict)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    @staticmethod
    def update():
        bands = View.read_band()
        if len(bands) == 0: 
            st.info("Nenhuma banda cadastrada")
        else:
            with st.form("update_band"):
                opt = st.selectbox("Atualização de cidade", bands)
                band_name = st.text_input("Nome da banda")
                music_genre = st.text_input("Gênero musical:")
                description = st.text_area("Descrição da banda")
                formed_date = st.date_input("Data de formação:")
                members_count = st.number_input("Quantidade de membros:", min_value=1, step=1, format="%d")
                total_shows_by_band = st.number_input("Quantidade de apresentações:", step=1, format="%d")
                updated_at = datetime.now()
                if st.form_submit_button("Atualizar"):
                    View.update_band(opt.id, band_name, music_genre, description, formed_date, members_count, total_shows_by_band, updated_at)
                    st.success("Banda atualizada com sucesso")
                    time.sleep(2)
                    st.rerun()
    @staticmethod
    def delete():
        bands = View.read_band()
        if len(bands) == 0: 
            st.info("Nenhuma banda cadastrada")
        else:
            with st.form("delete_band"):
                op = st.selectbox("Exclusão de banda", bands)
                if st.form_submit_button("Excluir"):
                    View.delete_band(op.id)
                    st.success("Banda excluída com sucesso")
                    time.sleep(2)
                    st.rerun()
    @staticmethod
    def search():
        st.markdown("## Pesquisa de Shows por Banda:")
        band_name = st.text_input("Digite o nome da banda:")
        if band_name:
            results = View.search_shows_by_band(band_name)
            if results:
                st.write(f"Shows encontrados para a banda '{band_name}':")
                for show in results:
                    st.write(f"ID: {show.id}, Banda: {show._Band__band_name}")
            else:
                st.write(f"Nenhum show encontrado para a banda '{band_name}'.")
    if __name__ == "__main__":
        main()