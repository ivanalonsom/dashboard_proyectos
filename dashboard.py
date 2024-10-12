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
    <div style="text-align: justify;">
        ¡Bienvenido a mi portfolio de analista de datos! Soy un analista de datos apasionado y comprometido con un sólido conocimiento en el análisis y visualización de datos. 
                                A lo largo de mi carrera, he desarrollado y perfeccionado habilidades en diversas herramientas y técnicas que me permiten transformar datos complejos 
                                en información valiosa y comprensible.
        </div>
    """, unsafe_allow_html=True)
        with col2:
            st.image("https://avatars.githubusercontent.com/u/160544813?v=4", width=200)

    
    st.markdown("""
    <div style="text-align: justify;">

    **Herramientas y Técnicas que utilizo**

    * **Lenguaje de programación principal**: Utilizo `Python` como mi lenguaje principal de programación debido a su versatilidad y potencia.
    * **Manipulación y análisis de datos**: Con bibliotecas como `pandas`, puedo realizar manipulación y análisis de datos de manera eficiente.
    * **Visualización de datos**:  `Matplotlib` y `seaborn` me resultan muy útiles para la visualización de datos, permitiéndome crear gráficos claros y persuasivos que comunican las historias detrás de los datos.
    * **Machine Learning**: Tengo nociones de Machine y Deep Learning, las cuales he podido poner a prueba con técnicas como Random Forest, Bagging y Prophet he podido desarrollar modelos predictivos robustos. 

    *Mi objetivo es siempre encontrar patrones ocultos y proporcionar insights que impulsen la toma de decisiones estratégicas.*

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style="text-align: justify;">
En este portfolio, presento algunos de los proyectos que he realizado, destacando mi capacidad para abordar problemas complejos y proporcionar soluciones basadas en datos </div>
    """, unsafe_allow_html=True) 
    st.write("
<div style="text-align: justify;">
Si estás interesado en colaborar en proyectos relacionados con el análisis de datos, machine learning o cualquier otro ámbito de la ciencia de datos, no dudes en contactarme.  Estoy siempre en busca de nuevas oportunidades para aplicar mis habilidades y aprender algo nuevo.
</div>
    """, unsafe_allow_html=True)

    st.write("**Gracias por visitar mi portfolio**, espero que disfrutes explorando mis proyectos tanto como yo disfruté trabajándo en ellos.
</div>
    """, unsafe_allow_html=True)


def proyecto_crimenML():

    st.header("¿Y si el COVID-19 no hubiera existido? Predicción de la criminalidad en España en los ultimos años utilizando Deep Learning")
    
    st.markdown("""    
    ### Análisis de Criminalidad en España""")
    
    st.image("data/imagen_proyecto_deep_learning_ironhack.png", width=500)

    st.markdown(""" 
    <p style="text-align: justify;">
    El objetivo de este proyecto partió de una idea: ¿Y si el COVID-19 no hubiera existido?. Todos sabemos que en 2020 la criminalidad bajó a minimos en gran parte del mundo debido 
    a la pandemia. Sin embargo, ¿que pasaría si entrenasemos un modelo de inteligencia artificial hasta 2019 y le hiciesemos predecir los resultados de 2020? Los resultados que obtuvimos
    fueron más que sorprendentes.  </br>
    A continuación están los links del repositorio y de la web creada a modo de presentación para el proyecto.</br>
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    - [Repositorio en GitHub](https://github.com/ivanalonsom/Project6_Predict_Criminality_Using_ML)  
    - [Aplicación de Streamlit](https://deep-learning-spain-crimen-study.streamlit.app/)""")

def proyecto_abtest():

    st.header("Realización de A-B Testing mediante Análisis Exploratorio de Datos ")

    st.markdown(""" 
    <p style="text-align: justify;">
    En este proyecto partiamos de una serie de datos obtenidos durante un experimento de A-B Testing. Este consistió en realizar una recogida de datos de usuarios de una 
    misma página web durante varios meses, con la única diferencia de que algunos usuarios veían la web original (de control) y otros la nueva web (test). </br>
    El objetivo del proyecto consistió en limpiar, analizar y mostrar las conclusiones a las que llegamos a partir de los datos obtenidos.  </br>
    Para este paso de mostrar los resultados nos valimos de PowerBi y Tableau. 
    A continuación están los links del repositorio y de Tableau, además de una demostración del PowerBI realizado.  
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    - [Repositorio en GitHub](https://github.com/ivanalonsom/Project_A-B_Testing_Based_On_EDA)  
    - [Aplicación de Tableau](https://public.tableau.com/app/profile/iv.n.alonso8801/viz/ABTesting_Project_Clients_Analysis/Clientinsights)""")

    st.video("https://www.youtube.com/watch?v=risEWolXBHs")


def proyecto_ventas_sql():

    st.header("Proyecto SQL")

    st.markdown(""" 
    <p style="text-align: justify;">
    En este proyecto se obtuvieron datos de videojuegos en diferentes tiendas de *claves* y de tiendas oficiales mediante el manejo de diversas APIs. </br>
    Los datos obtenidos, entre los que destaca el precio,se limpiaron y trataron para su posterior utilización almacenándolos en una base de datos SQL, ofreciendo así una ventaja doble: </br>
    <ol> 
        <li> Poder obtener y filtrar los precios más baratos de cada videojuego y donde adquirirlo en apenas dos clicks con el programa desarrollado en Python. </li>
        <li> Podemos analizar las tendencias de mercado que, gracias al almacenamiento en la base de datos que creé para la tarea, cada vez ofrezca más información. Podemos también filtrar con las querys que necesitemos. </li>
    </ol>
    </p>""", unsafe_allow_html=True)
    
    st.image("data/relational_sql_ironhack.png")

    st.markdown(""" A continuación estan los links del repositorio y de la web creada a modo de presentación para el proyecto.
    - [Repositorio en GitHub](https://github.com/ivanalonsom/Project4_DataAnalysis_Sales_SQL)  
    - [Demo de Streamlit](https://project4-sql-data-oriented-to-sales.streamlit.app/)""")


def contacto():
    st.subheader("Contacto")
    st.markdown("""
    - **Nombre:** Iván Alonso
    - **Email:** ivan7yt@gmail.com
    - **LinkedIn:** [Perfil Iván Alonso](https://www.linkedin.com/in/tuperfil)
    """)

# Selector de página
page = st.sidebar.selectbox("Selecciona una página", ["Introducción", "Proyecto Machine Learning", "Proyecto A-B Testing", "Proyecto SQL", "Contacto"])
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


elif page == "Proyecto A-B Testing":
    proyecto_abtest()
    
elif page == "Proyecto SQL":
    proyecto_ventas_sql()

elif page == "Contacto":
    contacto()


