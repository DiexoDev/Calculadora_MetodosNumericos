import numpy as np
import pandas as pd

def regla_trapezoidal(f, a, b, n):
    delta = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    # Coeficientes: 1 para los extremos, 2 para los internos
    coefs = np.ones(n + 1)
    if n > 0:
        coefs[1:-1] = 2
    
    terminos = coefs * y
    integral = (delta / 2) * np.sum(terminos)

    datos = pd.DataFrame({
        "i": range(n + 1),
        "xi": x,
        "f(xi)": y,
        "Coeficiente": coefs,
        "Término": terminos
    })

    return integral, datos

def regla_boole(f, a, b):
    delta = (b - a) / 4
    x = np.linspace(a, b, 5)
    y = f(x)

    coefs = np.array([7, 32, 12, 32, 7])
    terminos = coefs * y
    integral = (2 * delta / 45) * np.sum(terminos)

    datos = pd.DataFrame({"i": range(5), "xi": x, "f(xi)": y, "Coeficiente": coefs, "Término": terminos})

    return integral, datos

def regla_simpson38(f, a, b):
    delta = (b - a) / 3
    x = np.linspace(a, b, 4)
    y = f(x)

    coefs = np.array([1, 3, 3, 1])
    terminos = coefs * y
    integral = (3 * delta / 8) * np.sum(terminos)

    datos = pd.DataFrame({"i": range(4), "xi": x, "f(xi)": y, "Coeficiente": coefs, "Término": terminos})

    return integral, datos

def regla_simpson13(f, a, b):
    delta = (b - a) / 2
    x = np.linspace(a, b, 3)
    y = f(x)

    coefs = np.array([1, 4, 1])
    terminos = coefs * y
    integral = (delta / 3) * np.sum(terminos)

    datos = pd.DataFrame({"i": range(3), "xi": x, "f(xi)": y, "Coeficiente": coefs, "Término": terminos})

    return integral, datos

def regla_simpson_abierta(f, a, b, n):
    if n % 2 != 0: 
        raise ValueError("n No puede ser un numero impar")

    delta = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    coefs = np.ones(n + 1)
    for i in range(1, n):
        coefs[i] = 4 if i % 2 != 0 else 2
    
    terminos = coefs * y
    integral = (delta / 3) * np.sum(terminos)

    datos = pd.DataFrame({
        "i": range(n + 1),
        "xi": x,
        "f(xi)": y,
        "Coeficiente": coefs,
        "Término": terminos
    })

    return integral, datos