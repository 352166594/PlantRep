#!/public/software/R-3.3.1/bin/Rscript
argv<-commandArgs(TRUE)

##云雨图脚本
library(ggplot2)
library(grid)
library(RColorBrewer)
library(dplyr)
#pdf("length_percentage_genome.pdf",10,8)#png(argv[2],309,500)
#mydata = read.table("Total_length_percentage_genome_r.xls",header=T)
#pdf("Total_length_percentage_genome.pdf",2.6,4.1)
#repeat_type=strsplit(argv[1], '_div_order_kindom.xls')[[1]]
#main=paste(repeat_type,"divergence")
#filename=paste(repeat_type,"_divergence_in_plant_clade.pdf",sep="")
mydata = read.table(argv[1],header=T)
repeat_type=strsplit(argv[1], '.xls')[[1]]
#filename=paste(repeat_type,".pdf",sep="")
filename=paste(repeat_type,".png",sep="")
png(filename,168,220)
#pdf(filename,2.6,4.1)
mainlab=repeat_type

"%||%" <- function(a, b) {if (!is.null(a)) a else b}
geom_flat_violin <- function(mapping = NULL, data = NULL, stat = "ydensity",
                             position = "dodge", trim = TRUE, scale = "area",
                             show.legend = NA, inherit.aes = TRUE, ...) {
  layer(
    data = data,
    mapping = mapping,
    stat = stat,
    geom = GeomFlatViolin,
    position = position,
    show.legend = show.legend,
    inherit.aes = inherit.aes,
    params = list(
      trim = trim,
      scale = scale,
      ...
    )
  )
}

GeomFlatViolin <-
  ggproto("GeomFlatViolin", Geom,
          setup_data = function(data, params) {
            data$width <- data$width %||%
              params$width %||% (resolution(data$x, FALSE) * 0.9)
            # ymin, ymax, xmin, and xmax define the bounding rectangle for each group
            data %>%
              group_by(group) %>%
              mutate(ymin = min(y),
                     ymax = max(y),
                     xmin = x,
                     xmax = x + width / 2)
          },
          
          draw_group = function(data, panel_scales, coord) {
            # Find the points for the line to go all the way around
            data <- transform(data, xminv = x,
                              xmaxv = x + violinwidth * (xmax - x)) #利用transform函数为数据框mydata增加数据
            
            newdata <- rbind(plyr::arrange(transform(data, x = xmaxv), -y),plyr::arrange(transform(data, x = xminv), y))
            newdata_Polygon <- rbind(newdata, newdata[1,])
            newdata_Polygon$colour<-NA
            
            newdata_Path <- plyr::arrange(transform(data, x = xmaxv), -y)
            
            ggplot2:::ggname("geom_flat_violin", grobTree(
              GeomPolygon$draw_panel(newdata_Polygon, panel_scales, coord),
              GeomPath$draw_panel(newdata_Path, panel_scales, coord))
            )
          },
          
          draw_key = draw_key_polygon,
          
          default_aes = aes(weight = 1, colour = "grey20", fill = "white", size = 0.5,
                            alpha = NA, linetype = "solid"),
          
          required_aes = c("x", "y")
  )

findParams <- function(mu, sigma, skew, kurt) {
  value <- .C("JohnsonMomentFitR", as.double(mu), as.double(sigma),
              as.double(skew), as.double(kurt - 3), gamma = double(1),
              delta = double(1), xi = double(1), lambda = double(1),
              type = integer(1), PACKAGE = "SuppDists")
  
  list(gamma = value$gamma, delta = value$delta,
       xi = value$xi, lambda = value$lambda,
       type = c("SN", "SL", "SU", "SB")[value$type])
}

#mydata = read.table("Total_length_percentage_genome_r.xls",header=T)

d <- group_by(mydata, Species_type) %>%
  summarize(mean = mean(Stat),
            sd = sd(Stat))
ggplot(mydata, aes(x=Species_type, y=Stat))  +
  geom_jitter(aes(color=Species_type), width=0.1) +
  geom_boxplot(width=.1,position=position_nudge(x=0.25),fill="white",size=0.5) +
  geom_flat_violin(aes(fill=Species_type),position=position_nudge(x=.25),color="black") +
  coord_flip() + 
#  labs(title="Total length percentage in genome")+
  labs(title=mainlab)+
  #  theme_bw() +
  #  theme( axis.text = element_text(size=13),
  #         axis.title =  element_text(size=15),
  #         legend.position="none")
  scale_y_continuous(expand = c(0, 0)) +
  
  #theme(title=element_text(family="myFont",size=12,color="red",face="italic",hjust=0.2,lineheight=0.2),
  theme(plot.title = element_text(size=8,face="bold",color="black",hjust = 0.5),
        panel.background = element_blank(),#去除背景
        #       axis.title.x=element_text(size=28,face="bold",color="green",hjust=0.5),
        #       axis.text.x=element_text(size=20,face="bold",color="black",hjust=0.5),
        #axis.title.x=element_blank(),axis.text.x=element_blank(), axis.ticks.x=element_blank(),
        axis.title.y=element_blank(),axis.text.y=element_blank(), axis.ticks.y=element_blank(),
        #theme(axis.title.x=element_blank(),axis.text.x=element_blank(),axis.ticks.x=element_blank())
        legend.title = element_blank(),legend.position='none',#,
        axis.line.x = element_line(size=1, colour = "black"),axis.title.x=element_blank(),#,
        axis.text.x=element_text(size=8,face="bold",color="black",hjust=0))
        # axis.title.y=element_text(size=28,face="bold",color="green",hjust=0.5))
        
