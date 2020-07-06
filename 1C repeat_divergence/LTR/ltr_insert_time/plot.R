#argv<-commandArgs(TRUE)
library(ggplot2)
#dat = read.table("total_copia_count_max_ltr_inserttime.xls",header=T)   #,sep="\t")
dat = read.table("copia_percentage_kindom_count_insert_time_format.xls",header=T)
p<-ggplot(data=dat,aes(x=Figure_order,y=LTR_nummber,fill =Temporal,group = Temporal)) + 
  geom_bar(aes(colour=Temporal),stat = "identity")+
  facet_grid(Species_type ~ .,scales = "free_y")+
  #facet_grid(Species_type ~Temporal,scales = "free_y")+
  labs(title="Intact LTR/Copia insert time",x="Insert_Temporal_interval", y="Species_number")+
  theme(panel.background = element_blank(),
        plot.title = element_text(size=8,face="bold",color="black",hjust = 0.5),#,family="Arial")
        legend.title = element_text(size=8,face="bold",color="black",hjust = 0.2),
        legend.text = element_text(size=8,color="black"),
        axis.title.x=element_text(size=8,face="bold",color="black",hjust=0.5),
        axis.title.y=element_text(size=8,face="bold",color="black",hjust=0.5),
        axis.text.x=element_text(size=8,color="black",angle = 90,hjust=1),
        axis.text.y=element_text(size=8,color="black"),#,hjust=0.5),
        axis.line.y = element_line(size=1, colour = "black"),
        axis.line.x = element_line(size=1, colour = "black"))+
  #  scale_x_continuous(expand = c(0, 0),breaks=dat$Figure_order,labels=paste(dat$Interval,"-",dat$Temporal))+
  scale_x_continuous(expand = c(0, 0.01),breaks=dat$Figure_order,labels=dat$Interval)+#paste(dat$Interval,"-",dat$Temporal))+
  scale_y_continuous(expand = c(0, 0.01))
#  scale_x_continuous(expand = c(0.001, 0.5),breaks=dat$gene_site,labels=paste(dat$gene_site-1,"-",dat$gene_site))+
#scale_y_continuous(breaks=seq(0, 200, 20),expand = c(0, 0))#+ scale_x_continuous(expand = c(0, 0))
p

