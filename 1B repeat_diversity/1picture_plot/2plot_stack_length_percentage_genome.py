import sys
#f1=open("length_in_genome_order_r.txt")
#f2=open("StackedColumn_length_percentage_genome.xls","w")
f1=open(sys.argv[1])
f2=open(sys.argv[2],"w")

dict_repeat={}
num_repeat={}
list_repeat=[]
list_type=[]
for lin in f1:
        if "Species_type" in lin:continue
        lis=lin.strip().split("\t")
        Species_type = lis[0]
        Order= lis[2]
        if Order not in dict_repeat:
                dict_repeat[Order]={}
                num_repeat[Order]={}
                list_repeat.append(Order)
        if Species_type not in list_type:
                list_type.append(Species_type)
        
        if Species_type not in dict_repeat[Order]:
                dict_repeat[Order][Species_type] = float(lis[3])
                num_repeat[Order][Species_type] = 1
        elif Species_type in dict_repeat[Order]:
                dict_repeat[Order][Species_type] = dict_repeat[Order][Species_type]+float(lis[3])
                num_repeat[Order][Species_type] =num_repeat[Order][Species_type] +1


list_type.reverse()
f2.write("Clarity")
for type in list_type:
	f2.write("\t"+"_".join(type.split("_")[1:]))
f2.write("\n")
	
for repeat in list_repeat:
	f2.write(repeat)
	for type in list_type:
		whole_ratio = dict_repeat[repeat][type]
		whole_num= num_repeat[repeat][type]
		f2.write("\t"+str(round(whole_ratio/whole_num,4)))	
	f2.write("\n")
