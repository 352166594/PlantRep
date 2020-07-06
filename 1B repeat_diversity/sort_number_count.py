# coding=utf-8 
f1=open("kindom_super_family_number.xls")
f2=open("sort_kindom_super_family_number.xls","w")
f3=open("type_kindom_super_family_number.xls","w")
dict_type = {}
list_type = []
list_kindom = []
dict_stat = {}
dict_count = {}#统计一个类群中出现的重复类型的种类

for lin in f1:
	lis = lin.strip().split("\t")
	if "#" in lin:
		for type in lis[1:-1]:
			dict_type[type] = {}
			dict_stat[type] = {}
			list_type.append(type)
	else:
		kindom_type = lis[-1]
		if kindom_type not in list_kindom:
			list_kindom.append(kindom_type)
			dict_count[kindom_type]=[]
		for num in range(len(lis[1:-1])):
			te_type = list_type[num]
#			if te_type not in dict_count[kindom_type]:#统计一个类群出现总的te类型
##				dict_count[kindom_type].append(te_type)
			if kindom_type not in dict_type[te_type]:
				dict_type[te_type][kindom_type] = 0
				dict_stat[te_type][kindom_type] = 0
				if int(lis[num+1]) != int(0):
					dict_type[te_type][kindom_type] = dict_type[te_type][kindom_type] + 1
					dict_stat[te_type][kindom_type] = dict_stat[te_type][kindom_type] + int(lis[num+1])
				
				
			else:
				if int(lis[num+1]) != int(0):
					dict_type[te_type][kindom_type] = dict_type[te_type][kindom_type] + 1#每个TE类型每个植物类群的数量
					dict_stat[te_type][kindom_type] = dict_stat[te_type][kindom_type] + int(lis[num+1])
					if te_type not in dict_count[kindom_type]:
						dict_count[kindom_type].append(te_type)
				
#a = sorted(d.items(), key=lambda x: x[1])
#type_te_kindom = sorted(dict_type[te_type].items(), key=lambda x: x[1])#每个TE类型每个植物类群的数量
#print type_te_kindom
dic_count = {}
for kindom in list_kindom:
	lens = len(dict_count[kindom])
	dic_count[kindom] = lens
count_kindom = sorted(dic_count.items(), key=lambda x: x[1])
print count_kindom

f2.write("kindom")
for ys_type in list_type:
	f2.write("\t"+ys_type)
f2.write("\n")

for ys_kindom in list_kindom:
	f2.write(ys_kindom)
	for ys_type in list_type:
 		f2.write("\t"+str(dict_stat[ys_type][ys_kindom]))
	f2.write("\n")	
		
		
f3.write("kindom")
for ys_type in list_type:
	f3.write("\t"+ys_type)
f3.write("\n")

for ys_kindom in list_kindom:
	f3.write(ys_kindom)
	for ys_type in list_type:
 		f3.write("\t"+str(dict_type[ys_type][ys_kindom]))
	f3.write("\n")	
				
				
				
				
				
				
