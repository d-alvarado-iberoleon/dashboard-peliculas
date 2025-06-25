import plotly.express as px
import streamlit as st

def grafica_dispersion(df_filtrado, anio):
    df_plot = df_filtrado[(df_filtrado["revenue"] > 0) & (df_filtrado["budget"] > 0)]
    if not df_plot.empty:
        fig = px.scatter(df_plot, 
                         x="budget", 
                         y="revenue", 
                         color="genero_principal",
                         hover_name="title", 
                         title=f"Presupuesto vs Ingresos en {anio}", 
                         labels={
                             "budget": "Presupuesto (USD)",
                             "revenue": "Ingresos (USD)"
                             })
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No hay datos suficientes para mostrar la gráfica de dispersión.")

def grafica_top_peliculas(df_filtrado, anio):
    df_filtrado['title_corta'] = df_filtrado['title'].apply(lambda x: x[:10] + "..." if len(x) > 30 else x)

    if not df_filtrado.empty:
        top_df = df_filtrado.sort_values("revenue", ascending=False).head(20)
        fig = px.bar(top_df, 
                     x="title_corta", 
                     y="revenue", 
                     color="genero_principal",
                     title=f"Top 20 películas por ingresos en {anio}", 
                     labels={
                         "revenue": "Ingresos (USD)", 
                         "title_corta": "Películas"
                         })
        #fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

def grafica_area(df, generos):
    tabla = df[(df['year'] >= 2000) & (df['genero_principal'].isin(generos))] \
               .groupby(['year', 'genero_principal'])['title'].count().reset_index()
    if not tabla.empty:
        fig = px.area(tabla, x='year', y='title', color='genero_principal',
                      title='Películas por género a lo largo del tiempo (2000 en adelante)',
                      labels={'title': 'Cantidad de películas', 
                              "year": "Año"})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No hay datos para mostrar la evolución por género.")
