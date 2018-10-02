"""
test: amp gene and del gene in heatmap share no genes.
"""

import pandas as pd
import glob, re, os
import numpy as np
pd.set_option("display.max_columns", 100)

amp_df = pd.read_table("../CNV/heatmap_test/amp_set.gct", sep="\t", skiprows=2, index_col=0)
del_df = pd.read_table("../CNV/heatmap_test/del_set.gct", sep="\t", skiprows=2, index_col=0)

amp_list = amp_df.index.tolist()
del_list = del_df.index.tolist()

intersection_list = set(amp_list).intersection(del_list)
print intersection_list
