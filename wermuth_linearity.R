wermuth_linearity <- function(allvars){
  library(dplyr)
  library(tibble)
  ##browser()
  p <- ncol(allvars)
  pnames <- colnames(allvars)
  tvec <- vector(length = 0.5*p^2*(p - 1))
  #### get each pair of names
  namepairs <- as_tibble(apply(expand.grid(pnames, pnames),2,as.character))
  namepairs <- filter(namepairs, Var1 != Var2)
  #### and then get each pair and each other singleton

  ### correlations
  cormat <- data.matrix(cor(allvars))
  ### partial correlations
  partialcormat <- myPartialCorMat(pnames, allvars)
  
  cwmat <- matrix(nrow = p, ncol = p)  
  diag(cwmat) <- sqrt(diag(var(allvars)))
  cwmat[lower.tri(cwmat)] <- cormat[lower.tri(cormat)]
  cwmat[upper.tri(cwmat)] <- partialcormat[upper.tri(partialcormat)]
  colnames(cwmat) <- pnames
  

  #### regress then on the other names
  ### p(p-1) squared terms
  nlMat <- myNonlinearTMat(listOfNames = pnames, dataset = allvars)
  ### 0.5*p*(p-1)*(p-2) crossproducts
  ### compare t-statistics to a normal distribution with mean 3/8 and sd n + 1/4
  cpMat <- myCrossProdMat(namePairMat = namepairs, dataset = allvars)
  alltees <- c(nlMat, cpMat)
  alltees <- rbind(alltees, names(alltees))
  alt <- as_tibble(t(alltees))
  names(alt) <- c("tstats", "reg")
  alt <- mutate(alt, tstats = as.numeric(tstats))
  alt <- arrange(alt, tstats)
 # browser()
  resultList <- list(orderedstats = alt, correlations = cwmat)
}

myPartialCor <- function(name1, name2, listOfNames, dataset){
 
  otherVars <- setdiff(listOfNames, c(name1, name2))
  formula1 <- as.formula(paste(name1, paste(otherVars, collapse = " + "), sep = " ~ "))
  formula2 <- as.formula(paste(name2, paste(otherVars, collapse = " + "), sep = " ~ "))
  resid1 <- residuals(lm(formula = formula1, data = dataset))
  resid2 <- residuals(lm(formula = formula2, data = dataset))
  
  cor(resid1, resid2)
}
myPartialCorVec <- function(name, listOfNames, dataset){
  sapply(listOfNames, myPartialCor, name1 = name, listOfNames = listOfNames, dataset = dataset )
}
myPartialCorMat <- function(listOfNames, dataset){
  
  sapply(listOfNames, myPartialCorVec, listOfNames = listOfNames, dataset = dataset)
  
}
 
myNonlinearT <- function(name1, name2, dataset){ 

  sqt <- as_tibble(scale(dataset[,name2], scale = FALSE)^2)
  dataset <- bind_cols(dataset, sqt)
  formula <- as.formula(paste0(name1," ~ ", name2," + V1"))

  tees <- summary(lm(formula = formula, data = dataset))$coefficients[, 't value']
  output <- ifelse(is.na(tees['V1']), NA, tees['V1'])
  names(output) <- name2
  return(output)
  }
myNonlinearTVec <- function(name, listOfNames, dataset){
  res <- sapply(setdiff(listOfNames, name), myNonlinearT, name1 = name, dataset = dataset)
  outvec <- vector(length = length(listOfNames))
  names(outvec) <- listOfNames
  idx <- match(name, listOfNames)
  outvec[idx] <- NA
  outvec[-idx] <- res
  names(outvec) <- paste(names(outvec),names(outvec), sep  = ".") 
  return(outvec)
}
myNonlinearTMat <- function(listOfNames, dataset){
  unlist(sapply(listOfNames, myNonlinearTVec, listOfNames = listOfNames, dataset = dataset, simplify = FALSE))
}

myCrossProd <- function(name, namepair, dataset){
 
  crossprod <- as_tibble(scale(dataset[namepair[[1]]], scale = FALSE)*scale(dataset[namepair[[2]]], scale = FALSE))
  names(crossprod) <- "V1"
  dataset <- bind_cols(dataset, crossprod)
  formula <- as.formula(paste0(name, " ~ ", namepair[[1]], " + ", namepair[[2]], " + V1"))
  tees <- summary(lm(formula = formula, data = dataset))$coefficients[, 't value']
  output <- ifelse(is.na(tees['V1']), NA, tees['V1'])
  names(output) <- paste(namepair, collapse = ".")
  return(output)
    
}

myCrossProdVec <- function(name, namePairMat, dataset){
  namePairMat <- filter(namePairMat, Var1 != name, Var2 != name) 
  result <- apply(namePairMat,1,myCrossProd, name = name, dataset = dataset)
  names(result) <- apply(namePairMat,1,paste0, collapse = ".")
  return(result)
} 

myCrossProdMat <- function(namePairMat, dataset){
  unlist(sapply(namePairMat$Var1, myCrossProdVec, namePairMat = namePairMat, dataset = dataset, simplify = FALSE))
}

