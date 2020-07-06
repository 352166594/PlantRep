library(ggplot2)
library(ggsci)
library(reshape2)

argv<-commandArgs(TRUE)
mydata = read.table(argv[1],header=T,sep="\t",na.strings="NA",stringsAsFactors=FALSE)
repeat_type=strsplit(argv[1], '_plotstack.xls')[[1]]
#filename=paste(repeat_type,".png",sep="")
filename=paste(repeat_type,".pdf",sep="")
mainlab=repeat_type
pdf(filename)
#png(filename)#,1000,220)

#mydata<-read.table("3StackedColumn_length_percentage_repeat.xls",header=T,sep="\t",na.strings="NA",stringsAsFactors=FALSE)
sum<-sort(rowSums(mydata[,2:ncol(mydata)]),index.return=TRUE)
#colsum<-sort(colSums(mydata[,2:ncol(mydata)]),index.return=TRUE,decreasing = TRUE)
#mydata<-mydata[,c(1,colsum$ix+1)]
mydata$Clarity <- factor(mydata$Clarity, levels = mydata$Clarity[order(sum$ix)])
mydata<-melt(mydata,id.vars='Clarity')

ggplot(data=mydata,aes(variable,value,fill=Clarity))+
  geom_bar(stat="identity",position="stack", color="black", width=0.7,size=0.25)+
  labs(title=mainlab,y="Percentage")+
#  labs(title="Repeat relative proportions", y="Percentage")+
  scale_fill_manual(values=pal_d3("category20")(25))+
  theme(panel.background = element_blank(),
        legend.text = element_text(size = 8),
	#legend.title = element_blank(),legend.position='none',
	#legend.text.title = element_text(size = 8,face="bold",color="black",hjust = 0.5),
        legend.title = element_text(size=8,face="bold",color="black",hjust = 0.2),
        legend.text = element_text(size=8,color="black"),
        plot.title = element_text(size=8,face="bold",color="black",hjust = 0.5),#,family="Arial")
        axis.title.x=element_blank(),#element_text(size=8,face="bold",color="black",hjust=0.5),
        axis.title.y=element_text(size=8,face="bold",color="black",hjust=0.5),
        axis.text.x=element_text(size=8,color="black",angle = 90,hjust=1),
        axis.text.y=element_text(size=8,color="black",hjust=0.5),
        axis.line.y = element_line(size=1,colour = "black"),
        axis.line.x = element_line(size=1,colour = "black"))+
	scale_y_continuous(expand = c(0, 0))+
#  scale_y_continuous(breaks=seq(0, 100, 10),expand = c(0, 0))+
  coord_flip()
  

