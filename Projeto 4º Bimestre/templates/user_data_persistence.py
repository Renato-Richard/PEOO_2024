import streamlit as st
class user_data_persistence():
    def main():
        st.title("Cadastrar bandas: ")
        st.text_input("Nome da banda:")
        st.text_input("Gênero musical:")
        st.text_input("Descrição da banda:")
        st.date_input("Data de formação:")
        st.number_input("Quantidade de membros:", min_value=1, step=1, format="%d")
        st.number_input("Quantidade de apresentações:", min_value=0, step=1, format="%d")
        st.write("Este é um valor inicial, ele será atualizado automaticamente.")
        st.text_input("Estado atual da banda:")
        st.write("Aqui vem a última aualização")