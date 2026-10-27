import pandas as pd

from autoreport.validator import validar_vendas

def test_validar_vendas_com_registro_valido():
    vendas = pd.DataFrame([
        {
            "id_venda": 1,
            "data": "2026-10-20",
            "produto": "Teclado",
            "quantidade": 2,
            "preco_unitario": 150.00,
            "categoria": "Periféricos",
        }
    ])

    validas, invalidas = validar_vendas(vendas)

    assert len(validas) == 1
    assert invalidas.empty
    assert validas.iloc[0]["quantidade"] == 2


def test_invalidar_venda_com_campo_obrigatorio_vazio():
    vendas = pd.DataFrame([
        {
            "id_venda": 1,
            "data": "2026-10-20",
            "produto": "",
            "quantidade": 2,
            "preco_unitario": 150.00,
            "categoria": "Periféricos",
        }
    ])

    validas, invalidas = validar_vendas(vendas)

    assert validas.empty
    assert len(invalidas) == 1
    assert "Campo obrigatório vazio: produto" in (
        invalidas.iloc[0]["motivo_validacao"]
    )


def test_invalidar_vendas_com_ids_duplicados():
    vendas = pd.DataFrame([
        {
            "id_venda": 1,
            "data": "2026-10-20",
            "produto": "Teclado",
            "quantidade": 2,
            "preco_unitario": 150.00,
            "categoria": "Periféricos",
        },
        {
            "id_venda": 1,
            "data": "2026-10-21",
            "produto": "Mouse",
            "quantidade": 1,
            "preco_unitario": 80.00,
            "categoria": "Periféricos",
        },
    ])

    validas, invalidas = validar_vendas(vendas)

    assert validas.empty
    assert len(invalidas) == 2

    assert invalidas["motivo_validacao"].str.contains(
         "ID de venda duplicado"
     ).all()


def test_converter_dados_validos_para_tipos_adequados():
    vendas = pd.DataFrame({
        "id_venda": ["V001"],
        "data": ["2026-10-27"],
        "produto": ["mouse"],
        "quantidade": ["3"],
        "preco_unitario": ["19.90"],
        "categoria": ["perifericos"],
    })

    validas, invalidas = validar_vendas(vendas)

    assert len(validas) == 1
    assert invalidas.empty

    assert pd.api.types.is_datetime64_any_dtype(validas["data"])
    assert pd.api.types.is_integer_dtype(validas["quantidade"])
    assert pd.api.types.is_numeric_dtype(validas["preco_unitario"])

    assert validas.loc[0, "quantidade"] == 3
    assert validas.loc[0, "preco_unitario"] == 19.90


