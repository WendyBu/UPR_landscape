"""
generate the folder CNV/q_value
all tumor types, del/amp q value
"""


import pandas as pd
import glob, re, os
import numpy as np
pd.set_option("display.max_columns", 100)


### retrive every upr gene start and end location
upr_list = pd.read_csv("../geneSets/organized_Table/kegg_go_list.xls", sep="\t", header=None, index_col=0)
upr_list = upr_list.index.tolist()
# generate genename, start and end position
gene_df3 = pd.DataFrame()
for genefile in glob.glob("/Users/yiwenbu/PycharmProjects/chrom/chrom_gene_list/*"):
    gene_df = pd.read_csv(genefile, sep="\t")
    gene_df2 = gene_df[["gene_name","start", "end"]]
    gene_df3 = pd.concat([gene_df3, gene_df2], axis=0)
gene_upr_df = gene_df3[gene_df3["gene_name"].isin(upr_list)]
gene_upr_df.set_index("gene_name", inplace=True)



gistic_file = "/Users/yiwenbu/Desktop/CNV_TCGA_GISTIC_RESULTS/*/scores.gistic"
for file in glob.glob(gistic_file):
    try:
        tumorName = re.search('org_(.+?)-T', file).group(1)
        print tumorName
    except AttributeError:
        print file
    df = pd.read_csv(file, sep="\t")
    sigQ = df[df["-log10(q-value)"] >2]  #q value < 0.25, 0.602
    sigQ = sigQ[sigQ["frequency"]>0.20]
    sigQ["Start"] = pd.to_numeric(sigQ["Start"])
    sigQ["End"] = pd.to_numeric(sigQ["End"])


#find region and gene
    sig_upr = pd.DataFrame()
    for index, gene in gene_upr_df.iterrows():
        sigQ2 = sigQ[(sigQ.Start < gene[0]) & (sigQ.End > gene[0])] # gene start site is inside of the amp or del regions
        if not sigQ2.empty:
            sigQ2["gene_name"] = index
            sig_upr = pd.concat([sig_upr, sigQ2], axis=0)
    # sig_upr.sort_values("Type", inplace=True)
    save_path = os.path.join("../CNV/q_value/", tumorName+"_qvalue.xls")
    sig_upr.to_csv(save_path, sep="\t", index=False)

