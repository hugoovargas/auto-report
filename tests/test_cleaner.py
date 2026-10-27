import pandas as pd
import pytest

from autoreport.cleaner import padronizar_colunas, padronizar_textos, padronizar_categorias


def test_limpar_nomes_das_colunas():
    vendas = pd.DataFrame({
        " Produto ": ["Mouse"],
        " Categoria ": ["Periféricos"],
        " Preco  Unitario ": [50.0]
    })

    resultado = padronizar_colunas(vendas)

    assert list(resultado.columns) == [
        "produto",
        "categoria",
        "preco_unitario"
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

def test_padronizar_maiusculas_e_minusculas():
    vendas = pd.DataFrame({
        "produto": ["mouse", "MOUSE", "Mouse"],
        "categoria": ["Eletrônicos", "ELETRÔNICOS", "eletrônicos"]
    })

    resultado = padronizar_textos(vendas)

    assert resultado["produto"].tolist() == [
        "mouse", "mouse", "mouse"
    ]

    assert resultado["categoria"].tolist() == [
        "eletrônicos", "eletrônicos", "eletrônicos"
    ]


def test_remover_espacos_extras():
    vendas = pd.DataFrame({
        "produto": ["  mouse   gamer  "],
        "categoria": [" eletrônicos "],
    })

    resultado = padronizar_textos(vendas)

    assert resultado.loc[0, "produto"] == "mouse gamer"
    assert resultado.loc[0, "categoria"] == "eletrônicos"


def test_converter_texto_vazio_em_valor_ausente():
    vendas = pd.DataFrame({
        "produto": ["   "],
        "categoria": [""]
    })

    resultado = padronizar_textos(vendas)

    assert pd.isna(resultado.loc[0, "produto"])
    assert pd.isna(resultado.loc[0, "categoria"])

def test_padronizar_categorias_com_e_sem_acento():
    vendas = pd.DataFrame({
        "categoria": [
            "Perifericos",
            "periféricos",
            "PERIFERICOS",
            "Acessorios",
            "áudio",
            "Moveis"
        ]
    })

    resultado = padronizar_categorias(vendas)

    assert resultado["categoria"].tolist() == [
        "Periféricos",
        "Periféricos",
        "Periféricos",
        "Acessórios",
        "Áudio",
        "Móveis"
    ]

def test_preservar_categorias_desconhecidas():
    vendas = pd.DataFrame({
        "categoria": ["categoria nova"]
    })

    resultado = padronizar_categorias(vendas)

    assert resultado.loc[0, "categoria"] == "categoria nova"

def test_preservar_categorias_vazias():
    vendas = pd.DataFrame({
        "categoria": [pd.NA]
    })

    resultado = padronizar_categorias(vendas)

    assert pd.isna(resultado.loc[0, "categoria"])

