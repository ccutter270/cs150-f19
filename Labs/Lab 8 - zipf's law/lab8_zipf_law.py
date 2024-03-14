'''
CSCI150 Fall 2019 Lab 8

Name: Caroline Cutter
Section: <B>

Creativity:
    - I added the file name in the title of the graph
    - I created a table using the data science table fucntion (I kept the old table too for requirments)
    - Prints out usage error if the wrong inputs are entered
    
    Sorry for the lack of creativity on this lab:( It was a very busy week!
    
'''

#Imports
import numpy as np
import datascience as ds
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
import sys


#Constants

PUNCTUATION = ",'?.!*{};:/"



def get_1st(alist):
    '''
    Gets the first item of a list
    
    Args:
        alist: a list
    
    Returns: First item of that list
    '''
    return alist[0]


def get_2nd(alist):
    '''
    Gets the second item of a list
    
    Args:
        alist: a list
    
    Returns: Second item of that list
    '''
    return alist[1]






def read_corpus(filename):
    '''
    Takes a file and creates a list of the word with puncutation removed
    
    Args:
        filename: name of file to read
        
    Returns:
        list of words from that file

    '''
    words = []
    with open(filename, "r") as file:
        for lines in file:
            line = lines.lower().split()
            for word in line:
                words.append(word.strip(PUNCTUATION))
    return words
    
    
    
    
    

def count_and_rank(word_list):
    '''
    Takes a list of words and returns a touple of two lists; the first is a list of words in the list
    and the second is a list of that words counts. They are in ranking from greatest to least
    
    Args:
        word_list: a list of words
     
    Returns:
        A touple of two lists; words in word_list and their count; in order from greatest to least
    '''
    new_dict = {}
    for word in word_list:
        if word in new_dict:
            new_dict[word] += 1
        else:
            new_dict[word] = 1
    
    sorted_dict = sorted(new_dict.items(), key=get_2nd, reverse=True)
    
    word_list = []
    count_list = []
    
    for word in sorted_dict:
        word_list.append(get_1st(word))
        count_list.append(get_2nd(word))
        
    return word_list, count_list
    
    
  
def count_rank_table(words_and_rank_tuple):
    '''
    Prints a table of the most appeared 10 words from a tuple of words and thier counts
    
    Args:
        count_and_rank_tuple: tuple of words and their counts

    Returns: None
    '''
    index = 0
    print("Word \t Count\n")
    for word in count_and_rank[0]:
        print(str(word) + "\t" + str(count_and_rank[1][index]))
        index += 1
        if index == 10:
            break
    


def count_rank_table_with_ds(words_and_rank_tuple):
    '''
    Prints a table of the most appeared 10 words from a tuple of words and thier counts using data science table
    
    Args:
        count_and_rank_tuple: tuple of words and their counts

    Returns: None
    '''
    count_rank_table = ds.Table().with_columns(
        'Words', count_and_rank[0][0:11],
        'Count', count_and_rank[1][0:11]
        )
    print(count_rank_table)



def word_count_plot(words_counts, filename):
    '''
    Creates a plot of words based on their rank and count using log scales.
    
    Args:
        words_counts: a tuple of wors and their counts
        filename: filename of where the words and their counts are from
    '''
    counts = words_counts[1]
    ranks = range(1, len(counts) + 1)
    plt.plot(ranks, counts, "bo")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Rank")
    plt.ylabel("Count")
    plt.title("“Log-log plot of count vs. rank of words in" + str(filename))
    plt.show()
    



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python3 lab8_zipf_law.py <file>')
    else:
        filename = sys.argv[1]
        word_list = read_corpus(filename)
        count_and_rank = count_and_rank(word_list)
        count_rank_table_with_ds(count_and_rank)
        word_count_plot(count_and_rank, filename)
        
 
    