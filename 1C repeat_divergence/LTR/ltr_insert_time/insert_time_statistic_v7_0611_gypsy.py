#!/usr/local/python
import os
import sys
import re
f1=open(sys.argv[1])
dir_now= os.getcwd()
time_u = 1
if ".fa.pass.list" in sys.argv[1]:
	if "/" in sys.argv[1]:
		species_whole_name = sys.argv[1].split("/")[-1].split(".fa.pass.list")[0]
	else:
		species_whole_name = sys.argv[1].split(".fa.pass.list")[0]
	species_number = int(species_whole_name.split("_")[0])
        if species_number >= 1 and species_number<=77:
                species_type = "01_Alage"
        elif species_number >= 78 and species_number<=81:
                species_type = "02_Bryophyte"			
        elif species_number >= 82 and species_number<=84:
                species_type = "03_Lycophytes"			
        elif species_number >= 85 and species_number<=87:
                species_type = "04_Fern"			#1.55186831293703E-09
        elif species_number >= 88 and species_number<=96:
                species_type = "05_Gymnosperms"			#2.2E-09
        elif species_number == 97 or species_number == 98:
                species_type = "06_ANA"				#1.8E-8	
        elif species_number >= 99 and species_number<=102:
                species_type = "07_Magnoliids"
        elif species_number >= 103 and species_number<=177:
                species_type = "08_Monocots"			#1.5E-8	2004	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC545599/
        elif species_number >= 178 and species_number <= 184:
                species_type = "09_Base_eudicots"		#1.3E10-8
        elif species_number >= 185 and species_number <= 194:
                species_type = "10_Super_rosids"
        elif species_number >= 195 and species_number <= 313:
                species_type = "11_Fabids"
        elif species_number >= 314 and species_number <= 417:
                species_type = "12_Malvids"			#1.3E10-8	2016	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4715297/
        elif species_number >= 418 and species_number <= 448:
                species_type = "13_Super_asterids"
        elif species_number >= 449 and species_number <= 510:
                species_type = "14_Lamiids"
        elif species_number >= 511 and species_number <=525:
                species_type = "15_Campanulids"

if species_type== "01_Alage" or species_type=="02_Bryophyte" or species_type=="03_Lycophytes" or species_type=="04_Fern":
	time_u = float(1.3E-8)/float(1.55186831293703E-09)
elif species_type== "05_Gymnosperms":
	time_u = float(1.3E-8)/float(2.2E-09)
elif species_type=="06_ANA" or  species_type=="07_Magnoliids":
	time_u = float(1.3E-8)/float(1.8E-08)
elif species_type=="08_Monocots":
	time_u = float(1.3E-8)/float(1.5E-08)
else:
	time_u=1

dir_out = "/vol3/agis/huangsanwen_group/luoxizhi/work/525_harvast/gypsy_mya2_insert_time/"
#dir_out = "/vol3/agis/huangsanwen_group/luoxizhi/work/525_harvast/count100_insert_time/"
os.chdir(dir_out)
#out_name = "/vol3/agis/huangsanwen_group/luoxizhi/work/525_harvast/count_insert_time/"
#out_name =species_whole_name+"_"+species_type+"_ltr_inserttime.xls"
out_name =species_whole_name+"_gypsy_ltr_inserttime.xls"
f2=open(out_name,"w")

num=0

num10000_dict = {}
num_dict = {}
num100_dict = {}
num10_dict = {}

total_num = 0
Ten_thousand_num = 0
Hundred_thousand_num = 0
Million_num = 0
Ten_million_num = 0
num_near = 0
num_before = 0

for line1 in f1:
        if '#' in line1:continue
        list1=line1.strip().split()
	if "Gypsy" not in list1[-3]:continue
	if list1[-1] == "NA":continue
	if int(list1[-1]) == int(0):continue
	total_num = total_num+1
#	species_type
        for i in range(1,100):
		#num10_dict	Ten thousand
                if 10000*i <= float(list1[-1])*time_u < 10000* (i + 1):
			Ten_thousand_num = Ten_thousand_num+1
                        key = str(i) + 'Ten_thousand'
                        if key not in num10_dict:
                                num10_dict[key] = 1
                        elif key in num10_dict:
                                num10_dict[key] = num10_dict[key] + 1
				
		#num100_dict	One hundred thousand
                elif 100000*i <= float(list1[-1])*time_u < 100000* (i + 1):
                        key = str(i) + 'Hundred_thousand'
			Hundred_thousand_num=Hundred_thousand_num+1
                        if key not in num100_dict:
                                num100_dict[key] = 1
                        elif key in num100_dict:
                                num100_dict[key] = num100_dict[key] + 1
		
		#num_dict	mya
                elif 1000000*i <= float(list1[-1])*time_u < 1000000* (i + 1):
                        key = str(i) + 'Million'
			Million_num=Million_num+1
                        if key not in num_dict:
                                num_dict[key] = 1
                        elif key in num_dict:
                                num_dict[key] = num_dict[key] + 1
		

#f2.write("Species_type\tSpecies_whole_name\ttotal_number\tMillion_num\tHundred_thousand_num\tTen_thousand_num")	#\t1-10Million\t")
f2.write("Species_type\tSpecies_whole_name\ttotal_number\tMillion_num\tHundred_thousand_num")
for n in range(200,0,-1):
#	if 1<=n<100:
#		f2.write("\t"+str(n)+"-"+str(n+1)+ 'Ten_thousand')
	if 1<=n<100:
		f2.write("\t"+str(n)+"-"+str(n+1)+ 'Hundred_thousand')
	if 101<=n<200:
		f2.write("\t"+str(n-100)+"-"+str(n+1-100)+ 'Million')
f2.write("\n")

f2.write(species_type+"\t"+species_whole_name)
f2.write("\t{0}\t{1}\t{2}".format(total_num,Million_num,Hundred_thousand_num))


	
for j in range(99,0,-1):
        key000 = str(j) + 'Million'
        if key000 in num_dict:
		f2.write("\t"+str(num_dict[key000]))
        elif key000 not in num_dict:
		f2.write("\t"+ '0')
	
for j in range(99,0,-1):
        key00 = str(j) + 'Hundred_thousand'
        if key00 in num100_dict:
		f2.write("\t"+str(num100_dict[key00]))
        elif key00 not in num100_dict:
		f2.write("\t"+ '0')

	
f2.write("\n")
f1.close()
f2.close()
os.chdir(dir_now)
