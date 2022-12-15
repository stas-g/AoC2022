setwd("/home/nfg/AoC2022")

#day1
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
x <- read.csv("calories.txt", blank.lines.skip = FALSE)[,1]
z <- sort(sapply(strsplit(paste(x, collapse = "-"), split = "NA")[[1]], FUN = function(z) sum(as.numeric(strsplit(z, split = "-")[[1]]), na.rm = TRUE)), decreasing = TRUE)
max(z)
sum(z[1 : 3])


#day2
# ROCK PAPER CISSORS
# A     B       C
# X     Y       Z
x <- read.csv("rpc.txt", sep = " ", header = FALSE)
xx <- paste0(x[,1], x[,2])
w <- ifelse(xx %in% c("AY", "BZ", "CX"), 6, ifelse(xx %in% c("AX", "BY", "CZ"), 3, 0))
v <- ifelse(x[,2] == "X", 1, ifelse(x[,2] == "Y", 2, 3))
sum(w + v)

# ROCK PAPER CISSORS
# A     B       C
#lose   draw    win
# X     Y       Z

x$num <- ifelse(x[,1] == "A", 1, ifelse(x[,1] == "B", 2, 3))
w <- ifelse(x[,2] == "X", (x$num - 1)%%3, ifelse(x[,2] == "Y", x$num, (x$num + 1)%%3))
w[w == 0] <- 3
v <- ifelse(x[,2] == "X", 0, ifelse(x[,2] == "Y", 3, 6))
sum(w + v)

#day3
x <- scan("rucksack.txt", what = "", sep = "\n")
z <- lapply(x, FUN = function(z) strsplit(z, "")[[1]])
pr <- sapply(x, FUN = function(z) {
        zz <- strsplit(z, split = "")[[1]]
        n <- length(zz)
        w <- intersect(unique(zz[1 : (n/2)]), unique(zz[(n/2 + 1) : n]))
        which(w == c(letters, LETTERS))
      })
#3.1
sum(pr)
#3.2
pr2 <- tapply(z, (0:(length(z) - 1))%/%3, FUN = function(w) {
        l <- Reduce(intersect, w)
        which(l == c(letters, LETTERS))
      })
sum(pr2)


#day4
x <- scan("day4.txt", what = "", sep = "\n")
w <- lapply(x, FUN = function(ww) as.numeric(strsplit(ww, split = "[-,]")[[1]]))
#4.1
z <- sapply(w, FUN = function(ww) {
  if(any((ww[1:2] - ww[3:4]) == 0)) return(TRUE)
  if(ww[1] < ww[3]) {
    ifelse(ww[2] > ww[4], TRUE, FALSE)
    } else {
        ifelse(ww[2] < ww[4], TRUE, FALSE)
  }
})

#or
z2 <- sapply(w, FUN = function(ww) {
  length(intersect(ww[1] : ww[2], ww[3] : ww[4])) == min(ww[2] - ww[1] + 1, ww[4] - ww[3] + 1)
})

#4.2
z3 <- sapply(w, FUN = function(ww) {
  if(any((ww[1:2] - ww[3:4]) == 0)) return(TRUE)
  if(any((ww[1:2] - ww[4:3]) == 0)) return(TRUE)
  if(ww[1] < ww[3]) {
      ww[2] > ww[3]
  } else {
      ww[4] > ww[1]
  }
})





##
