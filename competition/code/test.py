import pandas as pd;
import numpy as np;

df = pd.read_stata('../dataResource/cgss2015_14.dta',);
vList = df.columns.values.tolist()

#家庭成员列开始
fStart_col = vList.index('a1201');
fEnd_col = vList.index('a1214');

for index,rowData in df.iterrows():
    if index == 0 :
        print(rowData.notna());
