# -*- coding: utf-8 -*-
import streamlit as st
from utils.cargar_datos import cargar_datos
from components.filtros import aplicar_filtros
from components.layout import mostrar_estadisticas, mostrar_tabla
from utils.graficas import grafica_dispersion, grafica_top_peliculas, grafica_area

st.set_page_config(page_title="Análisis de películas", 
                   layout="wide", 
                   page_icon="🎬")

st.sidebar.expander(" ", expanded=True)

st.title("🎬 Análisis interactivo de películas")

df = cargar_datos()
df_filtrado, anio, generos = aplicar_filtros(df)
mostrar_estadisticas(df_filtrado)

grafica_dispersion(df_filtrado, anio)
grafica_top_peliculas(df_filtrado, anio)
grafica_area(df, generos)
mostrar_tabla(df_filtrado)
