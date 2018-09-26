"""
read in geneSets/GO_genelist/unfolded_protein_GO_all.txt
and combine kegg and this GO table
FINAL TABLE: geneSets/organized_Table/kegg_go_list.xls
"""


import pandas as pd
import glob, re, os, math
import numpy as np
pd.set_option("display.max_columns", 100)

df = pd.read_csv("../geneSets/GO_genelist/unfolded_protein_GO_all.txt", sep="\t", skiprows=2, header=None)
GO_list = df.iloc[:, 2]
GO_list.drop_duplicates(inplace=True)
GO_list.to_csv("../geneSets/organized_Table/GO_table.xls", sep="\t", index=False)

kegg_df = pd.read_csv("../geneSets/organized_Table/kegg_upr.xls", sep="\t", header=None)
print kegg_df.shape

df_all = pd.concat([GO_list,kegg_df], axis=0, ignore_index=True)
df_all.drop_duplicates(inplace=True)
print df_all.head(), df_all.shape
df_all.to_csv("../geneSets/organized_Table/kegg_go_list.xls", sep="\t", header=None, index=False)


