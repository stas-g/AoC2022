#day1
setwd("/home/nfg/AoC2022")
x <- read.csv("calories.txt", blank.lines.skip = FALSE)[,1]

ind <- rep(NA, length = length(x))
m <- 0
for(i in 1 : length(x)) {
  ind[i] <- m
  if(is.na(x[i])) {
    m <- m + 1
      }
}

elf_calories <- tapply(x, ind, sum, na.rm = TRUE)

#1.1
max(elf_calories)
#1.2
sum(sort(elf_calories, decreasing = TRUE)[1 : 3])

#---------------------version 2
x <- read.csv("calories.txt", blank.lines.skip = FALSE)[,1]
z <- sort(tapply(x, cumsum(is.na(x)), sum, na.rm = TRUE), decreasing = TRUE)
max(z)
sum(z[1 : 3])

#---------------------version 3
x <- read.csv("calories.txt", blank.lines.skip = FALSE, na.strings = "X")[,1]
