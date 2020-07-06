# coding=utf-8
import sys
import os
list_dir_00 = os.listdir(".")
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

list_dir_01 =sort_humanly(list_dir_00)

list_species_name = []
div_dict_name = {}

repeat_type = {}
div_list_name = []
list_name = []
for i in list_dir_01:
	if ".py" in i or ".sh" in i:continue
	if ".txt" in i:
		species_name=i.split(".txt")[0]
		list_species_name.append(species_name)
		div_dict_name[species_name] = {}
		f1 = open(i)
		for lin1 in f1:
			lis1 = lin1.strip().split("\t")
			if "Order" in lis1[0]:
				div_list_name = lis1[1:]
			else:
				repeat_name = lis1[0]
				if repeat_name not in div_dict_name[species_name]:	#repeat_type:
					div_dict_name[species_name][repeat_name] = {}
	                	for i in range(len(lis1[1:])):
					div_dict_name[species_name][repeat_name][div_list_name[i]]= lis1[1:][i]

#ClassI:LTR	ClassI:LINE	ClassI:SINE	ClassII:Rolling_Circle		ClassII:TIR 

fout=open("div_clade.xls","w")
fout2=open("div_species.xls","w")
		
repeat_list=["ClassI:LTR","ClassI:LINE","ClassI:SINE","ClassII:Rolling_Circle","ClassII:TIR"]
fout.write("Species_type\tSpecies\tRepeat_type\tDivergence\tPercetage\n")
div_list=[]
for i in range(0,50):
        div=str(i)+"-"+str(i+1)
        div_list.append(div)

dict_kindom={}
dict_number={}
list_kindom=[]
	
for species in list_species_name:
        species_number = int(species.split("_")[0])
	
        if species_number >= 3 and species_number<=77:
                species_type = "01_Alage"
        elif species_number >= 78 and species_number<=81:
                species_type = "02_Bryophyte"
        elif species_number >= 82 and species_number<=84:
                species_type = "03_Lycophytes"
        elif species_number >= 85 and species_number<=87:
                species_type = "04_Fern"
        elif species_number >= 88 and species_number<=96:
                species_type = "05_Gymnosperms"
        elif species_number == 97 or species_number == 98:
                species_type = "06_ANA"
        elif species_number >= 99 and species_number<=102:
                species_type = "07_Magnoliids"
        elif species_number >= 103 and species_number<=177:
                species_type = "08_Monocots"
        elif species_number >= 178 and species_number <= 184:
                species_type = "09_Base_eudicots"
        elif species_number >= 185 and species_number <= 194:
                species_type = "10_Super_rosids"
        elif species_number >= 195 and species_number <= 313:
                species_type = "11_Fabids"
        elif species_number >= 314 and species_number <= 417:
                species_type = "12_Malvids"
        elif species_number >= 418 and species_number <= 448:
                species_type = "13_Super_asterids"
        elif species_number >= 449 and species_number <= 510:
               species_type =  "14_Lamiids"
        elif species_number >= 511 and species_number <=525:
                species_type = "15_Campanulids"
	
	if species_type not in dict_kindom:
		dict_kindom[species_type] = {}
		dict_number[species_type] = {}
		
		list_kindom.append(species_type)
#fout.write("Species_type\tSpecies\tRepeat_type\tDivergence\tPercetage\n"
#div_dict_name[species_name][repeat_name][div_list_name[i]]= lis1[i]
	for repeat in repeat_list:
		if repeat not in dict_kindom[species_type]:
			dict_kindom[species_type][repeat]={}
			dict_number[species_type][repeat]={}
			
		if repeat in div_dict_name[species]:
			for dive in div_list:
				if dive not in dict_kindom[species_type][repeat]:
					dict_kindom[species_type][repeat][dive] = float(0)
					dict_number[species_type][repeat][dive] = 0
				#	e#		
				if  dive in div_dict_name[species][repeat]:
					fout.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(species_type,species,repeat,dive,div_dict_name[species][repeat][dive]))
					dict_kindom[species_type][repeat][dive] =dict_kindom[species_type][repeat][dive]+float(div_dict_name[species][repeat][dive])
					dict_number[species_type][repeat][dive] =dict_number[species_type][repeat][dive]+1
				else:
					fout.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(species_type,species,repeat,dive,0))
					dict_kindom[species_type][repeat][dive] = dict_kindom[species_type][repeat][dive]+0
					dict_number[species_type][repeat][dive] = dict_number[species_type][repeat][dive]+1
		else:
			for dive in div_list:
				if dive not in dict_kindom[species_type][repeat]:
					dict_kindom[species_type][repeat][dive] = 0
					dict_number[species_type][repeat][dive] = 0
				dict_kindom[species_type][repeat][dive] = dict_kindom[species_type][repeat][dive]+0
				dict_number[species_type][repeat][dive] =dict_number[species_type][repeat][dive] +0
				fout.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(species_type,species,repeat,dive,0))
				
fout2.write("Species_type\tRepeat_type\tDivergence\tPercetage\n")
for type in list_kindom:	#list_species_name:
        for repeat in repeat_list:
		if repeat in dict_kindom[type]:
			for dive in div_list:
				div_num=dive.split("-")[1]
				if dive in dict_kindom[type][repeat]:
#					fout2.write("{0}\t{1}\t{2}\t{3}\n".format(species_type,dive,dict_kindom[type][repeat][dive]))
					fout2.write("{0}\t{1}\t{2}\t{3}\n".format(type,repeat,div_num,  round(dict_kindom[type][repeat][dive]/float(dict_number[type][repeat][dive]),4) ))
				else:
					fout2.write("{0}\t{1}\t{2}\t{3}\n".format(type,repeat,div_num,0))
		else:	
			for dive in div_list:
				div_num=dive.split("-")[1]
				fout2.write("{0}\t{1}\t{2}\t{3}\n".format(type,repeat,div_num,0))
