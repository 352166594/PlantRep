mkdir 20_5start_500_merge
mkdir 20_5gene3_500_merge
mkdir 20_3gene5_500_merge
mkdir 20_3end_500_merge

mkdir 20_3gene5_500_merge
for i in 5start_500/*_500bp.xls
do
	echo python `pwd`/20_count_500bp_5start.py `pwd`/5start_500/$(basename ${i#*/}) `pwd`/20_5start_500_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls
	echo python `pwd`/20_count_500bp_5gene3.py `pwd`/5gene3_500/$(basename ${i#*/}) `pwd`/20_5gene3_500_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls
	echo python `pwd`/20_s3_count_500bp_3gene5.py `pwd`/3gene5_500/$(basename ${i#*/}) `pwd`/20_3gene5_500_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls
	echo python `pwd`/20_count_500bp_3end.py  `pwd`/3end_500/$(basename ${i#*/}) `pwd`/20_3end_500_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls
#	echo cat `pwd`/5start_500_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls `pwd`/5gene3_500_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls `pwd`/3end_500_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls \> `pwd`/500bp_53/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls
done > 20_3start_500bp_merge.command

cat 20_3start_500bp_merge.command |xargs -i quick_qsub =20_500= {-q queue5  -l nodes=1:ppn=1}   {}

mkdir 20_500bp_35
for i in 5start_500/*_500bp.xls
do
	echo cat `pwd`/20_5start_500_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls `pwd`/20_5gene3_500_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls `pwd`/20_3gene5_500_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls `pwd`/20_3end_500_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls \> `pwd`/20_500bp_35/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls
done > 20_cat.command


###############
#mkdir 5gene3_500_merge
#for i in 5gene3_500/*_500bp.xls
#do
#	echo python `pwd`/count_500bp.py `pwd`/5gene3_500/$(basename ${i#*/}) `pwd`/5gene3_500_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls
#done > 5gene3_500_merge.command
#cat 5gene3_500_merge.command |xargs -i quick_qsub =jobname= {-q low  -l nodes=1:ppn=1}   {}

#mkdir 3end_500b_merge
#for i in 3end_500bp/*_500bp.xls
#do
#	echo python `pwd`/count_500bp.py `pwd`/3end_500bp/$(basename ${i#*/}) `pwd`/3end_500bp_merge/$(basename ${i#*/} _500bp.xls)_500bp_merge.xls
#done > 3end_500bp_merge.command
#cat 3end_500bp_merge.command |xargs -i quick_qsub =jobname= {-q low  -l nodes=1:ppn=1}   {}
#######
