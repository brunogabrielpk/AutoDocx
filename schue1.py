import pandas as pd
import datetime
df = pd.read_excel(r'Listagem.xlsx') 

# AS PRÓXIMAS 3 LINHAS É PORQUE TEM UMA FUCKING BARRA ( / ) 
# NO CABEÇALHO DA COLUNA DA TABELA NO EXCEL
# E TAMBÉM PARA REMOVER ESPAÇOS
cols = df.columns
cols = cols.map(lambda x: x.replace('/', '') if isinstance(x, (str)) else x)
cols = cols.map(lambda x: x.replace(' ', '') if isinstance(x, (str)) else x)
cols = cols.map(lambda x: x.replace('.', '') if isinstance(x, (str)) else x)
df.columns = cols
# É ISTO

for hue in range(5):
    # print(df['Data'][hue])
    # print(type(df['Data'][hue]))
    if isinstance(df['Data'][hue], str):
        print(df['Data'][hue])
    if isinstance(df['Data'][hue], datetime.datetime):
        print(df['Data'][hue].strftime('%d/%m/%Y'))
