import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading example_file
censo = pd.read_excel('censo_es3.xlsx')
#
#print(censo['idade'].value_counts())
#print(censo['levar_cartao'].value_counts())
#print(censo['periodo_compra'].value_counts())
#print(censo['periodo_compra_Cartao'].value_counts())
#
def compute_mudanca(df1, df2):
    for i, c in zip(df1, df2):
        if i == c:
            return "Igual"
        if i != c and c == 'Noturno':
            return 'Noturno'
        if i != c and c == "Vespertino":
            return 'Vespertino'
        if i != c and c == "Matutino":
            return 'Matutino'
        
#a = censo['periodo_compra']
#b = censo['periodo_compra_Cartao']
#censo["mudanca_cartao"] = compute_mudanca(a, b)

#df2 = pd.DataFrame(np.random.rand(10, 3), columns=["periodo_compra", "periodo_compra_Cartao", "mudanca_cartao"])
#df2.plot.bar()

#c = censo['mudanca_cartao'].value_counts()
#plt.bar(censo["mudanca_cartao"],c, color = 'green')
#plt.title("Teste")
#plt.xlabel("...")
#plt.show()

censo['genero'].plot.pie(y='Gênero', figsize=(5, 5))