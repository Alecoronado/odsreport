import streamlit as st
import pandas as pd
import plotly.express as px
from openpyxl import load_workbook

# Título de la aplicación
st.title('Visualización de Inversiones en ODS')

# Cargar archivo
uploaded_file = st.file_uploader("Sube tu archivo de Excel aquí", type=["xlsx"])

if uploaded_file is not None:
    # Si el archivo está cargado, leerlo con pandas
    # Si necesitas usar openpyxl porque tu archivo tiene múltiples hojas o necesidades especiales, puedes adaptar esta parte.
    df = pd.read_excel(uploaded_file)

    # Procesar los datos (ejemplo simple: sumar los aportes de FONPLATA por ODS)
    ods_totals = df.groupby('Nombre ODS')['AporteFONPLATA'].sum().reset_index()

    # Crear el gráfico
    fig = px.scatter(ods_totals, x='Nombre ODS', y='AporteFONPLATA',
                     size='AporteFONPLATA', color='Nombre ODS',
                     hover_name='Nombre ODS', size_max=60)
    
    # Mostrar el gráfico en la aplicación de Streamlit
    st.plotly_chart(fig)

