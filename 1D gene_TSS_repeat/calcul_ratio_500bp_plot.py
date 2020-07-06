# coding=utf-8
import sys

f1=open('whole_species_ratio_500bp_merge.xls')
f2=open('plot_whole_species_ratio_500bp_merge.xls','w')

dict_te = {}
list_site_bin = []
list_TE_type=[]
dict_number={}
for lin1 in f1:
	lis1=lin1.strip().split("\t")
	if "TE_type" in lin1:continue
	if "no_TE_in_scaffold" in lin1 or "Unknown" in lin1 or "Others" in lin1:continue
	TE_type = lis1[0]
#	if TE_type=="RC":
#		TE_type="Rolling_Circle"
	if TE_type not in dict_te:
		dict_te[TE_type]={}
		dict_number[TE_type]={}
		list_TE_type.append(TE_type)
	#print lis1[1]
	site_bin= str(int(float(lis1[1])))+"_site_bin_"+lis1[3]+"_genebin_"+lis1[4]
	#print site_bin
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

f2.write("TE_type\tgene_site\tgene_bin\tgene_TE\tTE_percentage\n")
#f2.write("Site_number\tgene_bin\tgene_site")
#for TE in list_TE_type:
#	f2.write("\t"+TE)
#f2.write("\n")

for site in list_site_bin:
#	f2.write("{0}\t{1}\t{2}".format(site.split("_site_bin")[0],site.split("_site_bin")[1].split("_bin2")[0],site.split("_site_bin")[1].split("_bin2")[1]))
	for te in list_TE_type:
#		print dict_te[te][site]
#		print float(dict_number[te][site])
		f2.write(te+"\t")
		f2.write("{0}\t{1}\t{2}\t".format(site.split("_site_bin_")[0],site.split("_site_bin_")[1].split("_genebin_")[0],site.split("_site_bin_")[1].split("_genebin_")[1]))
		if site in dict_te[te]:
			f2.write(str(round( float(dict_te[te][site])/float(dict_number[te][site]),4) ) +"\n") 
		else:
			f2.write(str(0)+"\n")
#	f2.write("\n")
