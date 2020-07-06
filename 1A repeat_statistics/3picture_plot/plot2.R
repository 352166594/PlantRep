#!/public/software/R-3.3.1/bin/Rscript

argv<-commandArgs(TRUE)
#pdf(argv[2],10,8)
#png(argv[2],1000,600)
library(ggplot2)
library(grid)
library(ggsci)

#dat = read.table("DNA_r_1class_number.xls",header=T)
dat = read.table(argv[1],header=T)
repeat_type=strsplit(argv[1], '.xls')[[1]]
filename=paste(repeat_type,".png",sep="")
#pdf(filename,2.6,4.1)
png(filename,168,220)
#pdf(filename,3.6,3.6)
mainlab=repeat_type


bar_plot <- ggplot(dat, aes(Species_type,Stat,fill=Species_type))+
  scale_x_discrete(breaks=dat$Species_type, labels = dat$Species_type)+
  geom_boxplot(outlier.shape= NA)+
#  scale_fill_manual(values=pal_d3("category20")(15))+
   labs(title=mainlab)+
  scale_y_continuous(expand = c(0, 0)) +
  theme(#plot.title = element_text(family="Arial",size=36,face="bold",color="green",hjust = 0.5),
	plot.title = element_text(size=8,face="bold",color="black",hjust = 0.5),
	panel.background = element_blank(),#去除背景
#	axis.title.x=element_blank(),axis.text.x=element_blank(), axis.ticks.x=element_blank(),
	axis.title.y=element_blank(),axis.text.y=element_blank(), axis.ticks.y=element_blank(),
	legend.title = element_blank(),legend.position='none',
	axis.line.x = element_line(size=1, colour = "black"),
	axis.text.x=element_text(size=8,face="bold",color="black",hjust=0),
        axis.title.x=element_blank()
#	axis.line.y = element_line(size=1, colour = "black"),
#	axis.text.y=element_text(size=8,face="bold",color="black",hjust=0),
#        axis.title.y=element_blank()
	)+
   coord_flip()
bar_plot


