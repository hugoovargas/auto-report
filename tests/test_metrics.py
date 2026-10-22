
import pandas as pd

from autoreport.metrics import (
    calcular_faturamento_total,
    calcular_quantidade_total,
    contar_vendas,
    calcular_faturamento_por_produto,
    calcular_faturamento_por_categoria,
)


def criar_vendas_processadas() -> pd.DataFrame:
    return pd.DataFrame([
        {
            "id_venda": 1,
            "produto": "Teclado",
            "categoria": "Periféricos",
            "quantidade": 2,
            "faturamento": 300.00,
        },
        {
            "id_venda": 2,
            "produto": "Mouse",
            "categoria": "Periféricos",
            "quantidade": 3,
            "faturamento": 240.00,
        },
        {
            "id_venda": 3,
            "produto": "Teclado",
            "categoria": "Periféricos",
            "quantidade": 1,
            "faturamento": 150.00,
        },
        {
            "id_venda": 4,
            "produto": "Cadeira",
            "categoria": "Móveis",
            "quantidade": 1,
            "faturamento": 500.00,
        },
    ])


def test_calcular_faturamento_total():
    vendas = criar_vendas_processadas()

    resultado = calcular_faturamento_total(vendas)

    assert resultado == 1190.00


def test_calcular_quantidade_total():
    vendas = criar_vendas_processadas()

    resultado = calcular_quantidade_total(vendas)

    assert resultado == 7


def test_contar_vendas():
    vendas = criar_vendas_processadas()

    resultado = contar_vendas(vendas)

    assert resultado == 4


def test_calcular_faturamento_por_produto():
    vendas = criar_vendas_processadas()

    resultado = calcular_faturamento_por_produto(vendas)

    assert resultado["produto"].tolist() == [
        "Cadeira",
        "Teclado",
        "Mouse",
    ]

    assert resultado["faturamento"].tolist() == [
        500.00,
        450.00,
        240.00,
    ]