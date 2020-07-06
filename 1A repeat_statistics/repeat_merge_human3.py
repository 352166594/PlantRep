# coding=utf-8
import sys
import os
list_dir_01 = os.listdir(".")
fout = open("repeat_order_length.xls","w")
fout2 = open("repeat_order_number.xls","w")
fout3 = open("repeat_order_average_length.xls","w")

list_dir_01.sort()

list_species_name = []
repeat_dict_name = {}

repeat_type = {}
repeat_list_name = []
list_name = []
#fout.write("#species_id")
for i in list_dir_01:
	if "gather_repeat" in i:continue
	if ".py" in i or ".sh" in i or ".R" in i or ".csv" in i or ".xls" in i or ".png" in i:continue
	if ".txt" in i:
#		fout.write("\t" + i.split('.xls')[0]#.split("_RRAS")[0])
		species_name = i.split('.txt')[0].split('_')[0] +" "+ i.split('.txt')[0]#.split('_')[1:])
#		print species_name
		list_species_name.append(species_name)
		
		repeat_dict_name[species_name] = {}
		f1 = open(i)
		for line in f1:
			repeat_name = line.strip().split('\t')[0]# + '|' + line.strip().split('\t')[1]
			if "Simple_repeat" in repeat_name:
				repeat_name = "Tandem_Repeat:Simple_repeat"
			elif "Satellite" in repeat_name:
				repeat_name = "Tandem_Repeat:Satellite"
			elif "Low_complexity" in repeat_name:
				repeat_name = "Tandem_Repeat:Low_complexity"
			elif "Retroposon" in repeat_name:
				repeat_name = "ClassI:unknown"
					
#			if r'?' in repeat_name:
#				repeat_name = repeat_name.split(r'?')[0]
#			
#			if "ARTEFACT" == repeat_name or "RC" == repeat_name or "rRNA" == repeat_name or "snRNA" == repeat_name:
#				repeat_name ="Other"
				
			repeat_length = line.strip().split('\t')[1]
			#print repeat_length
			repeat_number = line.strip().split('\t')[2]
			#print repeat_number
			repeat_avelen = line.strip().split('\t')[3]
				
#			repeat_dict_name[species_name] = {}
			if repeat_name not in repeat_dict_name[species_name]:
				if repeat_name not in repeat_type:
					repeat_list_name.append(repeat_name)
					repeat_type[repeat_name] = ''
					
#				repeat_dict_name[species_name] = {}#[repeat_name] = {}
				repeat_dict_name[species_name][repeat_name] = str(repeat_length)+"|"+str(repeat_number)+"|"+str(repeat_avelen)
				#print repeat_dict_name[species_name][repeat_name]	
				#repeat_dict_name[species_name][repeat_name] = "{0}\t{1}\t{2}".format(repeat_length,repeat_number,repeat_avelen)
			elif repeat_name in repeat_dict_name[species_name]:
				repeat_dict_name[species_name][repeat_name] = str(repeat_length)+"|"+str(repeat_number)+"|"+str(repeat_avelen)
repeat_list_name.sort()
print(repeat_list_name)

#https://nedbatchelder.com/blog/200712/human_sorting.html
import re
def tryint(s):#                       //将元素中的数字转换为int后再排序
    try:
        return int(s)
    except ValueError:
        return s
def str2int(v_str):#                //将元素中的字符串和数字分割开
    return [tryint(sub_str) for sub_str in re.split('([0-9]+)', v_str)]
def sort_humanly(v_list):#    //以分割后的list为单位进行排序
    return sorted(v_list, key=str2int)

list_species_name =sort_humanly(list_species_name)

fout.write("Species")
for repeat in repeat_list_name:
	fout.write("\t"+repeat)
fout.write("\n")

fout2.write("Species")
for repeat in repeat_list_name:
	fout2.write("\t"+repeat)
fout2.write("\n")

fout3.write("Species")
for repeat in repeat_list_name:
	fout3.write("\t"+repeat)
fout3.write("\n")

for species in list_species_name:
	fout.write(species.split(" ")[1])#+"_"+species.split(" ")[1])
	fout2.write(species.split(" ")[1])#+"_"+species.split(" ")[1])
	fout3.write(species.split(" ")[1])#+"_"+species.split(" ")[1])
	for repeat in repeat_list_name:
		if repeat in repeat_dict_name[species]:
			#print repeat_dict_name[species][repeat]
			length = repeat_dict_name[species][repeat].split('|')[0]
			number = repeat_dict_name[species][repeat].split('|')[1]
			avelen = repeat_dict_name[species][repeat].split('|')[2]
		elif repeat not in repeat_dict_name[species]:
			#repeat_dict_name[species][repeat] = 0
			length = 0
			number = 0
			avelen = 0
		fout.write("\t"+str(length))
		fout2.write("\t"+str(number))
		fout3.write("\t"+str(avelen))
	fout3.write("\n")
	fout2.write("\n")
	fout.write("\n")
