py repeat_merge_human3.py
py percentage_order_r.peat5.py
py percentage_order_r.peat428.py

python type_family520.py repeat_order_number.xls kindom_order_number.xls
python type_family520.py repeat_order_average_length.xls kindom_order_average_length.xls
python type_family520.py order_number_percentage.xls kindom_order_number_percentage.xls
python type_family520.py order_length_percentage_repeat.xls kindom_order_length_percentage_repeat.xls
python type_family520.py order_length_percentage_genome.xls kindom_order_length_percentage_genome.xls
python type_family520.py order_length_number_genome.xls kindom_order_length_genome.xls

cp kindom_order_* picture_plot
cd picture_plot

python r_format_sys.py kindom_order_number.xls number_order_r.txt
python r_format_sys.py kindom_order_average_length.xls average_length_order_r.txt
python r_format_sys.py kindom_order_number_percentage.xls number_percentage_order_r.txt
python r_format_sys.py kindom_order_length_percentage_repeat.xls length_in_repeat_order_r.txt
python r_format_sys.py kindom_order_length_percentage_genome.xls length_in_genome_order_r.txt
python r_format_sys.py kindom_order_length_genome.xls length_order_r.txt

#plot2.R
sh type_plot_yunyutu.sh
sh plot_command_0520
sh mv_work.sh
sh mv_type.sh
rm *.xls
