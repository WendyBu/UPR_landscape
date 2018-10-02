"""
label genes by "ATF", "PERK", "IRE1", "ERAD"
"""
import pandas as pd
import glob, re, os
import numpy as np
pd.set_option("display.max_columns", 100)




def label_table(file, keywords, table):
    genelist = pd.read_csv(file)
    genelist = genelist.iloc[:,0].tolist()
    table.loc[table.index.isin(genelist),keywords]=1
    return table


files = ["../geneSets/GO_symbol_list/ATF6_gene_GO.txt", \
         "../geneSets/GO_symbol_list/ERAD.txt",  \
         "../geneSets/GO_symbol_list/IRE1_gene_GO.txt", \
         "../geneSets/GO_symbol_list/Perk_gene_GO.txt",]

keywords = ["ATF6", "ERAD", "IRE1", "PERK"]
table_amp = pd.read_csv("../CNV/deep_amp.xls", sep="\t", index_col=0)
table_del = pd.read_csv("../CNV/deep_del.xls", sep="\t", index_col=0)
for i in range(0,4):
    table_amp = label_table(files[i],keywords[i],table_amp)
    table_del = label_table(files[i],keywords[i],table_del)
table_amp.to_csv("../CNV/amp_lable.xls", sep="\t")
table_del.to_csv("../CNV/del_lable.xls", sep="\t")



