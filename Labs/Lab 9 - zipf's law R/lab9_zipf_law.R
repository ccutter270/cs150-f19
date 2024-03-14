# This program takes a file of text and reads over the file to extract each word. It will print out a table of the top 10 most frequent words in that
# file as well as their counts. Also, a graph will be generated of the Log-log plot of count vs. rank of words in the file.
#
# CS150 Fall 2019 Lab 9
#
# Name: Caroline Cutter
# Section: B
#
# Creativity:
# 1. I incorperated the filename in the plot title
# 2. I generated the plot using ggplot2



# Imports
library(plyr, warn.conflicts=FALSE)
library(stringr, warn.conflicts=FALSE)
library(ggplot2, warn.conflicts=FALSE)





# Split strings on word boundaries, removing any punctuation
# Args:
#   strings: A vector of strings
# Returns a vector of strings (the words)
split_and_strip <- function(strings) {
  # str_subset removes any empty strings, or strings that contain only whitespace.
  # \S is the character class for non white-space characters
  unlist(str_split(str_subset(strings, "\\S+"), boundary("word")))
}




# Read file into a vector of cleaned and normalized words
# Args:
#   filename: Filename to analyze as a string
# Returns a vector of cleaned and normalized words
file_to_words <- function(filename) {
  vector_of_words <- readLines(filename, warn = FALSE)
  stripped_vector <- split_and_strip(vector_of_words)
  new_vector <- tolower(stripped_vector)
  
  return(new_vector)
}





# Create a ranked data frame of words and their counts
# Args:
#   words: Vector of cleaned words
# Returns a data.frame of words and counts in descending order of count
count_and_rank <- function(words) {
  df <- plyr::count(words)
  colnames(df) <- c("Word", "Count") 
  df[order(df$Count, decreasing = TRUE),]
                   
}





# Prompt the user for a file name and construct ranks data.frame
filename <- readline(prompt="Enter a filename: ")
words <- file_to_words(filename)
counts <- count_and_rank(words)




# Print 10 most common words and generate a log-log plot count vs. rank

if (nrow(counts) < 10) {
  print(counts, row.names=FALSE) 
} else{
  print(counts[c(1:10),], row.names=FALSE)  
}


#Regular plot of Count vs Rank
plot(1:nrow(counts), counts$Count, xlab="Rank", ylab="Count", main =paste("Log-log plot of count vs. rank of words in", filename), log="xy")




#ggplot of Count vs Rank
plt <- ggplot(counts, aes(x=1:nrow(counts), y=Count)) + geom_point() + 
  xlab("Rank") + ylab("Count") + scale_x_log10() + scale_y_log10() + ggtitle(paste("Log-log plot of count vs. rank of words in", filename))

print(plt)












