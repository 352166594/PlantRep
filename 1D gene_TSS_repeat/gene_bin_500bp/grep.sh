mkdir name_30000
for i in *_gene_bin_500bp.xls
do
	echo grep '29500-30000bp' $i \> ./name_30000/$(basename ${i#*/} _gene_bin_500bp.xls).xls
done>gerp.command
