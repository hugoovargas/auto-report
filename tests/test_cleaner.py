
import pandas as pd

from autoreport.cleaner import limpar_vendas, padronizar_colunas, padronizar_texto
import pytest


def test_limpar_nomes_das_colunas():
    vendas = pd.DataFrame({
        " Produto ": ["Mouse"],
        " Categoria ": ["Periféricos"],
        " Preco  Unitario ": [50.0],
    })

    resultado = padronizar_colunas(vendas)

    assert list(resultado.columns) == [
        "produto",
        "categoria",
        "preco_unitario",
    ]

def test_padronizar_nomes_das_colunas():
    vendas = pd.DataFrame({
        "ID-VENDA": [1],
        "PRECO UNITARIO": [50.0],
        "CATEGORIA": ["Monitores"]
    })

    resultado = padronizar_colunas(vendas)

    assert list(resultado.columns) == [
        "id_venda",
        "preco_unitario",
        "categoria"
    ]

def test_detectar_colunas_duplicadas_apos_padronizacao():
    vendas = pd.DataFrame({
        "PRODUTO": ["Mouse"],
        "produto": ["Teclado"]
    })

    with pytest.raises(ValueError, match="Colunas Duplicadas"):
        padronizar_colunas(vendas)


def test_remover_espacos_extras_dos_textos():
    vendas = pd.DataFrame({
        "produto": ["  Mouse   Gamer  "],
        "categoria": ["  Informática  "],
    })

    resultado = limpar_vendas(vendas)

    assert resultado.loc[0, "produto"] == "mouse gamer"
    assert resultado.loc[0, "categoria"] == "informática"


def test_converter_texto_vazio_em_valor_ausente():
    vendas = pd.DataFrame({
        "produto": ["   "],
        "categoria": [""],
    })

    resultado = limpar_vendas(vendas)

    assert pd.isna(resultado.loc[0, "produto"])
    assert pd.isna(resultado.loc[0, "categoria"])


# def test_nao_alterar_dataframe_original():
#     vendas = pd.DataFrame({
#         " Produto ": ["  Mouse  "],
#     })
#
#     limpar_vendas(vendas)
#
#     assert " Produto " in vendas.columns
#     assert vendas.loc[0, " Produto "] == "  Mouse  "
