import pandas as pd
from datetime import datetime, timedelta
import random

# Produtos fictícios
produtos = ["Camiseta", "Boné", "Calça Jeans", "Tênis", "Jaqueta"]

# Gerar dados de exemplo
dados = []
for _ in range(20):
    data = datetime(2025, 10, 1) + timedelta(days=random.randint(0, 26))
    produto = random.choice(produtos)
    quantidade = random.randint(1, 10)
    valor_unitario = random.choice([29.9, 49.9, 79.9, 99.9, 149.9])
    dados.append([data.strftime("%Y-%m-%d"), produto, quantidade, valor_unitario])

# Criar DataFrame
df = pd.DataFrame(dados, columns=["Data", "Produto", "Quantidade", "Valor_Unitario"])

# Salvar como Excel
df.to_excel("vendas.xlsx", index=False)
print("✅ Arquivo 'vendas.xlsx' criado com sucesso!")
