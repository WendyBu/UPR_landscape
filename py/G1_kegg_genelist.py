import pandas as pd
import glob, re, os, math
import numpy as np
pd.set_option("display.max_columns", 100)

filename = "../geneSets/KEGG_genelist/KEGG_hsa04141.txt"
df_whole = pd.read_csv("../geneSets/genename_conversion_table.xls", sep="\t")

def convert_ID(filename, type, skiprow=0):
    """
    :param filename: the pathway filename.txt, kegg using Entrez_ID
    :param type: Symbol or any type of ID
    :return: the list of symbols
    """
    df = pd.read_table(filename, sep="\t", header=None, skiprows=skiprow)
    df2 = df.loc[df.iloc[:,0].str.startswith("hsa:")]
    df3 = df2.iloc[:,0].str.split(" ", expand=True)[0]
    df4 = df3.str.split(":", expand=True)[1].unique()
    symbols = df_whole[df_whole["Entrez_ID"].isin(df4)][type]
    return symbols


signaling_symbol = convert_ID(filename, type="Symbol", skiprow=5)
signaling_symbol.to_csv("../geneSets/organized_Table/kegg_upr.xls", sep="\t", index=False)




