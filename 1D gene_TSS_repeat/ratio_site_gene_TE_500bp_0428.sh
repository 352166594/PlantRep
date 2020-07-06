#python ratio_site_gene_TE_500bp.py /vol3/agis/huangsanwen_group/luoxizhi/work/gene_525/gene_bin_500bp/104_Zostera_marina_gene_bin_500bp.xls /vol3/agis/huangsanwen_group/luoxizhi/work/gene_525/site_gene_TE_500bp/20_500bp_35/104_Zostera_marina_500bp_merge.xls  /vol3/agis/huangsanwen_group/luoxizhi/work/gene_525/ratio_site_gene_TE_500bp/104_Zostera_marina_ratio_500bp_merge.xls

#for i in /vol3/agis/huangsanwen_group/luoxizhi/work/gene_525/site_gene_TE_500bp/20_500bp_35/*_500bp_merge.xls
mkdir ratio_site_gene_TE_500bp

for i in /vol3/agis/zhangxinyan_group/zhangxinyan/luoxizhi/80_class2_gene_site_TE/20_500bp_35/*_500bp_merge.xls

do
	echo python  `pwd`/ratio_site_gene_TE_500bp.py /vol3/agis/huangsanwen_group/luoxizhi/work/gene_525/gene_bin_500bp/$(basename ${i#*/} _500bp_merge.xls)_gene_bin_500bp.xls $i `pwd`/ratio_site_gene_TE_500bp/$(basename ${i#*/} _500bp_merge.xls)_ratio_500bp_merge.xls
done > ratio_site_gene_TE_500bp.command_0428

