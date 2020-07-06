argv<-commandArgs(TRUE)
library(ggplot2)
library(ggsci)
#dat = read.table("plot3_whole_species_ratio_500bp_merge.xls",header=T)
dat = read.table(argv[1],header=T)
repeat_type=strsplit(argv[1], '_plot_whole_species_ratio_500bp_merge.xls')[[1]]
#filename=paste(repeat_type,".pdf",sep="")
#filename=paste(repeat_type,".png",sep="")
#png(filename,800,300)
pdfname=paste(repeat_type,".pdf",sep="")
pdf(pdfname,8,5.2)
mainlab=paste(repeat_type,"percentage with gene site",sep=" ")

p<-ggplot(data=dat,aes(x=gene_site,y=TE_percentage,group = TE_type)) + 
  geom_line(aes(colour=TE_type),size=1)+
# scale_fill_manual(values=c(pal_npg("nrc")(7)))+
# scale_fill_manual(values=c("#E64B35FF","#4DBBD5FF","#00A087FF","#3C5488FF","#F39B7FFF","#8491B4FF","#91D1C2FF","#DC0000FF"))+
#  scale_fill_manual(values=c( "#1F77B4FF","#FF7F0EFF","#2CA02CFF","#D62728FF","#9467BDFF","#8C564BFF","#E377C2FF","#7F7F7FFF","#BCBD22FF","#17BECFFF","#AEC7E8FF","#FFBB78FF","#98DF8AFF","#FF9896FF","#C5B0D5FF","#C49C94FF","#F7B6D2FF","#C7C7C7FF","#DBDB8DFF","#9EDAE5FF"))+
  scale_colour_manual(values=pal_d3("category20")(20))+
#  scale_fill_manual(values=pal_d3("category20")(20))+
#  scale_shape_manual(values=c(21,22,23,24))+
  #scale_shape_manual(values=c(21,24,3,22,25,4,23,12)) +
#  scale_shape_manual(values=c(1,2,3,4,5,6,7,8)) +
  #https://www.jianshu.com/p/e53b9692173f
#  geom_point(size=1,aes(shape=TE_type,colour=TE_type))+
  geom_point(size=1,shape=21,aes(colour=TE_type))+
  #labs(title="average repeat ratio with gene site",x="gene_site", y="TE_percentage")+
  labs(title=mainlab,x="Gene bin", y="TE percentage")+
  theme(panel.background = element_blank(),
        legend.title = element_text(size=8,face="bold",color="black",hjust = 0.2),
        legend.text = element_text(size=8,color="black"),
        plot.title = element_text(size=8,face="bold",color="black",hjust = 0.5),#,family="Arial")
        axis.title.x=element_text(size=8,face="bold",color="black",hjust=0.5),
        axis.title.y=element_text(size=8,face="bold",color="black",hjust=0.5),
        axis.text.x=element_text(size=8,color="black",angle = 90,hjust=1),
        axis.text.y=element_text(size=8,color="black",hjust=0.5),
        axis.line.y = element_line(size=1, colour = "black"),
        axis.line.x = element_line(size=1, colour = "black"))+
#	scale_y_continuous(expand = c(0, 0))
  scale_x_continuous(expand = c(0.001, 0.5),breaks=dat$gene_site,labels=dat$gene_bin)+
  scale_y_continuous(expand = c(0, 0))
#  scale_y_continuous(breaks=seq(0, 0.3, 0.05),expand = c(0, 0))#+ scale_x_continuous(expand = c(0, 0))
p
