f1 = open('repeat_order_number.xls')
f2 = open('order_number_percentage.xls','w')
f3 = open('order_number_total.xls','w')
for lin in f1:
	if "Species" in lin:
		f2.write(lin.strip()+'\t'+'Total'+'\n')
		f3.write(lin.strip()+'\t'+'Total'+'\n')
	else:
		lis=lin.strip().split('\t')
		f2.write(lis[0])
		f3.write(lis[0])
		lengths = 0
		for repeat in lis[1:]:
			lengths = lengths + int(repeat)
			f3.write('\t' + str(repeat))
		f3.write('\t'+str(lengths)+'\n')
		for lens in lis[1:]:
			if lengths != 0:
				percentage = str(round(float(lens) / lengths , 4)*100)# + '%'
			else:
				percentage = str(0)
			f2.write('\t' + percentage)
		f2.write('\t'+'100'+'\n')
