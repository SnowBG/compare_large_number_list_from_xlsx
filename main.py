import pandas as pd
import xlrd

title = ['ICCID']
planilha = pd.read_excel('ICCIDs.xlsx', names=title,header=None)
df = pd.DataFrame(planilha)
df.index.name = 'Linha'
duplicados = df[df.duplicated()]
print(duplicados)