# coding=utf-8
import sys
import os
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
#list_dir_01 =sort_humanly(list_dir_00)
f1=open("merge_0611_gypsy_insert_time.xls")
f2=open("gypsy_percentage_species_count_insert_time_format.xls","w")
f3=open("gypsy_percentage_kindom_count_insert_time_format.xls","w")
dict_kindom={}
list_kindom=[]
numb_kindom={}
f2.write("Species_type\tSpecies_name\ttimes\tnumber\tNo\n")
for lin1 in f1:
	lis1=lin1.strip().split("\t")
	if "Species_type" in lin1:
		time_list= lis1[5:]
	else:
		#if int(lis1[2])<=30:continue
		if int(lis1[2])<=0:continue
		Species_name=lis1[1]+"_insert_time.xls"
#		os.chdir("/vol3/agis/huangsanwen_group/luoxizhi/work/525_harvast/species_percentage_insert_time")
		os.chdir("/vol3/agis/huangsanwen_group/luoxizhi/work/525_harvast/copia_gypsy/gypsy_species_percentage_insert_time")
		fout=open(Species_name,"w")
		fout.write("Species_type\ttimes\tnumber\tNo\n")
		for time in range(len(lis1[5:])):
			fout.write("{0}\t{1}\t{2}\t{3}\n".format(lis1[0],time_list[time],lis1[5:][time],time+1))
		fout.close()
		os.chdir("/vol3/agis/huangsanwen_group/luoxizhi/work/525_harvast/copia_gypsy/")
		for time in range(len(lis1[5:])):
			f2.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(lis1[0],lis1[1],time_list[time],lis1[5:][time],time+1))
		if lis1[0] not in dict_kindom:
			dict_kindom[lis1[0]]={}
			list_kindom.append(lis1[0])
			numb_kindom[lis1[0]]={}
		for time in range(len(lis1[5:])):
			if time_list[time] not in dict_kindom[lis1[0]]:
				dict_kindom[lis1[0]][time_list[time]]=0
				numb_kindom[lis1[0]][time_list[time]]=0
			dict_kindom[lis1[0]][time_list[time]]=dict_kindom[lis1[0]][time_list[time]]+float(lis1[5:][time])/float(lis1[2])
			numb_kindom[lis1[0]][time_list[time]]=numb_kindom[lis1[0]][time_list[time]]+1
			
#f3.write("Species_type\ttimes\tInterval\tnumber\tNo\n")
f3.write("Species_type\tInterval\tTemporal\tLTR_nummber\tFigure_order\n")
list_kindom =sort_humanly(list_kindom)
for type in list_kindom:
	for tim in range(len(time_list)):
		if "Million" in time_list[tim]:
			if int(time_list[tim].split("-")[0])>50:
				continue
			else:
				Interval=int(time_list[tim].split("-")[0])
				Figure_order= tim+1-49
				#f3.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(type,time_list[tim].split("-")[0],"Million",dict_kindom[type][time_list[tim]] ,tim+1))
				f3.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(type,Interval,"Million",dict_kindom[type][time_list[tim]]/numb_kindom[type][time_list[tim]] ,Figure_order))
		elif "Hundred_thousand" in time_list[tim]:
			Interval=int(time_list[tim].split("-")[0])
			Figure_order=tim+1-49
			f3.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(type,Interval,"Hundred_thousand",dict_kindom[type][time_list[tim]]/numb_kindom[type][time_list[tim]] ,Figure_order))
