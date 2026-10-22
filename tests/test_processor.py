import pandas as pd

from autoreport.processor import processar_vendas

def test_processar_vendas_calcula_faturamento():
    vendas = pd.DataFrame([
        {
            "id_venda": 1,
            "produto": "Teclado",
            "quantidade": 2,
            "preco_unitario": 150.00,
        },
        {
            "id_venda": 2,
            "produto": "Mouse",
            "quantidade": 3,
            "preco_unitario": 80.00,
        },
    ])

    resultado = processar_vendas(vendas)

    assert resultado["faturamento"].tolist() == [
        300.00,
        240.00,
    ]


def test_processar_vendas_nao_altera_dataframe_original():
    vendas = pd.DataFrame([
        {
            "id_venda": 1,
            "produto": "Teclado",
            "quantidade": 2,
            "preco_unitario": 150.00,
        }
    ])

    original = vendas.copy()

    processar_vendas(vendas)

    pd.testing.assert_frame_equal(vendas, original)


def test_processar_vendas_com_dataframe_vazio():
    vendas = pd.DataFrame(
        columns=[
            "id_venda",
            "produto",
            "quantidade",
            "preco_unitario",
        ]
    )

    resultado = processar_vendas(vendas)

    assert resultado.empty
    assert "faturamento" in resultado.columns



