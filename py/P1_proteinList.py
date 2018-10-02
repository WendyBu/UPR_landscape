import pandas as pd
import glob, re, os
import numpy as np
pd.set_option("display.max_columns", 100)

df = pd.read_csv("../protein/protein_array.txt", sep="\t", index_col=0)
protein_list = df["Gene Name"].tolist()

df_upr = pd.read_csv("../geneSets/organized_Table/kegg_go_list.xls", sep="\t", index_col=0, header=None)
upr_list = df_upr.index.tolist()

common = list(set(protein_list).intersection(upr_list))
with open('../protein/upr_protein.txt', 'w') as f:
    for item in common:
        f.write("%s\n" % item)

