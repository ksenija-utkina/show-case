import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.DataFrame()

wrt = pd.ExcelWriter("c:\project\General_data.xlsx")

for f in ['C:\project\data_1.xlsx','C:\project\data_2.xlsx']:
    data = pd.read_excel(f, sheet_name = 'Sheet1')
    data['from'] = [os.path.basename(f)] * len(data)
    df = df.append(other=data)
df.to_excel(wrt, "Sheet1")

df1 = pd.DataFrame()
for f in ['C:\project\data_1.xlsx','C:\project\data_4.xlsx']:
    data = pd.read_excel(f, sheet_name = 'Sheet2')
    data['from'] = [os.path.basename(f)] * len(data)
    df1 = df1.append(other=data)
df1.to_excel(wrt, "Sheet2", verbose=True)
wrt.save()

df2 = pd.DataFrame()
for f in ['C:\project\data_3.xlsx','C:\project\data_4.xlsx']:
    data = pd.read_excel(f, sheet_name = 'Sheet1')
    data['from'] = [os.path.basename(f)] * len(data)
    df2 = df2.append(other=data)
df2.to_excel(wrt, "Sheet3",verbose=True)
wrt.save()

df3 = pd.DataFrame()
for f in ['C:\project\data_2.xlsx','C:\project\data_3.xlsx']:
    data = pd.read_excel(f, sheet_name = 'Sheet2')
    data['from'] = [os.path.basename(f)] * len(data)
    df3 = df3.append(other=data)
df3.to_excel(wrt, "Sheet4", verbose=True)
wrt.save()




