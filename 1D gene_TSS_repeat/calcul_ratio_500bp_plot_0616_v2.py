# coding=utf-8
import sys

f1=open('whole_species_ratio_500bp_merge.xls')
f2=open('supplement_whole_species_ratio_500bp_merge.xls','w')

dict_te = {}
list_site_bin = []
list_TE_type=[]
dict_number={}
for lin1 in f1:
	lis1=lin1.strip().split("\t")
	if "TE_type" in lin1:continue
	if "no_TE_in_scaffold" in lin1:continue #or "Unknown" in lin1 or "Others" in lin1:continue
	#TE_type = lis1[0]
	TE_type=lis1[0]
	
	if "Simple_repeat" in TE_type:
                TE_type = TE_type
        elif "Low_complexity" in TE_type:
                TE_type = TE_type
        elif "RC" in TE_type or "Helitron" in TE_type:
                TE_type = "Rolling_Circle-Helitron"
        elif "Penelope" in TE_type:
                TE_type = "PLE-Penelope"

        elif "DNA" in TE_type:
                if "/" in TE_type:
                        super_family=TE_type.split('/')[1]
                elif "?" in TE_type:
                        super_family="like"
                elif "/" not in TE_type and "?" not in TE_type:
                        super_family="unknown"
                if "-" in super_family:
                        super_family = super_family.split('-')[0]
#               if "Crypton" in super_family or "Helitron" in super_family or "Maverick" in super_family:
#                       TE_type = ""+super_family
                if "Crypton" in super_family:
                        TE_type = "Circular_dsDNA-Crypton"
                elif "Maverick" in super_family:
                        TE_type = "DNA_Polymerase-Maverick"
                else:
                        TE_type = "TIR-"+super_family
#       elif "rRNA" in TE_type:


        elif "SINE" in TE_type:
                if "/" in TE_type:
                        super_family=TE_type.split('/')[1]
                elif "?" in TE_type:
                        super_family="like"
                elif "/" not in TE_type and "?" not in TE_type:
                        super_family="unknown"
                if "-" in super_family:
                        super_family = super_family.split('-')[0]
                TE_type = "SINE-"+super_family


        elif "LINE" in TE_type:
                if "/" in TE_type:
                        super_family=TE_type.split('/')[1]
                elif "?" in TE_type:
                        super_family="unknown"
                elif "/" not in TE_type and "?" not in TE_type:
                        super_family="unknown"
                if "-" in super_family:
                        super_family = super_family.split('-')[0]
                TE_type = "LINE-"+super_family

        elif "LTR" in TE_type:
                if "/" in TE_type:
                        super_family=TE_type.split('/')[1]
                elif "?" in TE_type:
                        super_family="unknown"
                elif "/" not in TE_type and "?" not in TE_type:
                        super_family="unknown"
                if "-" in super_family:
                        super_family = super_family.split('-')[0]
                if "DIRS" in super_family or "Ngaro" in super_family or "Viper" in super_family:
                        TE_type = "DIRS-"+super_family                      #DIRS   Inverted_Long_Terminal_Repeat
#               elif "Penelope" in super_family:
#                       TE_type = "PLE-"+super_family
                else:
                        TE_type = "LTR-"+super_family
# Retroposon/L1-dep
        elif "Retroposon" in TE_type:
                if "/" in TE_type:
                        super_family=TE_type.split('/')[1]
                elif "/" not in TE_type and "?" not in TE_type:
                        super_family="nonLTR"
                        TE_type = "Retroposon_nonLTR"
#               TE_type = "Retroposon-"+super_family
                if "L1−dep" in super_family or "SVA" in super_family:
#			if "/" in TE_type:
#				super_family=TE_type.split('/')[1]
                        #super_family = "nonLTR"+
                        TE_type = "Retroposon_nonLTR-"+"L1_dep"#super_family
                elif "L1−derived" in super_family:
                        TE_type = "Retroposon_SINE-"+"L1_derived"#super_family

        elif "Satellite" in TE_type:
                if "/" in TE_type:
                        super_family=TE_type.split('/')[1]
                elif "/" not in TE_type and "?" not in TE_type:
                        super_family="unknown"
                TE_type = "Satellite-"+super_family

