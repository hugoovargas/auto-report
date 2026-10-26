
import pandas as pd

from autoreport.cleaner import limpar_vendas


def test_limpar_nomes_das_colunas():
    vendas = pd.DataFrame({
        " Produto ": ["Mouse"],
        " Categoria ": ["Periféricos"],
        " Preco Unitario ": [50.0],
    })

    resultado = limpar_vendas(vendas)

    assert list(resultado.columns) == [
        "produto",
        "categoria",
        "preco unitario",
    ]


def test_remover_espacos_extras_dos_textos():
    vendas = pd.DataFrame({
        "produto": ["  Mouse   Gamer  "],
        "categoria": ["  Informática  "],
    })

    resultado = limpar_vendas(vendas)

    assert resultado.loc[0, "produto"] == "Mouse Gamer"
    assert resultado.loc[0, "categoria"] == "Informática"


def test_converter_texto_vazio_em_valor_ausente():
    vendas = pd.DataFrame({
        "produto": ["   "],
        "categoria": [""],
    })

    resultado = limpar_vendas(vendas)

    assert pd.isna(resultado.loc[0, "produto"])
    assert pd.isna(resultado.loc[0, "categoria"])


def test_nao_alterar_dataframe_original():
    vendas = pd.DataFrame({
        " Produto ": ["  Mouse  "],
    })

    limpar_vendas(vendas)

    assert " Produto " in vendas.columns
    assert vendas.loc[0, " Produto "] == "  Mouse  "
