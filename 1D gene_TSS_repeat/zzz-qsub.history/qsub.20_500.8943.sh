#!/bin/bash
#PBS -N 20_500
#PBS -o /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/zzz-qsub.history/qsub.20_500.8943.log
#PBS -e /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/zzz-qsub.history/qsub.20_500.8943.err
#PBS -q low
# qsub parameter: "-q queue1 -l nodes=1:ppn=1"
uname -a
cd /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE
date
echo "job: 20_500"
echo $'python /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_count_500bp_5gene3.py /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/5gene3_500/133_Oryza_rufipogon_500bp.xls /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_5gene3_500_merge/133_Oryza_rufipogon_500bp_merge.xls'
python /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_count_500bp_5gene3.py /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/5gene3_500/133_Oryza_rufipogon_500bp.xls /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_5gene3_500_merge/133_Oryza_rufipogon_500bp_merge.xls
date
