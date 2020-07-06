f1=open("length_percentage_repeat_order_r.txt")
f2=open("3StackedColumn_length_percentage_repeat.xls","w")

dict_repeat={}
num_repeat={}
list_repeat=[]
list_type=[]
for lin in f1:
        if "Species_type" in lin:continue
	if "Total_repeat_percentage" in lin or "Genome_size_percentage" in lin:continue
        lis=lin.strip().split("\t")
        Species_type = lis[0]
        Order= lis[2]
        if "Species_type" in lin:continue
        lis=lin.strip().split("\t")
        Species_type = lis[0]
        Order= lis[2]
        #Stat=lis[3]
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
                
f2.write("Clarity")
for repeat in list_repeat:
        f2.write("\t"+repeat)
f2.write("\n")

for type in list_type:
        f2.write(type)
        for repeat in list_repeat:
                whole_ratio = dict_repeat[repeat][type]
                whole_num= num_repeat[repeat][type]
                f2.write("\t"+str(round(whole_ratio/whole_num,4)))
        f2.write("\n")
