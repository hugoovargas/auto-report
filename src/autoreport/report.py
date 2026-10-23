
from pathlib import Path

import pandas as pd

from autoreport.metrics import (
    calcular_faturamento_por_categoria,
    calcular_faturamento_por_produto,
    calcular_faturamento_total,
    calcular_quantidade_total,
    contar_vendas,
)


def gerar_relatorio(vendas: pd.DataFrame,invalidas: pd.DataFrame,caminho_saida: Path,) -> None:

    caminho_saida.parent.mkdir(parents=True, exist_ok=True)

    indicadores = pd.DataFrame([
        {
            "indicador": "Faturamento total",
            "valor": calcular_faturamento_total(vendas),
        },
        {
            "indicador": "Quantidade total vendida",
            "valor": calcular_quantidade_total(vendas),
        },
        {
            "indicador": "Número de vendas",
            "valor": contar_vendas(vendas),
        },
    ])

    faturamento_por_produto = calcular_faturamento_por_produto(vendas)
    faturamento_por_categoria = calcular_faturamento_por_categoria(vendas)

    with pd.ExcelWriter(caminho_saida, engine="openpyxl") as escritor:
        indicadores.to_excel(
            escritor,
            sheet_name="Resumo",
            index=False,
        )

        faturamento_por_produto.to_excel(
            escritor,
            sheet_name="Resumo",
            index=False,
            startcol=3,
        )

        faturamento_por_categoria.to_excel(
            escritor,
            sheet_name="Resumo",
            index=False,
            startcol=6,
        )

        vendas.to_excel(
            escritor,
            sheet_name="Vendas",
            index=False,
        )

        invalidas.to_excel(
            escritor,
            sheet_name="Registros inválidos",
            index=False,
        )
