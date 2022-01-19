import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../../')

import main

def test_introduce_palabra(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Marca")
    assert main.introduce_valor("prueba", "palabra") == "Marca"


def test_introduce_palabra_error(monkeypatch):
     monkeypatch.setattr('builtins.input', lambda _: "La marca es ")
     monkeypatch.setattr('builtins.input', lambda _: "Marca")
     assert main.introduce_valor("prueba", "palabra") == "Marca"


def test_introduce_frase(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "La marca es")
    assert main.introduce_valor2("prueba", "frase") == "La marca es"


def test_pedir_valor_letra(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "a")
    assert main.introduce_valor_letra("prueba", "letra") == "a"


def test_pedir_valor_letra_2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "A")
    assert main.introduce_valor_letra_mayuscula("prueba", "letra") == "A"


def test_pedir_valor_letra_numero(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5)
    assert main.introduce_valor_numero("prueba", "numero") == 5


