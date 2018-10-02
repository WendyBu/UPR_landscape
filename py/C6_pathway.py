import pandas as pd
import glob, re, os
import numpy as np
pd.set_option("display.max_columns", 100)


### amplification file generator
df = pd.read_csv("../CNV/amp_lable.xls", sep="\t", index_col=0)

ATF6_df = df[df["ATF6"] == 1]
ATF6_df.to_csv("../CNV/pathway/ATF6_amp.xls", sep="\t")

PERK_df =  df[df["PERK"] == 1]
PERK_df.to_csv("../CNV/pathway/PERK_amp.xls", sep="\t")

IRE1_df =  df[df["IRE1"] == 1]
IRE1_df.to_csv("../CNV/pathway/IRE1_amp.xls", sep="\t")

ERAD_df =  df[df["ERAD"] == 1]
ERAD_df.to_csv("../CNV/pathway/ERAD_amp.xls", sep="\t")


# deletion file generator
df2 = pd.read_csv("../CNV/del_lable.xls", sep="\t", index_col=0)
ATF6_df2 = df2[df2["ATF6"] == 1].applymap(lambda x: -x)
ATF6_df2.to_csv("../CNV/pathway/ATF6_del.xls", sep="\t")

PERK_df2 =  df2[df2["PERK"] == 1].applymap(lambda x: -x)
PERK_df2.to_csv("../CNV/pathway/PERK_del.xls", sep="\t")

IRE1_df2 =  df2[df2["IRE1"] == 1].applymap(lambda x: -x)
IRE1_df2.to_csv("../CNV/pathway/IRE1_del.xls", sep="\t")

ERAD_df2 =  df2[df2["ERAD"] == 1].applymap(lambda x: -x)
ERAD_df2.to_csv("../CNV/pathway/ERAD_del.xls", sep="\t")