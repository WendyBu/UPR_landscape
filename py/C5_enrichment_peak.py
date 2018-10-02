import pandas as pd
import glob, re, os
import numpy as np
pd.set_option("display.max_columns", 100)

upr_list = pd.read_csv("../geneSets/organized_Table/kegg_go_list.xls", sep="\t", header=None, index_col=0)
upr_list = upr_list.index.tolist()

amp_peak = "/Users/yiwenbu/Desktop/CNV_TCGA_GISTIC_RESULTS/*/amp_genes.conf_99.txt"
del_peak = "/Users/yiwenbu/Desktop/CNV_TCGA_GISTIC_RESULTS/*/del_genes.conf_99.txt"


def cal_enrichment(genelist, genes_confiles):
    stat = pd.Series()
    for file in glob.glob(genes_confiles):
        try:
            tumorName = re.search('org_(.+?)-T', file).group(1)
        except AttributeError:
            print file
        df = pd.read_csv(file, sep="\t", index_col=0, skiprows=4, header=None)
        df.reset_index(drop=True, inplace=True)
        all_gene = df.values.ravel()
        all_gene = [x for x in all_gene if str(x) != 'nan']
        all_gene = list(map(lambda x: x.split("|")[0], all_gene))
        common_genes = set(genelist).intersection(all_gene)
        upr_amp_num = len(common_genes)
        upr_num = len(genelist)
        upr_ratio = float(upr_amp_num)/upr_num
        other_ratio = float(len(all_gene))/25207
        try:
            enrich_ratio = upr_ratio/other_ratio
        except ZeroDivisionError:
            print tumorName, "float division by zero"
        stat[tumorName] = enrich_ratio
        stat.sort_values(inplace=True)
    return stat



amp_stat = cal_enrichment(upr_list, amp_peak)
del_stat = cal_enrichment(upr_list, del_peak)
# amp_stat.to_csv("../CNV/cnv_enrichment/amp_enrich.xls", sep="\t")
# del_stat.to_csv("../CNV/cnv_enrichment/del_enrich.xls", sep="\t")

## combine amp and del
del_stat2 = del_stat.apply(lambda x: -x)
all_stat = pd.concat([amp_stat,del_stat2], axis=1,join='outer')
all_stat.to_csv("../CNV/cnv_enrichment/all_enrich.xls", sep="\t")
