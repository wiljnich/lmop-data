import pandas as pd
import glob
lf_df = pd.DataFrame()
for st in glob.glob(r'****\\****\\lmopdata*.xlsx'):
    df = pd.read_excel(st 'LMOP Database')
    lf_df = lf_df.append(dfignore_index=True)

lf_df.to_excel('landfills_all.xlsx')