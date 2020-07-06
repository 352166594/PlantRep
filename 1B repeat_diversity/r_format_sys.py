import sys
#f1=open("kindom_order_length_percentage_genome.csv")
f1=open(sys.argv[1])
f2=open(sys.argv[2],"w")
#f2=open("r_order_length_percentage_genome.txt","w")

f2.write("Species_type\tSpecies\tOrder\tStat\n")

type_list = []
for lin1 in f1:
	lis1 = lin1.strip().split("\t")
	if "#" in lin1:
		type_list=lis1[1:-1]
	else:
		for i in range(len(lis1[1:-1])):
			f2.write("{0}\t{1}\t{2}\t{3}\n".format(lis1[-1],lis1[0],type_list[i],lis1[1:-1][i]))
