import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título y descripción del Portfolio

def intro():
    st.title("Iván Alonso - Data Analyst Portfolio")


    with st.container():
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
        ¡Bienvenido a mi portfolio de analista de datos! Soy un analista de datos apasionado y comprometido con un sólido conocimiento en el análisis y visualización de datos. 
                                A lo largo de mi carrera, he desarrollado y perfeccionado habilidades en diversas herramientas y técnicas que me permiten transformar datos complejos 
                                en información valiosa y comprensible.
        """)
        with col2:
            st.image("https://avatars.githubusercontent.com/u/160544813?v=4", width=200)

    
    st.markdown("""
    <div style="text-align: justify;">

    **Herramientas y Técnicas que utilizo**

    * **Lenguaje de programación principal**: Utilizo `Python` como mi lenguaje principal de programación debido a su versatilidad y potencia.
    * **Manipulación y análisis de datos**: Con bibliotecas como `pandas`, puedo realizar manipulación y análisis de datos de manera eficiente.
    * **Visualización de datos**:  `Matplotlib` y `seaborn` me resultan muy para la visualización de datos, permitiéndome crear gráficos claros y persuasivos que comunican las historias detrás de los datos.
    * **Machine Learning**: Tengo nociones de Machine y Deep Learning, las cuales he podido poner a prueba con técnicas como Random Forest, Bagging y Prophet he podido desarrollar modelos predictivos robustos. 

    *Mi objetivo es siempre encontrar patrones ocultos y proporcionar insights que impulsen la toma de decisiones estratégicas.*

    </div>
    """, unsafe_allow_html=True)

    st.markdown("En este portfolio, presento algunos de los proyectos que he realizado, destacando mi capacidad para abordar problemas complejos y proporcionar soluciones basadas en datos.")
    st.write("Si estás interesado en colaborar en proyectos relacionados con el análisis de datos, machine learning o cualquier otro ámbito de la ciencia de datos, no dudes en contactarme.  Estoy siempre en busca de nuevas oportunidades para aplicar mis habilidades y aprender algo nuevo.")
    st.write("**Gracias por visitar mi portfolio**, espero que disfrutes explorando mis proyectos tanto como yo disfruté trabajándolos.")


def proyecto_crimenML():

    st.subheader("Proyectos")
    
    st.markdown("""
    ### Predicción de Ventas
    He desarrollado modelos de Deep Learning para predecir ventas futuras utilizando técnicas como Random Forest, XGBoost y Prophet. 
    Aquí puedes ver algunos de mis resultados:
    
    ### Análisis de Criminalidad en España
    Un análisis detallado de cómo la criminalidad ha evolucionado en España a lo largo de los años, utilizando Deep Learning para predecir tendencias futuras.
    - [Repositorio en GitHub](https://github.com/tuusuario/tu-repositorio)
    - [Aplicación de Streamlit](https://tu-streamlit-app.com)
    """)


# Selector de página
page = st.sidebar.selectbox("Selecciona una página", ["Introducción", "Proyecto Machine Learning", "Análisis de Datos", "Contacto"])
st.sidebar.markdown("<br>" * 23, unsafe_allow_html=True)
st.sidebar.markdown("""  
                ### Github - https://github.com/ivanalonsom  
                ### Linkedin - https://www.linkedin.com/in/ivanalonsom  
                """)
# Página de Introducción
if page == "Introducción":
    intro()

# Página de Proyectos
elif page == "Proyecto Machine Learning":
    proyecto_crimenML()

# Página de Análisis de Datos
elif page == "Análisis de Datos":
    st.subheader("Análisis de Datos")
    
    # Cargar datos
    @st.cache
    def load_data():
        df = pd.read_csv("https://raw.githubusercontent.com/data-bootcamp-v4/data/main/sales.csv")
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
        return df

    df = load_data()
    
    # Mostrar los datos
    st.subheader("Conjunto de Datos")
    st.dataframe(df.head())
    
    # Selección de tienda
    store_ids = df['Store_ID'].unique()
    selected_store = st.selectbox("Selecciona una tienda para analizar", store_ids)
    
    # Filtrar datos por tienda seleccionada
    df_store = df[df['Store_ID'] == selected_store]
    
    # Visualización de ventas
    st.subheader(f"Ventas de la Tienda {selected_store} a lo largo del tiempo")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df_store, x='Date', y='Sales', ax=ax)
    plt.title(f"Ventas de la Tienda {selected_store}")
    plt.xlabel("Fecha")
    plt.ylabel("Ventas")
    st.pyplot(fig)
    
    # Análisis de correlación
    st.subheader("Análisis de Correlación")
    correlation = df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
    plt.title("Mapa de Calor de Correlaciones")
    st.pyplot(fig)
    
    # Análisis de ventas por día de la semana
    st.subheader("Ventas por Día de la Semana")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=df_store, x='Day_of_week', y='Sales', ax=ax)
    plt.title(f"Ventas de la Tienda {selected_store} por Día de la Semana")
    plt.xlabel("Día de la Semana")
    plt.ylabel("Ventas")
    st.pyplot(fig)

# Página de Contacto
elif page == "Contacto":
    st.subheader("Contacto")
    st.markdown("""
    - **Nombre:** Tu Nombre
    - **Email:** tuemail@ejemplo.com
    - **LinkedIn:** [Tu Perfil](https://www.linkedin.com/in/tuperfil)
    """)


