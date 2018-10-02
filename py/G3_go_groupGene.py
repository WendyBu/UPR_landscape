"""
output: geneSets/GO_symbol_list/
gene symbol converted
"""



import pandas as pd
import glob, re, os, math
import numpy as np
pd.set_option("display.max_columns", 100)



convert_table = pd.read_csv("../geneSets/genename_conversion_table.xls", sep="\t")
GO_path = "../geneSets/GO_genelist/*"

ERAD = pd.read_csv("../geneSets/GO_genelist/ERAD.txt", sep="\t", skiprows=2, header=None)
ERAD = ERAD.loc[:, 1]
print ERAD
ERAD.to_csv("../geneSets/GO_symbol_list/ERAD.txt", sep="\t", index=False)



def convert_symbol(uniProt, convert_df):
    df_symbol = convert_df[convert_df["UniProt_ID"].isin(uniProt)]
    gene_symbol = df_symbol[["Symbol"]]
    gene_symbol.drop_duplicates(inplace=True)
    return gene_symbol



for file in glob.glob(GO_path):
    df = pd.read_table(file, sep="\t", header=None, skiprows=2)
    basename = os.path.basename(file)
    if df.shape[1]>2:
        df_uni = df.iloc[:,0].str.split(":", expand=True)
        if df_uni.shape[1]>1:
            genelist = df_uni[1].tolist()
            geneSymbol = convert_symbol(genelist, convert_table)
            geneSymbol.to_csv("../geneSets/GO_symbol_list/"+basename, sep="\t", index=False)




