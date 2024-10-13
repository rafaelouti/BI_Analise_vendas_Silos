Análise de Vendas de Silos
Este repositório contém uma análise de dados de vendas para diferentes silos. Os dados são originados de um arquivo Excel e visualizados usando bibliotecas Python como Pandas, Matplotlib e Seaborn.

Dados
Os dados são armazenados em um arquivo Excel chamado Pasta 1.xlsx. Ele inclui as seguintes colunas:

ID_Venda : ID da venda
Data : Data da venda
Vendedor : Vendedor
Cliente : Cliente
Produto : Produto (Silo)
Quantidade : Quantidade vendida
Preço_Unitário : Preço unitário
Total : Valor total da venda
Visualização
Os dados de vendas são visualizados em um gráfico de barras para mostrar o total de vendas para cada silo. Abaixo está um exemplo do gráfico gerado:

Quer gráficos melhores? Veja no modo interativo 

Interativo

Estático
cair pra trás

Uso
Para gerar o gráfico de vendas:

Certifique-se de ter o Python instalado com as bibliotecas necessárias: Pandas, Matplotlib e Seaborn.
Execute o script fornecido para carregar os dados e gerar a visualização.

Download

Cópia
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_excel('Pasta 1.xlsx', sheet_name='Planilha1')

# Group by product and sum the total sales
silo_sales = df.groupby('Produto')['Total'].sum().sort_values(ascending=False)

# Plot the data
plt.figure(figsize=(10, 6))
sns.barplot(x=silo_sales.index, y=silo_sales.values)
plt.title('Vendas Totais por Silo')
plt.xlabel('Silo')
plt.ylabel('Vendas Totais (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
