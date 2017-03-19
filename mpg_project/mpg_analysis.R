# Analysis and visualization for gas data

#Load database from mysql, then select all into mpgs table
db <- dbConnect(MySQL(), dbname = "mpg_db", host = "localhost", default.file = "~/.my.cnf", user = NULL, password = NULL)
mpgs <- dbGetQuery(db, "SELECT * FROM mpg_table")

#plot
g <- ggplot(data = mpgs, aes(y = costpergal, x = thedate))
g + geom_point(size = 3) #these two commands plot out mpg over date
g + geom_point(aes(color = station), size = 3)


