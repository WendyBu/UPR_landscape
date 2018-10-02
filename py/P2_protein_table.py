import pandas as pd
import glob, re, os
import numpy as np
pd.set_option("display.max_columns", 100)


upr_list = pd.read_csv("../geneSets/organized_Table/kegg_go_list.xls", sep="\t", header=None,index_col=0)
upr_list = upr_list.index.tolist()
# XBP1	GSK3ALPHABETA	GSK3ALPHABETA_pS21S9	BAX	ASNS BCL2	BCL2A1 are in the protein array list


for file in glob.glob("../protein/download/*"):
    if "L4" in file and ".csv" in file:
        df4 = pd.read_csv(file, sep=",", index_col=0)
        df_upr = pd.DataFrame()
        for gene in upr_list:
            s = df4.loc[:,df4.columns.str.contains(gene)]
            if not s.empty:
                df_upr = pd.concat([df_upr,s], axis=1)
        filebase = os.path.basename(file).split(".")[0]
        save_path = os.path.join("../protein/upr_protein_matrix/", filebase+".xls")
        df_upr.to_csv(save_path, sep="\t")








