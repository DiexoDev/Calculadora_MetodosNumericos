import plotly.graph_objects as go
import numpy as np

def crear_grafico(f, a, b, func_str, datos):
    # Rango para la curva suave
    x_suave = np.linspace(a - 0.5, b + 0.5, 400)
    y_suave = f(x_suave)
    
    # Rango para el área bajo la curva
    x_area = np.linspace(a, b, 200)
    y_area = f(x_area)
    
    fig = go.Figure()
    
    # Curva de la función
    fig.add_trace(go.Scatter(
        x=x_suave, y=y_suave,
        name=f'f(x) = {func_str}',
        line=dict(color='#00d1b2', width=3)
    ))
    
    # Área bajo la curva
    fig.add_trace(go.Scatter(
        x=x_area, y=y_area,
        fill='tozeroy',
        fillcolor='rgba(0, 209, 178, 0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        name='Área calculada'
    ))
    
    # Puntos usados por el método
    fig.add_trace(go.Scatter(
        x=datos['xi'], y=datos['f(xi)'],
        mode='markers',
        marker=dict(color='#ff3860', size=8),
        name='Puntos de evaluación'
    ))
    
    fig.update_layout(
        title=f"Gráfica de {func_str}",
        template="plotly_dark",
        xaxis_title="x",
        yaxis_title="f(x)",
        hovermode="x unified"
    )
    
    return fig
