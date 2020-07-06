import sys
#python ratio_site_gene_TE_500bp.py /vol3/agis/huangsanwen_group/luoxizhi/work/gene_525/site_gene_TE_500bp/20_500bp_35/104_Zostera_marina_500bp_merge.xls /vol3/agis/huangsanwen_group/luoxizhi/work/gene_525/gene_bin_500bp/104_Zostera_marina_gene_bin_500bp.xls /vol3/agis/huangsanwen_group/luoxizhi/work/gene_525/ratio_site_gene_TE_500bp/104_Zostera_marina_ratio_500bp_merge.xls

f1=open(sys.argv[1])
f2=open(sys.argv[2])
f3=open(sys.argv[3],"w")

bin_dic = {}
for lin1  in f1:
	lis1 =lin1.strip().split("\t")
	gene_site =lis1[1]
	gene_TE = lis1[-2]
	bin_key = str(gene_site)#+"_"+gene_TE
	bin_dic[bin_key]=int(lis1[-1])#lin1.strip()
#	print bin_key
for lin2 in f2:
	if "TE_type" in lin2:
		f3.write(lin2.strip()+"\tgene_number\tTE_percentage\n")
	else:
		lis2=lin2.strip().split("\t")
		gene_site2=int(float(lis2[1]))
		gene_TE2 = lis2[-1]
		te_number=int(lis2[2])
		
		bin_key2= str(gene_site2)#+"_"+gene_TE2
#		print bin_key2
		if bin_key2 in bin_dic:
			gene_number = bin_dic[bin_key2]#.split("\t")[2])
			f3.write(lin2.strip()+"\t"+str(gene_number) + "\t"+str(round(te_number/float(gene_number),3))+"\n")
