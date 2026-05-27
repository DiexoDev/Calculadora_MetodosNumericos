# 📊 Calculadora de Métodos Numéricos

Una aplicación web interactiva de alto nivel diseñada para el cálculo de integrales definidas utilizando diversos algoritmos de análisis numérico. Desarrollada con **Python**, **Streamlit** y una estética moderna **Glassmorphism**.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Características Principales

- 🔢 **Teclado Matemático Integrado**: Escribe funciones potentes (sin, cos, ln, exp, etc.) de forma visual y rápida.
- 📈 **Gráficos Interactivos**: Visualización en tiempo real del área bajo la curva mediante **Plotly**.
- 📝 **Desglose Paso a Paso**: Tabla detallada con coeficientes (pesos) y resultados parciales de cada iteración.
- 🎨 **Interfaz Premium**: Diseño robusto en modo oscuro con efectos de desenfoque y gradientes dinámicos.
- ⚡ **Precisión Garantizada**: Algoritmos sincronizados con guías académicas estándar.

---

## 🛠️ Métodos Implementados

La calculadora permite comparar resultados entre los siguientes métodos:

1.  **Regla Trapezoidal**: Aproximación lineal por intervalos.
2.  **Regla de Jorge Boole**: Método de Newton-Cotes de alto orden (n=4).
3.  **Regla de Simpson 1/3**: Ajuste parabólico para mayor precisión.
4.  **Regla de Simpson 3/8**: Ideal para intervalos múltiplos de tres.
5.  **Simpson Abierto**: Extensión para múltiples particiones pares.

---

## 🚀 Instalación y Uso

### Opción 1: Ejecución Rápida (Windows)
Si estás en Windows y tienes Python instalado, simplemente descarga la carpeta y ejecuta:
```bash
ejecutar_proyecto.bat
```

### Opción 2: Instalación Manual
1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/metodos-numericos-streamlit.git
    cd metodos-numericos-streamlit
    ```
2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Correr la aplicación:**
    ```bash
    streamlit run app.py
    ```

---

## 📁 Estructura del Proyecto

```text
├── app.py                # Interfaz principal de la aplicación
├── metodos/              # Implementación lógica de los algoritmos
├── utils/                # Utilidades de evaluación matemática
├── graficas/             # Generación de gráficos dinámicos
├── requirements.txt      # Librerías necesarias
└── ejecutar_proyecto.bat # Lanzador para Windows
```

---

## 👨‍💻 Autor
Desarrollado por Diego Berrio Perez para la facultad de ingeniería.
