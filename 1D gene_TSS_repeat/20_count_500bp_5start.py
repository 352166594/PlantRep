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
#		title = "\t".join(lis1[4:])
		for site in lis1[4:]:
			site_list.append(site)
		continue
	if lis1[3] not in TE_type:
		TE_type[lis1[3]] = {}
	for i in range(len(lis1[4:])):
		pre_site = site_list[i]
		sit_list = lis1[4:]
		if pre_site not in TE_type[lis1[3]]:
			TE_type[lis1[3]][pre_site] = int(0)
			if lis1[3] not in TE_list:
				TE_list.append(lis1[3])
		TE_type[lis1[3]][pre_site] = TE_type[lis1[3]][pre_site] + int(sit_list[i])
		
#print TE_list
#print site_list
#f2.write("TE_type\tgene_site\tnumber\tgene_bin\n")
if len(TE_list) == 0:
	pass
elif len(TE_list) != 0:
	f2 = open(sys.argv[2],'w')
	f2.write("TE_type\tgene_site\tnumber\tgene_bin\tgene_TE\n")
	for te in TE_list:
		#for i in range(0,len(site_list),20):
		for i in range(0,20):
#			sit = title.split("\t")[i]
			sit = site_list[i]
			sites = sit.split("bp")[0].split("-")[0]	#0-1kb
			whole_sites = 20 - (int(sites)*2)/1000	#		1:60	0:29
			if  sit in TE_type[te]:
				f2.write(te+"\t"+str(whole_sites)+"\t"+str(TE_type[te][sit])+"\t"+sit+"\t"+"5'upper_500bp\n")
			else:
				f2.write(te+"\t"+str(whole_sites)+"\t"+str(0)+"\t"+sit+"\t"+"5'upper_500bp\n")
