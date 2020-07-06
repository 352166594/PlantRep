import sys

#python count_1000bp.py 494_Solanum_chilense_1000bp.xls 494_Solanum_chilense_1000bp_merge.xls
f1 = open(sys.argv[1])
#f2 = open(sys.argv[2],'w')
#gene_id chr     gene_5start_gene_3end   TE_type 0-500bp 500-1000bp      1000-1500bp     1500-2000bp     2000-2500bp     2500-3000bp     3000-3500bp     3500-4000bp     4000-4500bp     4500-5000bp     5000-5500bp     5500-6000bp     6000-6500bp     6500-7000bp     7000-7500bp     7500-8000bp     8000-8500bp     8500-9000bp     9000-9500bp     9500-10000bp    10000-10500bp   10500-11000bp   11000-11500bp   11500-12000bp   12000-12500bp   12500-13000bp   13000-13500bp   13500-14000bp   14000-14500bp   14500-15000bp   15000-15500bp   15500-16000bp   16000-16500bp   16500-17000bp   17000-17500bp   17500-18000bp   18000-18500bp   18500-19000bp   19000-19500bp    19500-20000bp   20000-20500bp   20500-21000bp   21000-21500bp   21500-22000bp   22000-22500bp   22500-23000bp   23000-23500bp   23500-24000bp   24000-24500bp   24500-25000bp   25000-25500bp   25500-26000bp   26000-26500bp   26500-27000bp   27000-27500bp   27500-28000bp   28000-28500bp   28500-29000bp   29000-29500bp   29500-30000bp
#ZOSMA_1G00010   LFYR01000729.1  2040    1977    DNA     0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0
#ZOSMA_1G00010   LFYR01000729.1  2040    1977    LINE    0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0
		
TE_type = {}
TE_list = []
site_list = []
for lin1 in f1:
	lis1 = lin1.strip().split("\t")
	if "TE_type" in lin1:
#		f2.write("\t".join(lis1[3:])+"\n")
#		title = "\t".join(lis1[1:])
		for site in lis1[4:]:
			site_list.append(site)
		continue
	if lis1[4] not in TE_type:
		TE_type[lis1[4]] = {}
	for i in range(len(lis1[5:])):
		pre_site = site_list[i]
		sit_list = lis1[5:]
		if pre_site not in TE_type[lis1[4]]:
			TE_type[lis1[4]][pre_site] = int(0)
			if lis1[4] not in TE_list:
				TE_list.append(lis1[4])
		TE_type[lis1[4]][pre_site] = TE_type[lis1[4]][pre_site] + int(sit_list[i])

#print TE_list
#print site_list
#f2.write("TE_type\tgene_site\tnumber\tgene_bin\n")
if len(TE_list) == 0:
	pass
elif len(TE_list) != 0:
	f2 = open(sys.argv[2],'w')
#	f2.write("TE_type\tgene_site\tnumber\tgene_bin\n")
	for te in TE_list:
#		f2.write(te)
		#for i in range(0,len(site_list),20):
		for i in range(0,20):
#			sit = title.split("\t")[i+1]
			#print sit	
			sit = site_list[i]
			sites = sit.split("bp")[0].split("-")[1]	#0-1000b
			whole_sites = (int(sites)*2)/1000+20		#61
#			print sites
#			f2.write(te+"\t"+str(whole_sites)+"\t"+str(TE_type[te][sit])+"\t"+"500bp_5gene3\n")
			if  sit in TE_type[te]:
				f2.write(te+"\t"+str(whole_sites)+"\t"+str(TE_type[te][sit])+"\t"+sit+"\t"+"500bp_5gene3\n")
			else:
				f2.write(te+"\t"+str(whole_sites)+"\t"+str(0)+"\t"+sit+"\t"+"500bp_5gene3\n")
