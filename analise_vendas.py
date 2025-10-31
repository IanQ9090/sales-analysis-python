import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_csv('vendas.csv')

# Mostrar primeiras linhas
print(df.head())

# Criar colunas de Receita e Lucro
df['Receita'] = df['Quantidade'] * df['Preço_Unitário']
df['Lucro'] = df['Receita'] - df['Custo']

# Faturamento por Região
faturamento = df.groupby('Região')['Receita'].sum().reset_index()
sns.barplot(data=faturamento, x='Região', y='Receita')
plt.title('Faturamento por Região')
plt.show()

# Produtos mais vendidos
produtos = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(x=produtos.index, y=produtos.values)
plt.xticks(rotation=45)
plt.title('Produtos mais vendidos')
plt.show()

# Receita por mês
df['Data'] = pd.to_datetime(df['Data'])
df['Mes_Ano'] = df['Data'].dt.to_period('M')
receita_mes = df.groupby('Mes_Ano')['Receita'].sum()
plt.figure(figsize=(10,6))
receita_mes.plot(kind='line', marker='o')
plt.title('Receita Mensal')
plt.ylabel('Receita')
plt.xlabel('Mês/Ano')
plt.grid(True)
plt.show()