#       elif "ARTEFACT" in TE_type or "rRNA" in TE_type or "snRNA" in TE_type:continue
        elif "ARTEFACT" in TE_type:continue
        elif "RNA" in TE_type:# or "snRNA" in TE_type:
                super_family=TE_type
                TE_type = "Pseudogene-"+super_family

        elif "Unknown" in TE_type:
                TE_type = "Unknown"
#        if "Simple_repeat" in TE_type:
 #               TE_type = "Simple_repeat"
#        elif "Low_complexity" in TE_type:
 #               TE_type = "Low_complexity"
#        elif "Satellite:unknown" in TE_type:
#                TE_type = "Satellite"
	
	if "0" in TE_type:continue
	if TE_type not in dict_te:
		dict_te[TE_type]={}
		dict_number[TE_type]={}
		list_TE_type.append(TE_type)
	site_bin= str(int(float(lis1[1])))+"sitebin"+lis1[3]+"genebin"+lis1[4]
	number="number"
	if site_bin not in list_site_bin:
		list_site_bin.append(site_bin)
	if site_bin not in dict_te[TE_type]:
		dict_te[TE_type][site_bin]=float(lis1[-1])
		dict_number[TE_type][site_bin]=1
	else:
		dict_te[TE_type][site_bin]=dict_te[TE_type][site_bin]+float(lis1[-1])
		dict_number[TE_type][site_bin]=dict_number[TE_type][site_bin]+1

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
	
list_site_bin=sort_humanly(list_site_bin)
#list_TE_type=sort_humanly(list_TE_type)
list_TE_type=sorted(list_TE_type)

#f2.write("TE_type\tgene_site\tgene_bin\tgene_TE\tTE_percentage\n")
#f2.write("Site_number\tgene_bin\tgene_site")
#for TE in list_TE_type:
#	f2.write("\t"+TE)
#f2.write("\n")
f2.write("TE_type\t")
for site in list_site_bin:
	gene_site= site.split("sitebin")[1].split("genebin")[0]
	f2.write("\t"+gene_site)
f2.write("\n")

#for site in list_site_bin:
#	f2.write("{0}\t{1}\t{2}".format(site.split("_site_bin")[0],site.split("_site_bin")[1].split("_bin2")[0],site.split("_site_bin")[1].split("_bin2")[1]))
for te in list_TE_type:
	f2.write(te+"\t")
#		print dict_te[te][site]
#		print float(dict_number[te][site])
	for site in list_site_bin:
		if site in dict_te[te]:
			f2.write("\t"+str(round( float(dict_te[te][site])/float(dict_number[te][site]),4) ))
			#f2.write(te+"\t")
			#print site
#			gene_site = site.split("sitebin")[1].split("-")[1].split("bp")[0]
#		if "000" in gene_site and "10000" not in gene_site:
#			gene_site = gene_site.split("000")[0]+"k"
#		elif "10000"  in gene_site:
#			gene_site = "10k"
#		elif "500"==str(gene_site):
#			gene_site = "0"
#		else:
#			gene_site = "."	
			#f2.write("{0}\t{1}\t{2}\t".format(site.split("sitebin")[0],site.split("sitebin")[1].split("genebin")[0],site.split("sitebin")[1].split("genebin")[1]))
#			f2.write("{0}\t{1}\t{2}\t".format(site.split("sitebin")[0],gene_site,site.split("sitebin")[1].split("genebin")[1]))
	#	if site in dict_te[te]:
#			f2.write(str(round( float(dict_te[te][site])/float(dict_number[te][site]),4) ) +"\n") 
		else:
			f2.write("\t"+str(0))
	f2.write("\n")
