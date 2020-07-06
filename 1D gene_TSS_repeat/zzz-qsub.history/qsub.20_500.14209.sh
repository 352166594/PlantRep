#!/bin/bash
#PBS -N 20_500
#PBS -o /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/zzz-qsub.history/qsub.20_500.14209.log
#PBS -e /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/zzz-qsub.history/qsub.20_500.14209.err
#PBS -q low
# qsub parameter: "-q queue1 -l nodes=1:ppn=1"
uname -a
cd /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE
date
echo "job: 20_500"
echo $'python /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_s3_count_500bp_3gene5.py /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/3gene5_500/97_Amborella_trichopoda_500bp.xls /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_3gene5_500_merge/97_Amborella_trichopoda_500bp_merge.xls'
python /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_s3_count_500bp_3gene5.py /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/3gene5_500/97_Amborella_trichopoda_500bp.xls /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_3gene5_500_merge/97_Amborella_trichopoda_500bp_merge.xls
date
