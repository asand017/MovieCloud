#!/usr/bin/python
# generate word cloud from movie subtitle file
# import re
import pysrt
#import matplotlib.pyplot as pPlot
#from wordcloud import WordCloud
#import numpy as npy
#from PIL import Image

# custom class to keep the top word results for given film
# 	contents: list[15] (words), list[15] (word's count), both sorted from highest to lowest
#class TopTerms:
#	def __init__(self, 

subs = pysrt.open("subtitles/ouatih.srt")

# get stop words
stops = []
stopwords = open("stopwords.txt")
for sw in stopwords:
	stops.append(sw.replace("\n", ""))
stopwords.close()
print(stops)

# film word list dictionary
movieWords = {}

def toText(subt): 	# function to convert srt file to a text file, in 'sub-out.txt', also cleans the 
					# the text for indexing
	
	lineCount = len(subt) # how many lines the film

	subout = open("sub-out.txt", "w+")
	for i in range(0, lineCount):
		line = subt[i].text # begin word clean here
		#print(type(line))
		newLine = cleanLine(line)
		newLine = removeStop(newLine)
		dictUpdate(newLine)
		subout.write(newLine)
		subout.write('\n')

	subout.close()
	
def cleanLine(line): # remove stop words for txt	
	newline = line.replace("<i>","")
	newline = newline.replace("</i>", "")
	newline = newline.replace("\'s", "")
	newline = newline.replace(",", "")
	newline = newline.replace(".", "")
	newline = newline.replace("-", " ")
	newline = newline.replace("?", "")
	newline = newline.replace("!", "")
	newline = newline.replace("$", "")
	newline = newline.replace(":", "")
	newline = newline.replace("\"", "")
	return newline

def removeStop(line):
	words = line.split()
	space = " "
	newline = []
	for word in words: # check against stops list
		if(word.isdigit()):
			continue;

		word = word.lower()
		if(word not in stops):
			newline.append(word)
			if(word in movieWords):
				movieWords[word] = movieWords[word] + 1
			else:
				movieWords[word] = 1
			# also update dictionary
			
				
	newline = space.join(newline)
	return newline

def dictUpdate(line):
	words = line.split()	

toText(subs)

#for key in sorted(movieWords):
	#print("%s: %s" % (key, movieWords[key]))

#print(sorted(movieWords.values()))
#print(movieWords)
#print("fuck count: ", movieWords["fuck"])
# create user input search for word count)

#print(movieWords)

# at this point, we want to generate an index of the search terms (counting terms in the subtitle doc)
# i.e. fuck, 87

# a simple word count application, after filtering stopwords, top results are printed into word cloud
