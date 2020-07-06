#!/public/software/R-3.3.1/bin/Rscript

argv<-commandArgs(TRUE)
dat = read.table(argv[1],header=T)
repeat_type=strsplit(argv[1], '.xls')[[1]]
filename=paste(repeat_type,"_mean.csv",sep="")
#filename_sd=paste(repeat_type,"_sd.csv",sep="")


#aggregate成功产生标准差和平均值的统计表

#dat = read.table("type_species_1class_number.xls",header=T)
#dat = read.table("kindom_order_length_percentage_genome.xls",header=T)
#vars <-c("DIRS","LINE","LTR","PLE","SINE","unknown","Circular_dsDNA","DNA_Polymerase","Rolling_Circle","TIR","RNA","Satellite","Low_complexity","Satellite","Simple_repeat","Unknown")
vars <-c("LTR","Unknown","TIR","LINE","Simple_repeat","Rolling_Circle","Low_complexity","SINE","Satellite","Satellite","RNA","PLE","DNA_Polymerase","DIRS","Circular_dsDNA")

head(dat[vars])
#6aggregate
#成功产生了标准差和平均值的统计表
aggregate(dat[vars],by=list(species_type=dat$species_type),mean)
#可输出
mystat=aggregate(dat[vars],by=list(species_type=dat$species_type),mean)
head(mystat)
#write.csv(mystat,file="kindom_order_length_percentage_genome_mean.csv")
write.csv(mystat,file=filename)
#aggregate(dat[vars],by=list(species_type=dat$species_type),sd)
#mysd=aggregate(dat[vars],by=list(species_type=dat$species_type),sd)
#write.csv(mysd,file="kindom_order_length_percentage_genome_sd.csv")
