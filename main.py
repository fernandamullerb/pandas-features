import pandas as pd

#VISUALIZAÇÃO DE DADOS:
vendas = {
    'data': ['07-01-2024', '08-01-2024'],
    'valor': [500, 300],
    'produto': ['feijão', 'arroz'],
    'quantidade': [50, 70]
}
vendas_df = pd.DataFrame(vendas) #transformando dict em df
vendas_df = pd.read_excel('Vendas.xlsx') #no pandas, podemos reatribuir um valor diferente ao mesmo df

vendas_df.head(10) #10 primeiras linhas
vendas_df.shape #qtd de linhas e colunas
vendas_df.describe() #estatísticas (média, mediana etc.)


#SELEÇÃO DE DADOS:
produtos = vendas_df['Produto'] #pegando uma série (coluna) do df
produtos_por_loja_df = vendas_df[['Produto', 'ID Loja']] #pegando mais de uma coluna para criar um novo df (tabela)
vendas_df.loc[0:5] #pegando linhas de acordo com 1 ou mais índices (range) do df

condicao_linhas = vendas_df['ID Loja'] == 'Norte Shopping' #criando a condição das linhas a serem selecionadas
vendas_norte_shopping_df = vendas_df.loc[condicao_linhas] #pegando as linhas que correspondem a condição para criar uma nova tabela
vendas_norte_shopping_df = vendas_df.loc[condicao_linhas, ['Produto', 'Quantidade', 'Valor Unitário']] #filtrando as colunas de interesse
print(vendas_norte_shopping_df) #o método loc permite filtrar linhas e colunas: .loc[linhas, colunas]


#EDIÇÃO DE DADOS:
vendas_df.loc[:, 'Imposto'] = 0 #criando uma nova coluna (Imposto) e populando todas as linhas com valor 0
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05 # criando uma nova coluna (Comissão) e populando com valor a partir de uma coluna que já existe

vendas_dezembro_df = pd.read_excel('Vendas - Dez.xlsx') #pegando outro df com as vendas de dezembro
vendas_df = vendas_df._append(vendas_dezembro_df) #adicionando as vendas de dezembro no df original

gerentes_df = pd.read_excel('Gerentes.xlsx') #pegando outro df com os gerentes de cada loja
vendas_df = vendas_df.merge(gerentes_df) #adicionando uma nova coluna (Gerente) a partir de um outro df
print(vendas_df)

vendas_df = vendas_df.drop('Imposto', axis=1) #removendo coluna Imposto (axis=0 significa Linha o axis=1 significa Coluna)
vendas_df = vendas_df.dropna() #removendo linhas que possuem pelo menos 1 valor vazio (NaN)

vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean()) #preenchendo as linhas vazias da coluna Comissão com a média de Comissão

vendas_df = vendas_df.ffill() #preenchendo as linhas vazias com o último valor populado (first fill)
print(vendas_df)


#AGRUPAMENTO DE DADOS:
transacoes_por_loja = vendas_df['ID Loja'].value_counts() #contador de vendas por loja
print(transacoes_por_loja)

faturamento_por_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum() #agrupa pela coluna Produto e soma as colunas numéricas (Valor Final)
print(faturamento_por_produto)
