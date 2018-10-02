import pandas as pd
import glob, re, os
import numpy as np
pd.set_option("display.max_columns", 100)


cnv_freq = "../CNV/Freq_byGene/*"
df_amp = pd.DataFrame()
df_del = pd.DataFrame()
for file in glob.glob(cnv_freq):
    try:
        tumorName = os.path.basename(file)
        tumorName = tumorName.split(".")[0]
    except AttributeError:
        print file
    df = pd.read_csv(file, sep="\t", index_col=0)
    df_amp[tumorName] = df.loc[:,"2"]
    df_del[tumorName] = df.loc[:,"-2"]
df_amp["amp_avg"] = df_amp.mean(axis=1)
df_del["del_avg"] = df_del.mean(axis=1)
df_amp.sort_values("amp_avg", ascending=False, inplace=True)
df_amp.to_csv("../CNV/deep_amp.xls", sep="\t")
df_del.sort_values("del_avg", ascending=False, inplace=True)
df_del.to_csv("../CNV/deep_del.xls", sep="\t")
