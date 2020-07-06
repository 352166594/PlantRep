# coding=utf-8
import sys
import os
list_dir_01 = os.listdir(".")

#fout = open("LTR_div.xls","w")#
#fout2 = open("Low_complexity_div.xls","w")
##fout3 = open("TIR_div.xls","w")
#fout4 = open("Simple_repeat_div.xls","w")
#fout5 = open("Rolling_Circle_div.xls","w")
#fout6 = open("DNA_Polymerase_div.xls","w")
#fout7 = open("LINE_div.xls","w")
#fout8 = open("SINE_div.xls","w")
#fout9 = open("Satellite_div.xls","w")
#fout10 = open("RNA_div.xls","w")
#fout11 = open("DIRS_div.xls","w")

list_dir_01.sort()

list_species_name = []
repeat_dict_name = {}
repeat_type = {}
repeat_list_name = []
list_name = []

for i in list_dir_01:
        if "gather_repeat" in i:continue
        if ".py" in i or ".sh" in i:continue
        if ".txt" in i:
#                species_name = i.split('.txt')[0].split('_')[0] +" "+ i.split('.txt')[0]#.split('_')[1:])
		species_name=i.split('.txt')[0]
		list_species_name.append(species_name)
		repeat_dict_name[species_name] = {}
		f1 = open(i)
		for line in f1:
			repeat_name = line.strip().split('\t')[0]
			lis = line.strip().split('\t')
#			for i in range(0,50):
#				div=str(i)+"-"+str(i+1)
			if "Order" in repeat_name:
				div_list=lis[1:]
			else:		
				if ":" in line:
					name=repeat_name.split(':')[1]
				elif "Retroposon" in line:continue
				#	name="Retroposon"
				else:
					name=repeat_name
				if name not in repeat_list_name:
					repeat_list_name.append(name)
				repeat_dict_name[species_name][name] = {}
				for j in range(len(lis[1:])):
					repeat_dict_name[species_name][name][div_list[j]]=lis[1:][j]
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

list_species_name=sort_humanly(list_species_name)
repeat_list_name=sort_humanly(repeat_list_name)

div_list=[]					
for i in range(0,50):
	div=str(i)+"-"+str(i+1)
	div_list.append(div)
for repeat in repeat_list_name:
	out_name=repeat+"_div_order.xls"
	fout=open(out_name,"w")
	fout.write("Species")
	for dive in div_list:
		fout.write("\t"+dive)
	fout.write("\n")
	
	for species in list_species_name:
		fout.write(species)
		if repeat in repeat_dict_name[species]:
			for dive in div_list:
				if dive in repeat_dict_name[species][repeat]:#[div_list[j]]
					fout.write("\t"+repeat_dict_name[species][repeat][dive])
				else:
					fout.write("\t"+str(0))
			fout.write("\n")	
		else:
			for dive in div_list:
				fout.write("\t"+str(0))
			fout.write("\n")
