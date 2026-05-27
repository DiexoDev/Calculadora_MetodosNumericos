import sympy as sp

def evaluar_funcion(func_str, x_valor):
    try:
        x = sp.symbols('x')
        # Reemplazar ^ por ** para que sea compatible con Python
        func_str = func_str.replace('^', '**')
        expr = sp.sympify(func_str)
        # Convertir a función numérica rápida (lambdify)
        f = sp.lambdify(x, expr, 'numpy')
        return float(f(x_valor))
    except Exception as e:
        raise ValueError(f"Error al evaluar la función: {e}")

def obtener_funcion(func_str):
    x = sp.symbols('x')
    func_str = func_str.replace('^', '**')
    expr = sp.sympify(func_str)
    return sp.lambdify(x, expr, 'numpy')


