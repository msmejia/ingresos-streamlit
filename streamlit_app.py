import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Datos
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
ingresos = [12000, 15000, 13000, 14000, 12500, 17000,
            16000, 18000, 15500, 19000, 20000, 21000]

df = pd.DataFrame({'Mes': meses, 'Monto': ingresos})

# Configurar la página
st.set_page_config(page_title="Ingresos Mensuales", layout="wide")
st.title("📊 Visualización de Ingresos Mensuales")

# Mostrar la tabla
st.subheader("📋 Tabla de Ingresos")
st.dataframe(df, use_container_width=True)

# Tabs con gráficos
tab1, tab2 = st.tabs(["📈 Gráfico de Líneas", "📦 Diagrama de Caja"])

with tab1:
    st.subheader("Ingresos por Mes")
    fig1, ax1 = plt.subplots()
    sns.lineplot(x='Mes', y='Monto', data=df, marker='o', ax=ax1, color="blue")
    ax1.set_title("Ingresos Mensuales")
    ax1.set_ylabel("Monto ($)")
    st.pyplot(fig1)

with tab2:
    st.subheader("Variabilidad de los Ingresos")
    fig2, ax2 = plt.subplots()
    sns.boxplot(y='Monto', data=df, ax=ax2, color="skyblue")
    ax2.set_title("Distribución de Ingresos")
    ax2.set_ylabel("Monto ($)")
    st.pyplot(fig2)
