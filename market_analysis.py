import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt

#reading example_file
censo = pd.read_excel('censo_es3.xlsx')

print(censo['idade'].value_counts())
print(censo['levar_cartao'].value_counts())
print(censo['periodo_compra'].value_counts())
print(censo['periodo_compra_Cartao'].value_counts())

def compute_mudanca(df1, df2):
    for i, c in df1.iterrows(), df2.iterrows():
        if i == c:
            return "Igual"
        if i != c and c == 'Noturno':
            return 'Noturno'
        if i != c and c == "Vespertino":
            return 'Vespertino'
        if i != c and c == "Matutino":
            return 'Matutino'
        
a = censo['periodo_compra']
b = censo['periodo_compra_Cartao']
censo["mudanca_cartao"] = compute_mudanca(a, b)

print(censo['mudanca_cartao'].value_counts())
#plt.scatter(a, b, color = 'green')
#plt.title("Teste")
#plt.xlabel("...")
#plt.show()