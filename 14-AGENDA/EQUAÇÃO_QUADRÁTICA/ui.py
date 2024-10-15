import streamlit as st
class UI:
    @staticmethod
    def menu():
        st.write("Digite 1 para inserir o valor de a")
        st.write("Digite 2 para inserir o valor de b")
        st.write("Digite 3 para inserir o valor de c")
        return st.number_input("Dígito: ")
    @staticmethod
    def main():
        op = 4
        while op != 0:
            op = UI.menu()
            if op == 1: UI.raizes_a()
            if op == 2: UI.raizes_b()
            if op == 3: UI.raizes_c()
        st.write()
    @staticmethod
    def raizes_a():
        st.number_input("Informe o valor de a: ")
    @staticmethod
    def raizes_b():
        st.number_input("Informe o valor de b: ")
    @staticmethod
    def raizes_c():
        st.number_input("Informe o valor de c: ")
    @staticmethod
    def grafico():
        xmin = 5
        xmax = 15
        n = 100
        d = (xmax - xmin)/n
        px = []
        py = []
        x = xmin
        while x < xmax:
            y = x**2 - 5*x + 6
            px.append(x)
            py.append(y)
            x = x + d
        # x = xmax
        # y = x**2 - 5*x + 6
        # px.append(x)
        # py.append(y)
        # dic = {"x" : px, "y" : py}
        # chart_data = pd.DataFrame(dic)
        # st.line_chart(chart_data, x = "x", y = "y")