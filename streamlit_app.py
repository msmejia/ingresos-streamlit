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

# CSS para centrar y ajustar tamaño
st.markdown(
    """
    <style>
    /* Centrar el contenedor de la tabla y poner ancho fijo */
    .css-1d391kg div[data-testid="stDataFrameContainer"] {
        margin-left: auto;
        margin-right: auto;
        max-width: 500px;
    }
    /* Centrar las figuras */
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.set_page_config(page_title="Ingresos Mensuales", layout="wide")
st.title("📊 Visualización de Ingresos Mensuales")

st.subheader("📋 Tabla de Ingresos")
# Mostrar tabla con contenedor centrado
st.dataframe(df, use_container_width=False, width=500)

tab1, tab2 = st.tabs(["📈 Gráfico de Líneas", "📦 Diagrama de Caja"])

with tab1:
    st.subheader("Ingresos por Mes")
    fig1, ax1 = plt.subplots(figsize=(6, 3))  # figura más pequeña
    sns.lineplot(x='Mes', y='Monto', data=df, marker='o', ax=ax1, color="blue")
    ax1.set_title("Ingresos Mensuales")
    ax1.set_ylabel("Monto ($)")
    ax1.grid(True)
    st.markdown('<div class="center">', unsafe_allow_html=True)
    st.pyplot(fig1)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.subheader("Variabilidad de los Ingresos")
    fig2, ax2 = plt.subplots(figsize=(4, 4))  # figura más pequeña y cuadrada
    sns.boxplot(y='Monto', data=df, ax=ax2, color="skyblue")
    ax2.set_title("Distribución de Ingresos")
    ax2.set_ylabel("Monto ($)")
    st.markdown('<div class="center">', unsafe_allow_html=True)
    st.pyplot(fig2)
    st.markdown('</div>', unsafe_allow_html=True)
