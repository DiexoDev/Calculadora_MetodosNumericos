from graficas.utils_graficos import crear_grafico
from metodos.metodosNumericos import (
    regla_simpson_abierta,
    regla_simpson13,
    regla_simpson38,
    regla_boole,
    regla_trapezoidal,
)
from utils.utils_matematicos import obtener_funcion
from streamlit import sidebar
import streamlit as st
import pandas as pd
import numpy as np

# Configuracion de la pagina
st.set_page_config(
    page_title="Métodos Numéricos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilos de la pagina.
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
    
    <style>
    /* Global Styles */
    .stApp {
        background: radial-gradient(circle at top right, #1e293b, #0f172a);
        font-family: 'Outfit', sans-serif;
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu, footer {visibility: hidden}
    .stDeployButton {display: none !important}
    header {background: transparent !important}
    
    /* Barra lateral */
    [data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.95);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Contenedores */
    div.stMetric {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        padding: 20px !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease;
    }
    div.stMetric:hover {
        transform: translateY(-5px);
        border-color: #6366f1;
        background: rgba(99, 102, 241, 0.05);
    }
    
    /* Tabs Personalizados */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 12px 12px 0 0;
        gap: 1px;
        padding: 10px 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #94a3b8;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(99, 102, 241, 0.2) !important;
        border-bottom: 3px solid #6366f1 !important;
        color: white !important;
    }
    
    /* Botones */
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border-radius: 12px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.4);
        border-color: transparent;
    }
    
    /* Inputs */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
    }
    
    /* Estilo del simbolo de integral */
    .integral-symbol {
        background: linear-gradient(135deg, #6366f1, #00d1b2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
""",unsafe_allow_html=True)

# Barra lateral
with sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 1rem 0;'>
            <img src='https://img.icons8.com/parakeet/96/math.png' width='80'>
            <h2 style='margin-top: 10px; font-weight: 700; color: white;'>Calculadora Científica</h2>
            <p style='color: #94a3b8; font-size: 0.9rem;'>Configuración del Cálculo</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("1. Métodos numéricos")

    # Opciones de la barra lateral
    opcion = st.selectbox(
        "Seleccione un método",
        [
            "Trapezoidal",
            "Jorge Boole",
            "T.Simpson 3/8",
            "T.Simpson 1/3",
            "Simpson abierto",
        ],
    )

    st.divider()

    st.subheader("2. Función y Límites")

    # Inicializar estado para la función si no existe
    if "funcion_input_val" not in st.session_state:
        st.session_state.funcion_input_val = "log(x)"

    # Funciones de callback para actualizar el estado antes del rerender (Forma recomendada)
    def agregar_valor(valor):
        if valor == "CLEAR":
            st.session_state.funcion_input_val = ""
        else:
            st.session_state.funcion_input_val += valor

    # Contenedor para Integral + Input + Teclado con estilo
    c1_side, c2_side = st.columns([1, 4])
    with c1_side:
        st.markdown("<h1 class='integral-symbol' style='font-size: 60px; margin-top: 5px;'>∫</h1>", unsafe_allow_html=True)
    with c2_side:
        # El widget está directamente ligado a st.session_state["funcion_input_val"]
        st.text_input("Función f(x)", key="funcion_input_val")
        
        with st.popover("🔢 Teclado Matemático", use_container_width=True):
            t1, t2 = st.tabs(["🔢 Números", "📈 Funciones"])
            with t1:
                kcols = st.columns(4)
                num_map = [
                    ('7','7'),('8','8'),('9','9'),(' / ','/'),
                    ('4','4'),('5','5'),('6','6'),(' * ','*'),
                    ('1','1'),('2','2'),('3','3'),(' - ','-'),
                    ('0','0'),('.','.'),('(','('),(')',')'),
                    (' + ','+'),('x','x'),('xʸ','**'),(' C ','CLEAR')
                ]
                for i, (label, val) in enumerate(num_map):
                    kcols[i%4].button(
                        label, 
                        key=f"k_{i}", 
                        use_container_width=True,
                        on_click=agregar_valor,
                        args=(val,)
                    )
            with t2:
                fcols = st.columns(2)
                func_map = [
                    ('sin(x)','sin('), ('cos(x)','cos('), 
                    ('tan(x)','tan('), ('ln(x)','log('), 
                    ('√x','sqrt('), ('eˣ','exp('), 
                    ('π','pi'), ('( )','(')
                ]
                for i, (label, val) in enumerate(func_map):
                    fcols[i%2].button(
                        label, 
                        key=f"f_{i}", 
                        use_container_width=True,
                        on_click=agregar_valor,
                        args=(val,)
                    )

    # Asignar a la variable global
    funcion_input = st.session_state.funcion_input_val

    col1_lim, col2_lim = st.columns(2)
    with col1_lim:
        a = st.number_input("Límite a", value=3.0)
    with col2_lim:
        b = st.number_input("Límite b", value=20.0)

    # Condiciones de "n" para cada metodo
    if opcion == "Jorge Boole":
        n = st.number_input("Número de particiones (n)", value=4, disabled=True)

    elif opcion == "T.Simpson 3/8":
        n = st.number_input("Número de particiones (n)", value=3, disabled=True)

    elif opcion == "T.Simpson 1/3":
        n = st.number_input("Número de particiones (n)", value=2, disabled=True)

    else:
        n = st.number_input("Número de particiones (n)", value=6, min_value=1)

    st.divider()

    calcular = st.button("Calcular integral")


# Cuerpo principal de la página
st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='font-size: 3rem; font-weight: 800; margin-bottom: 0.5rem;'>
            <span class='integral-symbol'>Métodos</span> Numéricos
        </h1>
        <p style='color: #94a3b8; font-size: 1.1rem;'>Calculadora avanzada para métodos numéricos</p>
    </div>
""", unsafe_allow_html=True)

if calcular:
    try:
        f_num = obtener_funcion(funcion_input)
        
        if opcion == "Trapezoidal":
            resultado, datos = regla_trapezoidal(f_num, a, b, n)
        elif opcion == "Jorge Boole":
            resultado, datos = regla_boole(f_num, a, b)
        elif opcion == "T.Simpson 3/8":
            resultado, datos = regla_simpson38(f_num, a, b)
        elif opcion == "T.Simpson 1/3":
            resultado, datos = regla_simpson13(f_num, a, b)
        elif opcion == "Simpson abierto":
            resultado, datos = regla_simpson_abierta(f_num, a, b, n)
        
        # Panel de Resultados Rápidos
        st.markdown("### 📊 Resumen del Cálculo")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Resultado Final", f"{resultado:.8f}")
        with c2:
            st.metric("Método", opcion)
        with c3:
            st.metric("Particiones (n)", n)

        st.markdown("---")
        
        # Pestañas para organizar la información
        tab1, tab2, tab3, tab4 = st.tabs(
            ["📉 Visualización", "📊 Datos del Gráfico", "📝 Desglose de Operación", "✨ Resultado Final"]
        )

        with tab1:
            grafica = crear_grafico(f_num, a, b, funcion_input, datos)
            st.plotly_chart(grafica, use_container_width=True)
        with tab2:
            st.subheader("Valores del gráfico")
            nombre_columna = f"y = {funcion_input}"
            datos_mostrar = datos.rename(columns={"f(xi)": nombre_columna})
            st.dataframe(
                datos_mostrar.style.format({"xi": "{:.2f}", nombre_columna: "{:.9f}"}),
                use_container_width=True,
            )
        with tab3:
            st.subheader("Desglose del cálculo por iteración")
            
            # Crear copia de los datos para el desglose
            df_desglose = datos.copy()
            
            # Calcular sumatoria de los términos
            suma_terminos = df_desglose["Término"].sum()
            
            # Añadir fila de sumatoria
            # Usamos un diccionario para la nueva fila
            fila_sumatoria = {
                "i": "TOTAL",
                "xi": np.nan,
                "f(xi)": np.nan,
                "Coeficiente": np.nan,
                "Término": suma_terminos
            }
            df_desglose = pd.concat([df_desglose, pd.DataFrame([fila_sumatoria])], ignore_index=True)

            # Renombrar columnas para mayor claridad según el pedido
            df_desglose = df_desglose.rename(columns={
                "xi": "Valor x (xi)",
                "f(xi)": f"y = {funcion_input}",
                "Coeficiente": "Constante Formula",
                "Término": "Resultado"
            })

            # Mostrar tabla con formato
            st.dataframe(
                df_desglose.style.format({
                    "Valor x (xi)": "{:.4f}",
                    "Función f(xi)": "{:.6f}",
                    "Constante Formula": "{:.0f}",
                    "Resultado": "{:.6f}"
                }, na_rep="-"),
                use_container_width=True
            )
            
            st.success(f"**Sumatoria de términos:** {suma_terminos:.8f}")
            st.code(f"Resultado final ≈ {resultado}")

        with tab4:
            st.markdown(f"""
                <div style='background: rgba(99, 102, 241, 0.1); padding: 2rem; border-radius: 20px; border: 1px solid rgba(99, 102, 241, 0.3); text-align: center;'>
                    <h2 style='color: white; margin-bottom: 1rem;'>✨ ¡Cálculo Exitoso!</h2>
                    <p style='color: #94a3b8; margin-bottom: 2rem;'>Se ha procesado la función <b>{funcion_input}</b> en el intervalo [<b>{a}</b>, <b>{b}</b>].</p>
                    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;'>
                        <div style='background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 15px;'>
                            <small style='color: #94a3b8;'>Sumatoria Total (Σ términos)</small>
                            <h3 style='color: #00d1b2; margin: 0;'>{suma_terminos:.8f}</h3>
                        </div>
                        <div style='background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 15px;'>
                            <small style='color: #94a3b8;'>Valor de la Integral (I)</small>
                            <h3 style='color: #6366f1; margin: 0;'>{resultado:.8f}</h3>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.info("💡 Consejo: Puedes cambiar el método en el menú lateral para comparar precisiones.")

    except Exception as e:
        st.error(f"⚠️ Error en el procesamiento: {str(e)}")
        st.info("Asegúrese de usar sintaxis válida (ej. sin(x), x**2, exp(x))")
else:
    # Estado inicial: Pantalla de Bienvenida
    st.markdown("""
        <div style='background: rgba(255,255,255,0.02); padding: 3rem; border-radius: 30px; border: 1px dashed rgba(255,255,255,0.1); text-align: center; margin-top: 2rem;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>📊</div>
            <h2 style='color: white;'>¡Bienvenido a la Calculadora de Métodos Numéricos!</h2>
            <p style='color: #94a3b8; max-width: 600px; margin: 0 auto 2rem;'>
                Configura los parámetros en el menú lateral izquierdo (función, límites, método e intervalos) 
                y presiona el botón <b>'Calcular integral'</b> para visualizar los resultados.
            </p>
            <div style='display: flex; justify-content: center; gap: 2rem; color: #6366f1; font-weight: 600;'>
                <span>✓ Precisión Alta</span>
                <span>✓ Gráficos Interactivos</span>
                <span>✓ Desglose Paso a Paso</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
