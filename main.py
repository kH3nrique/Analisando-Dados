#projetos de dados = resolção de problemas

#P1 - importar a base de dados
import pandas as pd
from IPython.display import display

#P2 ->ler essa base
tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop(columns="CustomerID")
display(tabela.info())

#P3 -> correção de erros da base de dados
tabela = tabela.dropna()
print('\n')
display(tabela.info())

#P4 -> anilise dos cancelamentos
print('\n')
display(tabela["cancelou"].value_counts())
print('\n')
display(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))

#P5 -> analise da causa do cancelamento
import plotly.express as px

#criação de gráficos -> criar e exibir
    
for i in tabela.columns:
    #criação->
    grafico = px.histogram(tabela, x=i, color="cancelou")

    #exibição ->
    grafico.show()

# analise da causa de cancelamento->

#se ligou mais de 4
tabela = tabela[tabela["ligacoes_callcenter"]<=4]

#se atrasar mais de 20 dias
tabela = tabela[tabela["dias_atraso"]<=20]

#se tiverrem contrato mensal
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]    

print('\n')
display(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))

import numpy, nbformat, ipykernel