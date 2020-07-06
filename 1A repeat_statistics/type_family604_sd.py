import sys

f1 = open(sys.argv[1])
f2 = open(sys.argv[2],'w')

for lin1 in f1:
	if 'Species' in lin1:
		lis =lin1.strip().split("\t")
		new_lis=[]
		for i in lis:
			if ":" in i:
				i=i.split(":")[1]
			new_lis.append(i)
		new_lin = "\t".join(new_lis)
		f2.write(new_lin+"\t"+"species_type"+"\n")
#		f2.write(lin1.strip()+"\t"+"species_type"+"\n")
		continue
	
	lis1 = lin1.strip().split("\t")
	species_number = int(lis1[0].split("_")[0])
	
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
		species_type = "14_Lamiids"
	elif species_number >= 511 and species_number <=525:
		species_type = "15_Campanulids"
		
	new_lin = lin1.strip()+"\t"+species_type+"\n"
	f2.write(new_lin)
		
