import pandas as pd
import glob, re, os, math
import numpy as np
pd.set_option("display.max_columns", 100)

genelist_file = "../geneSets/organized_Table/kegg_go_list.xls"
geneList_df = pd.read_csv(genelist_file, sep="\t", header=None)
geneList = geneList_df.iloc[:,0].tolist()

cnv_path = "/Users/yiwenbu/Desktop/CNV_TCGA_GISTIC_RESULTS/*/all_thresholded.by_genes.txt"
for file in glob.glob(cnv_path):
    try:
        tumorName = re.search('org_(.+?)-T', file).group(1)
    except AttributeError:
        print file
    df = pd.read_csv(file, sep="\t", index_col=0)
    df_group = df[df.index.isin(geneList)]
    df_group_s = df_group.drop(["Locus ID","Cytoband"], axis=1)

    num_sample = df_group_s.shape[1]

    df_count = pd.DataFrame()
    for index, row in df_group_s.iterrows():
        count = row.value_counts()
        df_count = pd.concat([df_count, count], axis=1)

    df_count.fillna(0, inplace=True)
    df_freq = df_count/num_sample*100
    save_path = os.path.join("../CNV", "Freq_byGene", tumorName + ".xls")
    df_freq.T.to_csv(save_path, sep="\t")









