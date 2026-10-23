import pandas as pd

from autoreport.report import gerar_relatorio

def test_gerar_relatorio_excel(tmp_path):
    vendas = pd.DataFrame([
        {
            "id_venda": 1,
            "produto": "Teclado",
            "categoria": "Periféricos",
            "quantidade": 2,
            "preco_unitario": 150.00,
            "faturamento": 300.00,
        },
        {
            "id_venda": 2,
            "produto": "Mouse",
            "categoria": "Periféricos",
            "quantidade": 3,
            "preco_unitario": 80.00,
            "faturamento": 240.00,
        },
    ])

    invalidas = pd.DataFrame([
        {
            "id_venda": 3,
            "produto": "",
            "motivo_validacao": "Campo obrigatório vazio: produto",
        }
    ])

    caminho_saida = tmp_path / "relatorio.xlsx"

    gerar_relatorio(vendas, invalidas, caminho_saida)

    assert caminho_saida.exists()

    with pd.ExcelFile(caminho_saida) as arquivo:
        assert arquivo.sheet_names == ["Resumo","Vendas","Registros inválidos"]

    resumo = pd.read_excel(caminho_saida, sheet_name="Resumo")
    vendas_lidas = pd.read_excel(caminho_saida, sheet_name="Vendas")
    invalidas_lidas = pd.read_excel(
        caminho_saida,
        sheet_name="Registros inválidos",
    )

    assert resumo.iloc[0]["indicador"] == "Faturamento total"
    assert resumo.iloc[0]["valor"] == 540.00

    assert len(vendas_lidas) == 2
    assert "faturamento" in vendas_lidas.columns

    assert len(invalidas_lidas) == 1
    assert "motivo_validacao" in invalidas_lidas.columns
