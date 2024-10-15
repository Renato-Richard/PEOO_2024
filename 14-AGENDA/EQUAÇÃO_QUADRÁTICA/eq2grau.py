import streamlit as st
import math
# import pandas as pd

class EquacaoQuadratica:
    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c
    def delta(self):
        delta = self.b ** 2 - 4 * self.a * self.c
    def raiz1(self):
        if EquacaoQuadratica.delta() > 0:
            x1 = -self.b + math.sqrt(EquacaoQuadratica.delta()) / 2 * self.a
        return x1
    def raiz2(self):
        if EquacaoQuadratica.delta() > 0:
            x2 = -self.__b - math.sqrt(EquacaoQuadratica.delta()) / 2 * self.__a
        return x2
    def __str__(self):
        return f"a = {self.__a} - b = {self.__b} - c = {self.__c}"


#delta = 5*5 - 4*1*6 = 1








        # xmin = 5
        # xmax = 15
        # n = 100
        # d = (xmax - xmin)/n
        # px = []
        # py = []
        # x = xmin
        # while x < xmax:
        #     y = x**2 - 5*x + 6
        #     px.append(x)
        #     py.append(y)
        #     x = x + d
        # x = xmax
        # y = x**2 - 5*x + 6
        # px.append(x)
        # py.append(y)
        # dic = { "x" : px, "y" : py }
        # chart_data = pd.DataFrame(dic)
        # st.line_chart(chart_data, x = "x", y = "y")