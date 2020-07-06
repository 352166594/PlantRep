for i in *_plot_whole_species_ratio_500bp_merge.xls
do
#	echo head -n 1  length_percentage_genome_plot_whole_species_ratio_500bp_merge.xls  \> Total_length_percentage_genome_order_r.xls
	#0Total_repeat_percentage
	echo head -n 1 $i \> Total_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
#	echo grep 'Total_repeat_percentage' length_percentage_genome_plot_whole_species_ratio_500bp_merge.xls \>\> Total_length_percentage_genome_order_r.xls
	echo grep 'Total' $i \>\> Total_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R  Total_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls	#Total_length_percentage_genome_order_r.xls
	
	#1DIRS
	echo head -n 1 $i \> DIRS_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'DIRS' $i \>\> DIRS_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R DIRS_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
	#2LINE
	echo head -n 1 $i \> LINE_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'LINE' $i \>\> LINE_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R LINE_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
	#3LTR
	echo head -n 1 $i \> LTR_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'LTR' $i \>\> LTR_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R LTR_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
	#4SINE
	echo head -n 1 $i \> SINE_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'SINE'  $i \>\> SINE_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R SINE_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
	#5Circular_dsDNA
	echo head -n 1 $i \> Circular_dsDNA_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'Circular_dsDNA'  $i \>\> Circular_dsDNA_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R Circular_dsDNA_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
	#6DNA_Polymerase
	echo head -n 1 $i \> DNA_Polymerase_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'DNA_Polymerase'  $i \>\> DNA_Polymerase_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R DNA_Polymerase_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
	#7Rolling_Circle
	echo head -n 1 $i \> Rolling_Circle_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'Rolling_Circle'  $i \>\> Rolling_Circle_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R  Rolling_Circle_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
	#8TIR
	echo head -n 1 $i \> TIR_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'TIR'  $i \>\> TIR_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R  TIR_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
	#9RNA
	echo head -n 1 $i \> RNA_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'RNA'  $i \>\> RNA_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R RNA_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
	#10Low_complexity
	echo head -n 1 $i \> Low_complexity_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'Low_complexity'  $i \>\> Low_complexity_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R Low_complexity_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
	#11Satellite
	echo head -n 1 $i \> Satellite_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'Satellite'  $i \>\> Satellite_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R Satellite_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
	#12Simple_repeat
	echo head -n 1 $i \> Simple_repeat_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'Simple_repeat'  $i \>\> Simple_repeat_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R Simple_repeat_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
	#13PLE
	echo head -n 1 $i \> PLE_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo grep 'PLE'  $i \>\> PLE_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	echo Rscript plot_gene_te_ratio.R PLE_$(basename ${i#*/} _plot_whole_species_ratio_500bp_merge.xls).xls
	
done > plot_command_0520
