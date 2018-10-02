import pandas as pd
import glob, re, os
import numpy as np
pd.set_option("display.max_columns", 100)

stat_df = pd.DataFrame()
for file in glob.glob("../CNV/q_value/*"):
    try:
        df = pd.read_csv(file, sep="\t")
        tumorName = os.path.basename(file).split("_")[0]
        df.drop_duplicates(subset=["Type", "gene_name"], inplace=True)
        n = df.groupby("Type").size()
        stat_df[tumorName] = n
    except:
        print tumorName
stat_df.to_csv("../CNV/qvalue_summary_001_freq20.xls", sep="\t")


