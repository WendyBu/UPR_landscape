import pandas as pd
import glob, re, os
import numpy as np
pd.set_option("display.max_columns", 100)

sample_info = pd.read_csv("../info/all_sample_info.csv", sep="\t")
sample_info = sample_info[["Sample ID", "Sample Type"]]

def add_sample_type(sample_info, data_file ):
    """
    from TCGA meta data, add sample type to each dataframe, tumor or primary
    :param sample_info:
    :return:
    """
    df = pd.read_csv(data_file, sep="\t")
    df["Sample_ID"] = df["Sample_ID"].str.split("-")
    df["Sample_ID"] = df["Sample_ID"].apply(lambda x: x[0:4])
    df["Sample_ID"] = df["Sample_ID"].apply(lambda x: '-'.join(x))

    df2 = df.merge(sample_info, how="inner", left_on = "Sample_ID", right_on = "Sample ID")
    df2.drop("Sample ID", inplace=True, axis=1)
    return df2

for file in glob.glob("../protein/upr_protein_matrix/*"):
    matrix_label = add_sample_type(sample_info, file)
    basename = os.path.basename(file)
    save_path = os.path.join("../protein/upr_protein_matrix_label", basename)
    matrix_label.to_csv(save_path, sep="\t", index=False)



