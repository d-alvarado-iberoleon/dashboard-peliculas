import streamlit as st

def mostrar_estadisticas(df):
    st.subheader("Estadísticas generales")
    col1, col2, col3 = st.columns(3)
    col1.metric("🎥 Total de películas", len(df))
    col2.metric("💰 Ingreso promedio", f"${df['revenue'].mean():,.0f}")
    col3.metric("📈 ROI promedio", f"{df['roi'].mean():.2f}")
    st.markdown("---")

def mostrar_tabla(df):
    st.subheader("Detalles de películas filtradas")
    st.dataframe(df[['title', 'budget', 'revenue', 'roi', 'genero_principal']].reset_index(drop=True))
