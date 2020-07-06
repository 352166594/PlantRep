#!/bin/bash
#PBS -N count_div
#PBS -o /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/zzz-qsub.history/qsub.count_div.29165.log
#PBS -e /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/zzz-qsub.history/qsub.count_div.29165.err
#PBS -q low
# qsub parameter: "-q queue1 -l nodes=1:ppn=1"
uname -a
cd /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE
date
echo "job: count_div"
echo $'python /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/ratio_site_gene_TE_500bp.py /vol3/agis/huangsanwen_group/luoxizhi/work/gene_525/gene_bin_500bp/193_Vitis_vinifera_gene_bin_500bp.xls /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_500bp_35/193_Vitis_vinifera_500bp_merge.xls /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/ratio_site_gene_TE_500bp/193_Vitis_vinifera_ratio_500bp_merge.xls'
python /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/ratio_site_gene_TE_500bp.py /vol3/agis/huangsanwen_group/luoxizhi/work/gene_525/gene_bin_500bp/193_Vitis_vinifera_gene_bin_500bp.xls /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_500bp_35/193_Vitis_vinifera_500bp_merge.xls /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/ratio_site_gene_TE_500bp/193_Vitis_vinifera_ratio_500bp_merge.xls
date
