for i in *_super_family_r.txt
do
#	echo head -n 1  length_percentage_genome_super_family_r.txt  \> Total_length_percentage_genome_super_family_r.xls
	#0Total_repeat_percentage
	echo head -n 1 $i \> Total_$(basename ${i#*/} _super_family_r.txt).xls
#	echo grep 'Total_repeat_percentage' length_percentage_genome_super_family_r.txt \>\> Total_length_percentage_genome_super_family_r.xls
	echo grep 'Total' $i \>\> Total_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R  Total_$(basename ${i#*/} _super_family_r.txt).xls	#Total_length_percentage_genome_super_family_r.xls
	
	#1DIRS
	echo head -n 1 $i \> DIRS_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'DIRS' $i \>\> DIRS_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R DIRS_$(basename ${i#*/} _super_family_r.txt).xls
	
	#2LINE
	echo head -n 1 $i \> LINE_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'LINE' $i \>\> LINE_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R LINE_$(basename ${i#*/} _super_family_r.txt).xls
	
	#3LTR
	echo head -n 1 $i \> LTR_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'LTR' $i \>\> LTR_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R LTR_$(basename ${i#*/} _super_family_r.txt).xls
	
	#4SINE
	echo head -n 1 $i \> SINE_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'SINE'  $i \>\> SINE_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R SINE_$(basename ${i#*/} _super_family_r.txt).xls
	
	#5Circular_dsDNA
	echo head -n 1 $i \> Circular_dsDNA_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'Circular_dsDNA'  $i \>\> Circular_dsDNA_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R Circular_dsDNA_$(basename ${i#*/} _super_family_r.txt).xls
	
	#6DNA_Polymerase
	echo head -n 1 $i \> DNA_Polymerase_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'DNA_Polymerase'  $i \>\> DNA_Polymerase_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R DNA_Polymerase_$(basename ${i#*/} _super_family_r.txt).xls
	
	#7Rolling_Circle
	echo head -n 1 $i \> Rolling_Circle_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'Rolling_Circle'  $i \>\> Rolling_Circle_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R  Rolling_Circle_$(basename ${i#*/} _super_family_r.txt).xls
	
	#8TIR
	echo head -n 1 $i \> TIR_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'TIR'  $i \>\> TIR_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R  TIR_$(basename ${i#*/} _super_family_r.txt).xls
	
	#9RNA
	echo head -n 1 $i \> RNA_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'RNA'  $i \>\> RNA_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R RNA_$(basename ${i#*/} _super_family_r.txt).xls
	
	#10Low_complexity
	echo head -n 1 $i \> Low_complexity_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'Low_complexity'  $i \>\> Low_complexity_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R Low_complexity_$(basename ${i#*/} _super_family_r.txt).xls
	
	#11Satellite
	echo head -n 1 $i \> Satellite_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'Satellite'  $i \>\> Satellite_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R Satellite_$(basename ${i#*/} _super_family_r.txt).xls
	
	#12Simple_repeat
	echo head -n 1 $i \> Simple_repeat_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'Simple_repeat'  $i \>\> Simple_repeat_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R Simple_repeat_$(basename ${i#*/} _super_family_r.txt).xls
	
	#13PLE
	echo head -n 1 $i \> PLE_$(basename ${i#*/} _super_family_r.txt).xls
	echo grep 'PLE'  $i \>\> PLE_$(basename ${i#*/} _super_family_r.txt).xls
	echo Rscript plot_stack.R PLE_$(basename ${i#*/} _super_family_r.txt).xls
	
	
done > plot_command_0521
