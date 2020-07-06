import sys

#python count_1000bp.py 494_Solanum_chilense_1000bp.xls 494_Solanum_chilense_1000bp_merge.xls
f1 = open(sys.argv[1])
#f2 = open(sys.argv[2],'w')
		
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
		for i in range(0,20):
#			sit = title.split("\t")[i+1]
			#print sit
			sit = site_list[i]
			sites = sit.split("bp")[0].split("-")[1]	#0-1000b
			whole_sites =60 -(int(sites)*2)/1000 + 1	#41-61
#			print sites
#			f2.write(te+"\t"+str(whole_sites)+"\t"+str(TE_type[te][sit])+"\t"+"500bp_5gene3\n")
			if  sit in TE_type[te]:
				f2.write(te+"\t"+str(whole_sites)+"\t"+str(TE_type[te][sit])+"\t"+sit+"\t"+"500bp_3gene5\n")
			else:
				f2.write(te+"\t"+str(whole_sites)+"\t"+str(0)+"\t"+sit+"\t"+"500bp_3gene5\n")
