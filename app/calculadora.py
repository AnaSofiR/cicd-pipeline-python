# app/calculadora.py
"""
Módulo calculadora.py
"""

AUTORES = "jsocampod@eafit.edu.co, asrodriguo@eafit.edu.co," \
" jdgutierrg@eafit.edu.co, mgutierrej@eafit.edu.co"  
# IMPORTANTE: Reemplaza con los usuarios de correo de EAFIT de los
#  estudiantes que participaron en la entrega, separados por comas.


def sumar(a, b):
    """
    Método de suma
    """
    return a + b


def restar(a, b):
    """
    Método de resta
    """
    return a - b


def multiplicar(a, b):
    """
    Método de multiplicación
    """
    return a * b


def dividir(a, b):
    """
    Método de división
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
