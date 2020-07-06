#!/bin/bash
#PBS -N 20_500
#PBS -o /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/zzz-qsub.history/qsub.20_500.11349.log
#PBS -e /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/zzz-qsub.history/qsub.20_500.11349.err
#PBS -q low
# qsub parameter: "-q queue1 -l nodes=1:ppn=1"
uname -a
cd /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE
date
echo "job: 20_500"
echo $'python /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_count_500bp_3end.py /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/3end_500/55_Chlorella_variabilis_500bp.xls /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_3end_500_merge/55_Chlorella_variabilis_500bp_merge.xls'
python /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_count_500bp_3end.py /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/3end_500/55_Chlorella_variabilis_500bp.xls /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_3end_500_merge/55_Chlorella_variabilis_500bp_merge.xls
date