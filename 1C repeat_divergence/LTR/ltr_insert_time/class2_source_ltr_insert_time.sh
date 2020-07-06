#gypsy
mkdir gypsy_mya2_insert_time
for i in done_525_harvast/*.fa.pass.list
do
	echo python insert_time_statistic_v7_0611_gypsy.py $i
done > 0611_ltr_insert_time_gypsy.command
sh 0611_ltr_insert_time_gypsy.command

cd gypsy_mya2_insert_time
head -n 1 85_Adiantum_capillus-veneris_gypsy_ltr_inserttime.xls > ../merge_0611_gypsy_insert_time.xls
cat *_ltr_inserttime.xls |grep -v 'Species' >> ../merge_0611_gypsy_insert_time.xls
cd ..
python total_gypsy_0611_stat_kindom_insert_time_species_max.py

###copia
mkdir copia_mya2_insert_time
for i in done_525_harvast/*.fa.pass.list
do
	echo python insert_time_statistic_v7_0611_copia.py $i
done > 0611_ltr_insert_time_copia.command
sh 0611_ltr_insert_time_copia.command


cd copia_mya2_insert_time
head -n 1 85_Adiantum_capillus-veneris_copia_ltr_inserttime.xls > ../merge_0611_copia_insert_time.xls
cat *_ltr_inserttime.xls |grep -v 'Species' >> ../merge_0611_copia_insert_time.xls
cd ..
python total_copia_0611_stat_kindom_insert_time_species_max.py
