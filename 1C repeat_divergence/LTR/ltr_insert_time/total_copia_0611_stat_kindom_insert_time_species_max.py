f1=open("merge_0611_copia_insert_time.xls")
#f1=open("merge_0317_count_insert_time.xls")
#f1=open("merge_0317_72_count_insert_time.xls")
f2=open("0611_copia_max_ltr_inserttime.xls","w")
f3=open("total_copia_count_max_ltr_inserttime.xls","w")

dic = {}
list_Interval= []
list_Species = []
for lin in f1:
	lis=lin.strip().split("\t")
	if "Species_type" in lin:
#		f2.write("Interval\tTemporal\tLTR_nummber\tFigure_order\tSpecies_type\n")
		#1-2       Ten_thousand      1            1             07_Magnoliids
#		for i in lis[5:]:
#			list_Interval.append(i)
		list_Interval=lis[5:]
	else:
		Species_type = lis[0]
		total = "total"
		if Species_type not in dic:
			dic[Species_type] = {}
			list_Species.append(Species_type)
#			total_stat = "total"
#			dic[total_stat] = {}
		if total  not in dic:
			dic[total] = {}
				
		time_lis = lis[5:]
		time_type = list_Interval[time_lis.index(max(time_lis))]
#		for j in range(len(time_lis)):
#			time_type = list_Interval[j]
		if time_type not in dic[Species_type]:
			dic[Species_type][time_type] = 1#max(time_lis)#time_lis[time_type]
		elif time_type in dic[Species_type]:
			dic[Species_type][time_type] = dic[Species_type][time_type] + 1#max(time_lis)#time_lis[time_type]
			
		if time_type not in dic[total]:
			dic[total][time_type] = 1
		elif time_type in dic[total]:
			dic[total][time_type] = dic[total][time_type] + 1
			
			
f2.write("Interval\tTemporal\tLTR_nummber\tFigure_order\tSpecies_type\n")
for n in list_Species:
#	if n == '01_Alage':
#		print(n)
#	file_name = n+"_max_ltr_inserttime.xls"
#	fn=open(file_name,"w")
	#f2.write("Interval\tTemporal\tLTR_nummber\tFigure_order\tSpecies_type\n")
#	fn.write("Interval\tTemporal\tLTR_nummber\tFigure_order\tSpecies_type\n")
	for m in range(len(list_Interval)):
		if "Million" in list_Interval[m]:
			Interval=list_Interval[m].split("Million")[0]
			Temporal="Million"
		elif "Hundred_thousand" in list_Interval[m]:
			Interval=list_Interval[m].split("Hundred_thousand")[0]
			Temporal="Hundred_thousand"
#		elif "Ten_thousand" in list_Interval[m]:
#			Interval=list_Interval[m].split("Ten_thousand")[0]
#			Temporal="Ten_thousand"
		if list_Interval[m] in dic[n]:
			LTR_nummber=dic[n][list_Interval[m]]
		else:
			LTR_nummber=0
		Figure_order = m+1
		Species_type = n
		Interval= Interval.split("-")[1]
		f2.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(Interval,Temporal,LTR_nummber,Figure_order,Species_type))
#		fn.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(Interval,Temporal,LTR_nummber,Figure_order,Species_type))
	#fn.close()
	
f3.write("Interval\tTemporal\tLTR_nummber\tFigure_order\tSpecies_type\n")
#for m in range(len(list_Interval)):
for m in range(len(list_Interval)):
	if "Million" in list_Interval[m]:
		Interval=list_Interval[m].split("Million")[0]
		Temporal="Million"
	elif "Hundred_thousand" in list_Interval[m]:
		Interval=list_Interval[m].split("Hundred_thousand")[0]
		Temporal="Hundred_thousand"
	elif "Ten_thousand" in list_Interval[m]:
		Interval=list_Interval[m].split("Ten_thousand")[0]
		Temporal="Ten_thousand"
	if list_Interval[m] in dic[total]:
		LTR_nummber=dic[total][list_Interval[m]]
	else:
		LTR_nummber=0
	Figure_order = m+1
	Species_type = n
	Interval= Interval.split("-")[0]
	if Figure_order <50:
		continue
	else:
		Figure_order=Figure_order-49
	
		
	f3.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(Interval,Temporal,LTR_nummber,Figure_order,"whole_species"))

	
	
