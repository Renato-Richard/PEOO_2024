import streamlit as st
from views import View
class ExploreBandsUI():
    def main():
        st.markdown("## Explore as suas bandas favoritas na Agenda Musical")
        st.markdown("<p style='font-size: 1.25em; margin: 1em 0 4em 0;'>Visualize os próximos shows e adquira logo os ingressos, antes que acabem!</p>", unsafe_allow_html=True)
        for c in View.read_band():
            st.write(c)