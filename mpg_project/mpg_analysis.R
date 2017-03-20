# Analysis and visualization for gas data

#Load database from mysql, then select all into mpgs table
db <- dbConnect(MySQL(), dbname = "mpg_db", host = "localhost", default.file = "~/.my.cnf", user = NULL, password = NULL)
mpgs <- dbGetQuery(db, "SELECT * FROM mpg_table")

#plot
g <- ggplot(data = mpgs, aes(y = mpg, x = mpd))
g + geom_point(size = 3) #these two commands plot out mpg over date
#g + geom_point(aes(color = station), size = 3)
g + geom_smooth(method=lm)

###
ggplot(mpgs, aes(x=mpd, y=mpg)) +
  geom_point(shape=1) +    # Use hollow circles
  geom_smooth(method=lm, se=FALSE) #find slop of fitted line

mean(mpgs[["mpg"]])
sum(mpgs[["gallons"]])
sum(mpgs[["cost"]])

sum(mpgs[["miles"]])/sum(mpgs[["gallons"]])


