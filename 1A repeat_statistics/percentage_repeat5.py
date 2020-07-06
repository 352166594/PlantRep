f = open('525_n50_gs.xls')
f1 = open('repeat_order_length.xls')
f2 = open('order_length_percentage_repeat.xls','w')
f3 = open('order_length_number_genome.xls','w')
f4 = open('order_length_percentage_genome.xls','w')
	
dic_gs = {}
list_gs = []
for lin0 in f:
	if "#species_name" in lin0:continue
	lis0 = lin0.strip().split('\t')
	dic_gs[lis0[0]] = lis0[1]
	
for lin in f1:
	lis=lin.strip().split('\t')
	if "Species" in lin:
		f2.write(lin.strip()+'\t'+'Total_repeat_percentage'+'\n')
		f3.write(lin.strip()+'\t'+'Total_repeat_length'+'\t'+'Genome_size_length'+'\n')
		f4.write(lin.strip()+'\t'+'Total_repeat_percentage'+'\t'+'Genome_size_percentage'+'\n')
	else:	
		lis=lin.strip().split('\t')
		f2.write(lis[0])
		f3.write(lis[0])
		f4.write(lis[0])
		Genome_size = int(dic_gs[lis[0]])
		
		percentage = 0
		lengths = 0
		for repeat in lis[1:]:
			gs_percentage=round(float(repeat) / Genome_size , 4)*100
			
			percentage = percentage + gs_percentage
			lengths = lengths + int(repeat)
			f3.write('\t' + str(repeat))
			f4.write('\t' + str(gs_percentage))
		f3.write('\t'+str(lengths)+'\t'+str(Genome_size)+'\n')
		#f4.write('\t'+str(percentage)+'%'+'\t'+"100%"+'\n')
		f4.write('\t'+str(percentage)+'\t'+"100"+'\n')
		
		for lens in lis[1:]:
			if lengths != 0:
				percentage = str(round(float(lens) / lengths , 4)*100)
			else:
				percentage = str(0)
			
			f2.write('\t' + percentage)
		f2.write('\t'+'100'+'\n')
