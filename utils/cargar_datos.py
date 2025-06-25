# -*- coding: utf-8 -*-
import pandas as pd

def cargar_datos():
    df = pd.read_csv("data/movies_clean.csv")
    if "genero_principal" not in df.columns:
        df["genero_principal"] = df["lista_generos"].dropna().apply(lambda x: eval(x)[0] if eval(x) else None)
    return df
