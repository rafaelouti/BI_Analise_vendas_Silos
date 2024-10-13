import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FILEPATH = "Pasta 1.xlsx"
dataframes = {
    "ID_Venda": [1, 2, 3],
    "Data": ["2024-01-15", "2024-02-20", "2024-03-10"],
    "Vendedor": ["João Silva", "Maria Oliveira", "Carlos Santos"],
    "Cliente": ["Agrícola Ltda", "Grãos do Sul", "Agro Indústria"],
    "Produto": ["Silo A", "Silo B", "Silo A"],
    "Quantidade": [10, 5, 8],
    "Preço_Unitário": [1500, 2000, 1500],
}
df = pd.DataFrame(dataframes)
df["Total"] = df["Quantidade"] * df["Preço_Unitário"]
print(df.head())
silo_sales = df.groupby("Produto")["Total"].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=silo_sales.index, y=silo_sales.values)
plt.title("Vendas Totais por Silo")
plt.xlabel("Silo")
plt.ylabel("Vendas Totais (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("Gr\u00e1fico de vendas dos silos criado com sucesso.")
