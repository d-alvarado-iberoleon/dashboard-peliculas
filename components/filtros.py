# -*- coding: utf-8 -*-
import streamlit as st

def aplicar_filtros(df):
    st.sidebar.header("Filtros")
    anios = sorted(df['year'].dropna().unique())
    anio_default = max(0, len(anios)-2)
    anio = st.sidebar.selectbox("Selecciona un año", options=anios, index=anio_default)
    generos = sorted(df['genero_principal'].dropna().unique())
    generos_sel = st.sidebar.multiselect("Filtrar por género principal", 
                                         generos, 
                                         default=["Action", "Drama", "Comedy"])

    df_filtrado = df[df['year'] == anio]
    if generos_sel:
        df_filtrado = df_filtrado[df_filtrado['genero_principal'].isin(generos_sel)]
    return df_filtrado, anio, generos_sel
